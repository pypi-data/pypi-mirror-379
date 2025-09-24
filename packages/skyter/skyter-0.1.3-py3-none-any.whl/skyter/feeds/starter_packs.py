from typing import Iterable
import pyperclip

from textual.app import ComposeResult, SystemCommand
from textual.binding import Binding
from rich.text import Text
from rich.panel import Panel

from skyter.utils import handle_to_link
from skyter.data_classes import StarterPack
from skyter.feeds.feed import FeedView, FeedPanel

class StarterPackFeedView(FeedView):
    """FeedView for starter pack feeds"""

    BINDINGS = [
        Binding("enter", "view_users", "Users"),
        Binding("p", "view_profile", "Profile"),
        Binding("f", "load_feed", "Feed"),
    ]

    async def create_list_items(self, items: list[dict]) -> list[FeedView.Listed]:
        """Create Listed objects from list of dictionaries"""
        return [self.Listed(StarterPack.from_dict(item)) for item in items if item is not None]

    async def generate_data(self, new_items: bool = False, reset_pagination: bool = False):
        """Make client calls to retrieve data for building feed."""

        match self.source.feed_type:

            case 'user_starter_packs':
                items = await self.client.get_user_starter_packs(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

        if items is None: # e.g., when user profile is blocked
            return []

        if len(items) == 0 and not new_items:
            if len(self.feed_data) == 0:
                self.app.notify("No results found", severity="warning")
            else:
                self.app.notify("No more results", severity="warning")

        return items

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        highlighted = self._get_highlighted(suppress_notification=True)
        if highlighted:
            yield SystemCommand("List users", "View users included in starter pack", self.action_view_users)
            yield SystemCommand("Profile", "Open profile of highlighted starter pack creator", self.action_view_profile)
            yield SystemCommand("View feed", "Load feed for highlighted starter pack", self.action_load_feed)
            yield SystemCommand("Copy URI", "Copy highlighted starter pack list URI to clipboard", self.action_copy_uri)
        yield from super().offer_widget_commands()

    def action_view_profile(self) -> None:
        """Request the app to build user feed for highlighted feed author"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.starter_pack.creator['handle']
            self.screen.action_build_user_feed(handle)

    def action_view_users(self) -> None:
        """Request the app to build list people feed for highlighted starter pack"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            list_uri = highlighted.starter_pack.list_uri
            name = highlighted.starter_pack.display_name
            self.screen.action_build_list_people(list_uri, name)

    def action_load_feed(self) -> None:
        """Request the app to rebuild the feed based on highlighted custom feed/list."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            list_uri = highlighted.starter_pack.list_uri
            name = highlighted.starter_pack.display_name
            self.screen.action_build_list_feed(list_uri, name)

    def action_copy_uri(self) -> None:
        """Action to copy the uri of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted:
            uri = highlighted.starter_pack.list_uri
            self.notify("copied URI to clipboard")
            pyperclip.copy(uri)


    class Listed(FeedView.Listed):
        """Custom ListItem container to list StarterPackPanel objects in StarterPackFeedView"""

        def compose(self) -> ComposeResult:
            yield StarterPackPanel(self.data_obj)


class StarterPackPanel(FeedPanel):
    """Feed panel for rendering starter pack information."""

    def __init__(self, starter_pack: StarterPack, is_embedded: bool = False, **kwargs):
        self.starter_pack = starter_pack
        self.is_embedded = is_embedded
        super().__init__(**kwargs)

    def render(self):

        body_style = style=self.app.theme_variables["text-secondary"] if self.is_embedded else None
        if self.starter_pack.description is None:
            body = Text('[No description provided]', style=body_style)
        else:
            body = Text(self.starter_pack.description, style=body_style)

        title = self.build_title()
        subtitle = self.build_subtitle() if not self.app.hide_metrics else ''

        return Panel(
            body,
            title=title,
            title_align="left",
            subtitle=subtitle,
            border_style = 'cyan' if self.is_embedded else self.app.theme_variables["foreground"],
            padding=(1, 2),
        )

    def build_title(self):
        """Build panel title"""
        title = Text()
        title.append(self.starter_pack.display_name, style="bold")
        title.append(" · starter pack by ")
        title.append(handle_to_link(self.starter_pack.creator['handle']))
        return title

    def build_subtitle(self):
        """Build panel subtitle"""
        return Text(f'{self.starter_pack.joined_count} users have joined')
