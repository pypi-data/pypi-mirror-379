from typing import Iterable
import pyperclip

from textual.app import ComposeResult, SystemCommand
from textual.widgets import ListView
from textual.binding import Binding
from textual import work
from rich.text import Text

from skyter.utils import abbrev_num, handle_to_link
from skyter.data_classes import CustomFeed
from skyter.ui import SplitTitlePanel
from skyter.feeds.feed import FeedView, FeedPanel

class CustomFeedView(FeedView):
    """FeedView for custom feed-based and list-based feeds (i.e., feed search results, suggested feeds, saved feeds, lists)"""

    BINDINGS = [
        Binding("enter", "load_feed", "Load Feed"),
        Binding("s", "save_feed", "Save Feed"),
        Binding("s", "unsave_feed", "Unsave Feed"),
        Binding("p", "view_profile", "Profile"),
        Binding("u", "view_users", "Users"),
    ]

    async def create_list_items(self, items: list[dict]) -> list[FeedView.Listed]:
        """Create Listed objects from list of dictionaries"""
        return [self.Listed(CustomFeed.from_dict(item)) for item in items if item is not None]

    async def generate_data(self, new_items: bool = False, reset_pagination: bool = False):
        """Make client calls to retrieve data for building feed."""

        match self.source.feed_type:

            case 'search':
                items = await self.client.search_feeds(query=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)
                for i in items:
                    i['type'] = 'feed'

            case 'user_lists':
                items = await self.client.get_user_lists(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)
                for i in items:
                    i['type'] = 'list'

            case 'saved_feeds':
                feeds = await self.client.get_saved_feeds()
                items = []
                for f in feeds:
                    item = f['feed'] if f['type'] != 'timeline' else {
                        'display_name': 'Following',
                        'description': 'Following timeline',
                    }
                    item['type'] = f['type']
                    item['pinned'] = f['pinned']
                    items.append(item)

        if items is None: # e.g., when user profile is blocked
            return []

        if len(items) == 0 and not new_items:
            if len(self.feed_data) == 0:
                self.app.notify("No results found", severity="warning")
            else:
                self.app.notify("No more results", severity="warning")

        return items

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Override default method to check if an action should be available."""

        # set s keybinding depending on feed type
        if action == "save_feed" and self.source.feed_type == 'saved_feeds':
            return False
        elif action == "unsave_feed" and self.source.feed_type != 'saved_feeds':
            return False

        # show view_users only when lists are included
        elif action == "view_users" and self.source.feed_type not in ['saved_feeds', 'user_lists']:
            return False

        return True

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        highlighted = self._get_highlighted(suppress_notification=True)
        if highlighted:
            yield SystemCommand("View feed", "Load highlighed feed", self.action_load_feed)
            yield SystemCommand("Profile", "Open profile of highlighted feed creator", self.action_view_profile)
            yield SystemCommand("Save feed", "Save feed to list of saved feeds", self.action_save_feed)
            yield SystemCommand("Unsave feed", "Remove feed from list of saved feeds", self.action_unsave_feed)
            yield SystemCommand("List users", "View users included in list", self.action_view_users)
            yield SystemCommand("Copy URI", "Copy highlighted feed URI to clipboard", self.action_copy_uri)
        yield from super().offer_widget_commands()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Override parent action to fetch more data on last index for feeds without pagination."""

        if self.source.feed_type != 'saved_feeds':
            pass # super called automatically
        else:
            event.prevent_default()
            event.stop()

    def action_load_feed(self) -> None:
        """Request the app to rebuild the feed based on highlighted custom feed/list."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            uri = getattr(highlighted.cust_feed, 'uri', None)
            name = highlighted.cust_feed.display_name
            item_type = highlighted.cust_feed.item_type
            if item_type == 'timeline':
                self.screen.action_build_timeline()
            elif item_type == 'feed':
                self.screen.action_build_custom_feed(uri, name)
            elif item_type == 'list':
                self.screen.action_build_list_feed(uri, name)

    @work
    async def action_save_feed(self) -> None:
        """Save highlighted custom feed"""
        highlighted = self._get_highlighted()

        if highlighted is not None:

            uri = highlighted.cust_feed.uri
            feed_name = highlighted.cust_feed.display_name
            saved = await self.client.is_feed_saved(uri)

            if saved:
                self.app.notify(f'"{feed_name}" is already saved.', severity="warning")

            else:
                result = await self.client.save_feed(uri)
                if result:
                    self.app.notify(f'Saved feed "{feed_name}"')
                else:
                    self.app.notify(f'Failed to save feed "{feed_name}"', severity="error")

    @work
    async def action_unsave_feed(self) -> None:
        """Unsave highlighted custom feed"""
        highlighted = self._get_highlighted()

        if highlighted is not None:

            feed_name = highlighted.cust_feed.display_name

            if highlighted.cust_feed.item_type == 'timeline':
                self.app.notify(f'"{feed_name}" cannot be unsaved.', severity="warning")
                return

            uri = highlighted.cust_feed.uri
            saved = await self.client.is_feed_saved(uri)

            if saved:
                result = await self.client.remove_saved_feed(uri)
                if result:
                    self.app.notify(f'Removed saved feed "{feed_name}"')
                    await self.refresh_items()
                else:
                    self.app.notify(f'Failed to remove saved feed "{feed_name}"', severity="error")
            else:
                self.app.notify(f'"{feed_name}" is not saved so could not be unsaved.', severity="warning")

    def action_view_profile(self) -> None:
        """Request the app to build user feed for highlighted feed author"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            if highlighted.cust_feed.item_type == 'timeline':
                self.app.notify('No profile to view', severity="warning")
                return
            handle = highlighted.cust_feed.creator['handle']
            self.screen.action_build_user_feed(handle)

    def action_view_users(self) -> None:
        """Request the app to build list people feed for highlighted list"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            item_type = highlighted.cust_feed.item_type
            if item_type == 'list':
                uri = highlighted.cust_feed.uri
                name = highlighted.cust_feed.display_name
                self.screen.action_build_list_people(uri, name)
            else:
                self.app.notify(f'Cannot get people for {item_type}', severity="warning")

    def action_copy_uri(self) -> None:
        """Action to copy the uri of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted:
            uri = highlighted.cust_feed.uri
            self.notify("copied URI to clipboard")
            pyperclip.copy(uri)


    class Listed(FeedView.Listed):
        """Custom ListItem container to list CustomFeedPanel objects in CustomFeedView"""

        def compose(self) -> ComposeResult:
            yield CustomFeedPanel(self.data_obj)


class CustomFeedPanel(FeedPanel):
    """Feed panel for rendering custom feed information"""

    def __init__(self, cust_feed: CustomFeed, is_embedded: bool = False, **kwargs):
        self.cust_feed = cust_feed
        self.is_embedded = is_embedded
        super().__init__(**kwargs)

    def render(self):
        body_style = self.app.theme_variables["text-secondary"] if self.is_embedded else None
        if self.cust_feed.description is None:
            body = Text('[No description provided]', style=body_style)
        else:
            body = Text(self.cust_feed.description, style=body_style)

        title = self.build_title()
        subtitle = self.build_subtitle() if not self.app.hide_metrics else ''

        return SplitTitlePanel(
            body,
            left_title=title,
            right_title=Text("📌") if self.cust_feed.pinned else None,
            subtitle=subtitle,
            border_style = 'cyan' if self.is_embedded else self.app.theme_variables["foreground"],
            padding=(1, 2),
        )

    def build_title(self):
        """Build panel title"""
        title = Text()
        title.append(self.cust_feed.display_name, style="bold")
        if self.cust_feed.creator:
            title.append(f" · {self.cust_feed.item_type} by ")
            title.append(handle_to_link(self.cust_feed.creator['handle']))
        return title

    def build_subtitle(self):
        """Build panel subtitle"""
        if self.cust_feed.item_type == 'feed':
            liked_color = f"bold {self.app.theme_variables["text-success"]}"
            return Text(f'{abbrev_num(self.cust_feed.like_count)} likes', style=None if self.cust_feed.liked is None else liked_color)
        elif self.cust_feed.item_type == 'list':
            return Text(f'{self.cust_feed.item_count} people')
        return Text()
