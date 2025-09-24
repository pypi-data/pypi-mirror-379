from typing import Any, Iterable

from textual.app import ComposeResult, SystemCommand
from textual.widgets import ListItem, ListView, Static
from textual.widget import Widget
from textual.binding import Binding
from textual import work

from skyter.bsky import BlueSkyClient, FeedPaginator
from skyter.data_classes import FeedSource

class FeedPanel(Widget):
    """Abstract class for panel items in feeds"""
    pass

class FeedView(ListView):
    """ListView for atproto feeds."""

    BINDINGS = [
        Binding("ctrl+up", "scroll_top", "Top"),
        Binding("ctrl+down", "scroll_bottom", "Bottom"),
        Binding("t", "view_timeline", "Timeline"),
    ]

    # disable new item monitoring for feeds that do not support pagination or do not have a use case for monitoring
    MONITOR_NEW_EXCLUDE = [
        'thread',
        'saved_feeds',
        'blocks',
        'mutes',
    ]

    # disable new item alerts for notifications, since notification alerts are handled separately; allow auto-updates
    ALERT_NEW_EXCLUDE = ['notifications']

    DEBOUNCE_DELAY = 1

    def __init__(self, client: BlueSkyClient, source: FeedSource, mount_empty: bool = False, **kwargs):
        self.client = client
        self.source = source
        self.mount_empty = mount_empty
        self.feed_data = []
        self.new_available = False
        self.feed_new_items_action = self.app.feed_new_items_action
        self.monitor_new = self.feed_new_items_action and self.app.feed_new_items_check_interval and self.source.feed_type not in self.MONITOR_NEW_EXCLUDE
        self._debounce = False
        super().__init__(*[], **kwargs)

    async def create_list_items(self, items: list[dict]) -> list:
        """Create Listed objects from list of dictionaries"""
        return [self.Listed(item) for item in items if item is not None]

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        if self.source.feed_type not in self.MONITOR_NEW_EXCLUDE:
            yield SystemCommand("Toggle auto-updates", "Turn on/off feed auto-updates for new items", self.action_toggle_auto_update)

    async def on_mount(self):
        """Get initial items once mounted"""
        self.loading = True
        if not self.mount_empty:
            await self.more_items()
        if self.monitor_new:
            self.new_checker = self.set_interval(self.app.feed_new_items_check_interval, self.new_monitor)

    def _get_highlighted(self, suppress_notification: bool = False) -> FeedPanel:
        """Get highlighted item"""

        highlighted_item = self.highlighted_child

        if highlighted_item:
            return highlighted_item.query_one(FeedPanel)

        else:
            if not suppress_notification:
                self.notify("No item highlighted", severity="warning")
            return None

    async def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Request more items when last item is highlighted"""
        if event.list_view.index == len(self) - 1: # when last item is reached, get more items
            await self.more_items()
        elif event.list_view.index == 0 and self.new_available: # when first item is highlighted and new items are available, get new
            await self.new_items()

    async def action_cursor_up(self) -> None:
        """When already on first index, up will fetch new items"""
        if self.index == 0 and self.source.feed_type not in self.MONITOR_NEW_EXCLUDE:
            await self.new_items()
        super().action_cursor_up()

    async def more_items(self, reset_pagination: bool = False) -> None:
        """Fetch data and add more Listed items to the feed"""
        if self._debounce: return
        self._debounce = True
        data = await self.generate_data(reset_pagination=reset_pagination)
        items = await self.create_list_items(data)
        self.feed_data = self.feed_data + data
        await self.extend(items)
        self.loading = False
        self.set_timer(self.DEBOUNCE_DELAY, lambda: setattr(self, '_debounce', False))

    async def refresh_items(self):
        """Refresh feed and reset pagination."""
        self.loading = True
        self.clear()
        self.scroll_home(animate=False)
        self.feed_data = []
        self.new_available = False
        self._debounce = False
        await self.more_items(reset_pagination=True)
        self.index = 0
        if self.monitor_new:
            self.new_checker.reset()
            self.new_checker.resume()
        self.refresh_bindings()

    async def refresh_from_data(self, feed_data: list, paginator: FeedPaginator, idx: int):
        """Refresh feed from a stored feed state"""
        self.loading = True
        self.clear()
        self.feed_data = feed_data
        self.new_available = False
        items = await self.create_list_items(self.feed_data)
        await self.extend(items)
        self.client.paginator = paginator
        if self.monitor_new and self.source.feed_type:
            self.new_checker.reset()
            self.new_checker.resume()
        self.refresh_bindings()
        self.loading = False
        self.index = idx
        self.set_timer(.1, self._scroll_to_index)

    async def new_items(self, auto_fetched: bool = False) -> None:
        """Fetch new data and add more Listed items to top of the feed"""
        if self._debounce: return
        self._debounce = True
        data = await self.generate_data(new_items=True)
        if len(data) > 0:
            items = await self.create_list_items(data)
            self.feed_data = data + self.feed_data
            self.new_available = False
            if self.source.feed_type == "notifications": self.screen.notification_count = 0
            if not auto_fetched and hasattr(self, 'new_checker'):
                self.new_checker.reset()
                self.new_checker.resume()
            self.screen.update_title()
            idx = self.index
            await self.insert(0, items)
            self.index = idx + len(items)
            if auto_fetched:
                self.scroll_home(animate=False)
            self.app.notify('Got new items')
        elif not auto_fetched:
            self.app.notify("No new items found", severity="warning")
        self.set_timer(self.DEBOUNCE_DELAY, lambda: setattr(self, '_debounce', False))

    async def check_new_available(self) -> None:
        """Check if new items are available and if so disable monitor and display indicator"""
        new_items = await self.client.paginator.check_new_available()
        if new_items:
            self.new_available = True
            self.screen.update_title(new_available=True)
            self.new_checker.pause()
            self.app.notify('New items available')

    @work
    async def new_monitor(self) -> None:
        """Worker to monitor new feed items"""
        if self.source.feed_type in self.MONITOR_NEW_EXCLUDE: return
        if self.feed_new_items_action == 'alert':
            if self.source.feed_type in self.ALERT_NEW_EXCLUDE: return
            await self.check_new_available()
        elif self.feed_new_items_action == 'update':
            await self.new_items(auto_fetched=True)

    def action_toggle_auto_update(self):
        """Action to toggle automatic updates when new feed items are available"""

        if self.feed_new_items_action != 'update' or not hasattr(self, 'new_checker'):
            self.feed_new_items_action = 'update'
            self.monitor_new = True
            self.new_available = False
            if hasattr(self, 'new_checker'):
                self.new_checker.reset()
                self.new_checker.resume()
            else:
                self.new_checker = self.set_interval(self.app.feed_new_items_check_interval or 60, self.new_monitor)
            self.app.notify('New feed items will be added automatically')

        else:
            self.feed_new_items_action = self.app.feed_new_items_action if self.app.feed_new_items_action != 'update' else 'alert'
            if not self.feed_new_items_action:
                self.monitor_new = False
                self.new_checker.pause()
            else:
                self.new_checker.reset()
            self.app.notify('New feed items will no longer be added automatically')

    def action_scroll_top(self):
        """Scroll to top of feed and highlight first item"""
        self.scroll_home(animate=False, on_complete=self._highlight_first)

    def _highlight_first(self):
        """Highlight first item in list / triggers get new if new items available"""
        self.index = 0

    def action_scroll_bottom(self):
        """Scroll to bottom of feed and highlight last item"""
        self.scroll_end(animate=False, on_complete=self._highlight_last)

    def _highlight_last(self):
        """Highlight last item in list / triggers get more"""
        self.index = len(self) - 1

    def _scroll_to_index(self):
        listed = self.query(self.Listed)
        if self.index < len(listed):
            self.scroll_to_widget(listed[self.index], animate=True)

    def action_view_timeline(self) -> None:
        """Request the app to build the following timeline."""
        self.screen.action_build_timeline()


    class Listed(ListItem):
        """ListItem container to list FeedPanel objects in FeedView object"""

        def __init__(self, data_obj: Any, **kwargs):
            self.data_obj = data_obj
            self.cls = type(data_obj).__name__
            super().__init__(**kwargs)

        def compose(self) -> ComposeResult: # overwritten by child classes
            yield Static(f'{self.cls} obj')

        def swap_data(self, data_obj: Any):
            """Change data object and trigger recompose"""
            self.data_obj = data_obj
            self.cls = type(data_obj).__name__
            self.refresh(recompose=True)
