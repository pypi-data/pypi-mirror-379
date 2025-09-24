from typing import Iterable

from textual.app import ComposeResult, SystemCommand
from textual.screen import Screen
from textual.widgets import Footer
from textual.containers import Vertical
from textual.binding import Binding
from textual.app import ComposeResult
from textual.screen import Screen
from textual import work

from skyter.bsky import BlueSkyClient
from skyter.data_classes import FeedSource, Post
from skyter.ui import BreakpointContainer
from skyter.login import LoginScreen
from skyter.compose.post_compose import PostComposeScreen
from skyter.feeds.container import FeedViewContainer
from skyter.feeds.feed import FeedView
from skyter.profile import ProfileView
from skyter.search import SearchSubmitted, SearchView


class MainScreen(Screen):
    """Main app screen"""

    BINDINGS = [
        Binding("ctrl+n", "open_post_compose", "New Post"),
        Binding("/", "toggle_search_panel", "Search"),
        Binding("alt+left", "previous_feed", "Back"),
        Binding("alt+right", "next_feed", "Forward"),
        Binding("escape", "hide_edge_panels", "Close panel"),
    ]

    def __init__(self, client: BlueSkyClient, source: FeedSource = FeedSource(), **kwargs):
        self.client = client
        self.source = source
        super().__init__(**kwargs)

        # state variables
        self._current_panel = None
        self.notification_count = 0

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Override default method to check if an action should be available."""

        # hide search binding when search panel active
        if action == "toggle_search_panel" and self._current_panel and self._current_panel == 'search-panel':
            return False

        # hide close panel binding when no panel active
        if action == "hide_edge_panels" and not self._current_panel:
            return False

        # hide back on initial feed
        if action == "previous_feed" and self.app._feed_stack_idx == 0:
            return False

        # hide forward on last feed
        if action == "next_feed" and self.app._feed_stack_idx == len(self.app._feed_stack) - 1:
            return False

        return True

    def offer_screen_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        yield SystemCommand("Home", "View home feed", self.action_build_home)
        yield SystemCommand("Timeline", "View following timeline", self.action_build_timeline)
        yield SystemCommand("My profile", "View your own profile", self.action_build_user_feed)
        yield SystemCommand("My followers", "Show list of my followers", self.action_build_follower_list)
        yield SystemCommand("My follows", "Show list of users I am following", self.action_build_follows_list)
        yield SystemCommand("My likes", "Show my liked posts", self.action_build_user_likes)
        yield SystemCommand("Search", "Open (or close) search panel", self.action_toggle_search_panel)
        yield SystemCommand("Repeat search", "Repeat most recent search", self.repeat_search)
        yield SystemCommand("Log out", "End session and return to login screen", self.log_out)
        yield SystemCommand("Suggested feeds", "Show suggested custom feeds", self.get_suggested_feeds)
        yield SystemCommand("Saved feeds", "Show saved and pinned feeds", self.get_saved_feeds)
        yield SystemCommand("Notifications", "Show notifications", self.action_build_notifications)
        yield SystemCommand("Mentions", "Show mention notifications", self.action_build_mentions)
        yield SystemCommand("Mute list", "Show lists of accounts I am muting", self.action_build_mute_list)
        yield SystemCommand("Block list", "Show lists of accounts I am blocking", self.action_build_block_list)
        yield SystemCommand("My lists", "Show lists I have created", self.action_build_user_lists)
        if self.app.notification_check_interval:
            yield SystemCommand("Pause notifications", "Temporarily hide notification count", self.action_pause_notifications)
        elif self.app._settings.notification_check_interval:
            yield SystemCommand("Resume notifications", "Resume displaying notification count", self.action_resume_notifications)
        if self.app._feed_stack_idx > 0:
            yield SystemCommand("Back", "Go to the previous feed", self.action_previous_feed)
        if self.app._feed_stack_idx < len(self.app._feed_stack) - 1:
            yield SystemCommand("Forward", "Go to the next feed", self.action_next_feed)

        # Show close panel command if panel active
        if self._current_panel:
            yield SystemCommand("Close panel", "Close edge panel", self.action_hide_edge_panels)

    def compose(self) -> ComposeResult:
        """Compose the app widgets"""
        with BreakpointContainer():
            with Vertical(id="profile-panel", classes="edge-panel hidden"):
                yield ProfileView(client=self.client, id="profile-view")
            with Vertical(id="search-panel", classes="edge-panel hidden"):
                yield SearchView(id="search-view")
            yield FeedViewContainer(client=self.client, source=self.source, id="feedview-container")
        if self.app.show_footer:
            yield Footer()

    async def on_mount(self) -> None:
        """Set title, focus feed, add timers on mount"""
        if self.app.notification_check_interval:
            await self.update_notification_count()
        self.update_title()
        self._focus_feed()
        if self.app.notification_check_interval:
            self.set_interval(self.app.notification_check_interval, self.check_notifications)

    @work
    async def action_build_user_feed(self, handle: str | None = None, params: dict | None = None) -> None:
        """Action to build user feed. If no handle is specified, get own profile."""
        if not handle:
            handle = self.client.handle
        if not params:
            params = {
                'post_type': 'posts_and_author_threads',
                'title': f'@{handle}\'s posts'
            }
        profile_view = self.query_one("#profile-view")
        profile_view.loading = True
        self.show_edge_panel('profile-panel')
        source = FeedSource(target=handle, feed_type="user", params=params)
        await self.reset_feed(source)
        await self.build_profile_panel(handle)
        self.notify(f"Got feed for user {handle}")

    @work
    async def action_build_custom_feed(self, uri: str, feed_name: str) -> None:
        """Action to build post feed for custom feed"""
        self.action_hide_edge_panels()
        source = FeedSource(target=uri, feed_type="custom_feed", params={'title': feed_name})
        await self.reset_feed(source)
        self.notify(f"Got custom feed: {uri}")

    @work
    async def action_build_list_feed(self, uri: str, feed_name: str) -> None:
        """Action to build post feed for list"""
        self.action_hide_edge_panels()
        source = FeedSource(target=uri, feed_type="list_feed", params={'title': feed_name})
        await self.reset_feed(source)
        self.notify(f"Got list feed: {uri}")

    @work
    async def action_build_list_people(self, uri: str, feed_name: str) -> None:
        """Action to build user feed of users included in list"""
        self.action_hide_edge_panels()
        source = FeedSource(target=uri, feed_type="list_people", params={'title': feed_name})
        await self.reset_feed(source)
        self.notify(f"Got users for in feed: {feed_name}")

    @work
    async def action_build_user_lists(self, handle: str | None = None) -> None:
        """Action to build list feed of lists created by user"""
        if handle is None:
            handle = self.client.handle
        self.action_hide_edge_panels()
        source = FeedSource(target=handle, feed_type="user_lists")
        await self.reset_feed(source)
        self.notify(f"Got lists by {handle}")

    @work
    async def action_build_user_starter_packs(self, handle: str | None = None) -> None:
        """Action to build starter packs feed"""
        if handle is None:
            handle = self.client.handle
        self.action_hide_edge_panels()
        source = FeedSource(target=handle, feed_type="user_starter_packs")
        await self.reset_feed(source)
        self.notify(f"Got starter packs by {handle}")

    @work
    async def action_build_timeline(self) -> None:
        """Action to build following timeline"""
        self.action_hide_edge_panels()
        await self.reset_feed(FeedSource())
        self.notify(f"Got feed for timeline")

    @work
    async def action_build_home(self) -> None:
        """Action to build feed from initial source defined in settings"""
        self.action_hide_edge_panels()
        await self.reset_feed(self.app.initial_source)
        self.notify(f"Got home feed")

    @work
    async def action_build_thread(self, uri: str, title_params: dict) -> None:
        """Action to build post thread feed"""
        self.action_hide_edge_panels()
        await self.reset_feed(FeedSource(target=uri, feed_type="thread", params=title_params))
        self.notify(f"Got thread for {uri}")

    @work
    async def action_build_likes(self, uri: str, title_params: dict) -> None:
        """Action to build feed for likers of a post"""
        self.action_hide_edge_panels()
        await self.reset_feed(FeedSource(target=uri, feed_type="likes", params=title_params))

    @work
    async def action_build_reposts(self, uri: str, title_params: dict) -> None:
        """Action to build feed for reposters of a post"""
        self.action_hide_edge_panels()
        await self.reset_feed(FeedSource(target=uri, feed_type="reposts", params=title_params))
        self.notify(f"Got likes for {uri}")

    @work
    async def action_build_quotes(self, uri: str, title_params: dict) -> None:
        """Action to build feed for quotes of a post"""
        self.action_hide_edge_panels()
        await self.reset_feed(FeedSource(target=uri, feed_type="quotes", params=title_params))

    @work
    async def action_build_follows_list(self, handle: str | None = None) -> None:
        """Action to build user follows feed. If no handle is specified, get own follows."""
        profile_view = self.query_one("#profile-view")
        profile_view.loading = True
        self.show_edge_panel('profile-panel')
        source = FeedSource(target=handle, feed_type="follows")
        await self.reset_feed(source)
        await self.build_profile_panel(handle)
        self.notify(f"Got follows for @{handle}")

    @work
    async def action_build_follower_list(self, handle: str | None = None) -> None:
        """Action to build user followers feed. If no handle is specified, get own followers."""
        profile_view = self.query_one("#profile-view")
        profile_view.loading = True
        self.show_edge_panel('profile-panel')
        source = FeedSource(target=handle, feed_type="followers")
        await self.reset_feed(source)
        await self.build_profile_panel(handle)
        self.notify(f"Got followers for @{handle}")

    @work
    async def action_build_user_likes(self, handle: str | None = None) -> None:
        """Action to build user liked posts feed. If no handle is specified, get own likes."""
        profile_view = self.query_one("#profile-view")
        profile_view.loading = True
        self.show_edge_panel('profile-panel')
        if handle is None:
            handle = self.client.handle
        source = FeedSource(target=handle, feed_type="user_likes")
        await self.reset_feed(source)
        await self.build_profile_panel(handle)
        self.notify(f"Got followers for @{handle}")

    @work
    async def action_build_mute_list(self) -> None:
        """Action to build muted users feed."""
        self.action_hide_edge_panels()
        source = FeedSource(feed_type="mutes")
        await self.reset_feed(source)
        self.notify(f"Got mute list")

    @work
    async def action_build_block_list(self) -> None:
        """Action to build blocked users feed."""
        self.action_hide_edge_panels()
        source = FeedSource(feed_type="blocks")
        await self.reset_feed(source)
        self.notify(f"Got block list")

    @work
    async def on_search_submitted(self, event: SearchSubmitted) -> None:
        """Handle when search is submitted"""
        source = FeedSource(target=event.query, params=event.params, feed_type="search")
        await self.reset_feed(source)
        self.notify(f"Showing results for \"{event.query}\"")

    @work
    async def repeat_search(self):
        """Search based on existing values in the search view form."""
        search_view = self.query_one('#search-view')
        search_view.handle_search()

    @work
    async def action_build_tag_result(self, query: str):
        """Action to fill search form and conduct to search for a given query, e.g., after clicking a hashtag."""
        if self._current_panel and self._current_panel != 'search-panel':
            self.action_hide_edge_panels()
        search_view = self.query_one('#search-view')
        search_view.reset(query)
        search_view.handle_search()

    @work
    async def get_suggested_feeds(self):
        """Action to build feed of suggested feeds by passing empty feed search."""
        self.action_hide_edge_panels()
        source = FeedSource(feed_type='search', params={'search_type': 'feeds'})
        await self.reset_feed(source)
        self.notify("Showing suggested feeds")

    @work
    async def get_saved_feeds(self):
        """Action to build feed of saved feeds."""
        self.action_hide_edge_panels()
        source = FeedSource(feed_type='saved_feeds')
        await self.reset_feed(source)
        self.notify("Showing saved feeds")

    @work
    async def action_build_notifications(self):
        """Action to build notifications feed."""
        self.action_hide_edge_panels()
        source = FeedSource(feed_type='notifications', params={'title': 'Notifications'})
        self.notification_count = 0
        await self.reset_feed(source)
        self.notify("Showing notifications")

    @work
    async def action_build_mentions(self):
        """Action to build notifications feed, showing only mentions."""
        self.action_hide_edge_panels()
        source = FeedSource(feed_type='notifications', params={
            'reasons': ['reply', 'quote', 'mention'],
            'title': 'Mentions',
        })
        await self.reset_feed(source)
        self.notify("Showing mentions")

    def store_current_feed_state(self) -> None:
        """Update feed stack with current feed state"""
        feed = self.query_one("#the-feed", FeedView)
        current_feed_state = {
            'source': self.source,
            'data': feed.feed_data,
            'paginator': feed.client.paginator,
            'idx': feed.index,
        }
        self.app._feed_stack[self.app._feed_stack_idx] = current_feed_state

    @work
    async def action_previous_feed(self) -> None:
        """Action to return to previous opened feed"""
        self.store_current_feed_state()
        self.app._feed_stack_idx -= 1
        await self.restore_feed()

    @work
    async def action_next_feed(self) -> None:
        """Action to return to next opened feed"""
        self.store_current_feed_state()
        self.app._feed_stack_idx += 1
        await self.restore_feed()

    async def reset_feed(self, source: FeedSource) -> None:
        """Action to rebuild the feed based on source, changing feed type if necessary"""

        self.store_current_feed_state()
        self.app._feed_stack_idx += 1
        self.app._feed_stack = self.app._feed_stack[:self.app._feed_stack_idx] + [{'source': source}]

        self.source = source
        self.update_title()
        feed = self.query_one("#the-feed", FeedView)
        if type(feed).__name__ == source.feedview_type():
            feed.source = source
            await feed.refresh_items()
            feed.focus()
        else:
            feed_container = self.query_one(FeedViewContainer)
            await feed_container.change_feed(source)

    async def restore_feed(self):
        """Restore feed from stored feed state data"""

        feed_state = self.app._feed_stack[self.app._feed_stack_idx]

        self.action_hide_edge_panels()

        build_profile_panel = feed_state['source'].feed_type in ['user', 'follows', 'followers', 'user_likes']
        if build_profile_panel:
            profile_view = self.query_one("#profile-view")
            profile_view.loading = True
            self.show_edge_panel('profile-panel')

        self.source = feed_state['source']
        self.update_title()

        feed = self.query_one("#the-feed", FeedView)
        if type(feed).__name__ == feed_state['source'].feedview_type():
            feed.source = feed_state['source']
            await feed.refresh_from_data(
                feed_data=feed_state['data'],
                paginator=feed_state['paginator'],
                idx=feed_state['idx']
            )
            feed.focus()
        else:
            feed_container = self.query_one(FeedViewContainer)
            await feed_container.reload_feed(feed_state)

        if build_profile_panel:
            await self.build_profile_panel(feed_state['source'].target)

    async def update_notification_count(self) -> int:
        """Make query to get unread notification count. Returns number of new notifications"""
        count = await self.client.get_unread_notification_count()
        if count is None:
            self.app.notify('Error updating notification count', severity="error")
            return 0
        diff = count - self.notification_count
        if diff != 0:
            self.notification_count = count
        return diff

    @work(exclusive=True)
    async def check_notifications(self) -> None:
        """Worker to periodically check for new notifications and update title header"""
        if self.app.notification_check_interval:
            new_notifications = await self.update_notification_count()
            if new_notifications != 0:
                self.update_title()

    def update_title(self, new_available = False) -> None:
        """Create app title header"""
        notifications = f'({self.notification_count}) ' if self.app.notification_check_interval and self.notification_count > 0 else ''
        new_available = f'{' [new available]' if new_available else ''}'

        self.title = notifications + self.source.feedview_title() + new_available

    def action_pause_notifications(self) -> None:
        """Action to disable header notification count display and client API calls"""
        self.app.notification_check_interval = None
        self.update_title()

    def action_resume_notifications(self) -> None:
        """Action to re-enable header notification count display and client API calls"""
        self.app.notification_check_interval = self.app._settings.notification_check_interval
        self.check_notifications()
        self.update_title()

    async def build_profile_panel(self, handle: str | None = None):
        """Make query for user profile data and update profile view edge panel."""
        profile_view = self.query_one("#profile-view")
        if handle is None: handle = self.client.handle
        await profile_view.action_refresh_panel(handle)

    def show_edge_panel(self, panel_name):
        """Show an edge panel by id"""
        if self._current_panel:
            if self._current_panel == panel_name:
                return
            else:
                self.action_hide_edge_panels()
        self._current_panel = panel_name
        panel = self.query_one(f"#{panel_name}")
        panel.remove_class("hidden")

    def action_hide_edge_panels(self):
        """Hide all edge panels"""
        panels = self.query(".edge-panel")
        for panel in panels:
            panel.add_class("hidden")
        self._current_panel = None
        self._focus_feed()

    def action_toggle_search_panel(self):
        """Action to toggle search edge panel"""
        if self._current_panel is not None and self._current_panel == 'search-panel':
            self.action_hide_edge_panels()
        else:
            self.show_edge_panel("search-panel")
            self.query_one("#search-bar").focus()

    def action_open_post_compose(self, reference: Post | None = None, post_type: str | None = None) -> None:
        """Action to open post compose screen."""
        self.app.push_screen(PostComposeScreen(reference=reference, post_type=post_type))

    def log_out(self):
        """Action to log out user and load log-in modal"""
        self.app.client = BlueSkyClient()
        self.app.logged_in = False
        self.app.pop_screen()
        self.app.push_screen(LoginScreen())

    def _focus_feed(self):
        """Focus feed or first available widget"""
        try:
            self.query_one("#the-feed").focus()
        except:
            self._focus_first_available()

    def _focus_first_available(self) -> None:
        """Focus the first available focusable widget."""
        try:
            # Try to find the first focusable widget in the app
            focusable_widgets = self.query("*").filter(lambda w: w.can_focus)
            if focusable_widgets:
                focusable_widgets.first().focus()
        except Exception:
            pass
