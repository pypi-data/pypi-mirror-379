from typing import Iterable
import pyperclip

from textual.app import ComposeResult, SystemCommand
from textual.binding import Binding
from rich.text import Text
from rich.panel import Panel

from skyter.utils import abbrev_num, handle_to_link
from skyter.data_classes import User
from skyter.user_actions import UserActions
from skyter.feeds.feed import FeedView, FeedPanel


class UserFeedView(FeedView, UserActions):
    """FeedView for user-based feeds (i.e., user search results)"""

    BINDINGS = [
        Binding("enter", "view_profile", "Profile"), # default
        Binding("enter", "handle_block", "Toggle block"), # for block list
        Binding("enter", "handle_mute_profile", "Toggle mute"), # for mute list
        Binding("f", "handle_follow", "Follow"),
    ]

    async def create_list_items(self, items: list[dict]) -> list[FeedView.Listed]:
        """Create Listed objects from list of dictionaries"""
        return [self.Listed(User.from_dict(item)) for item in items if item is not None]

    async def _apply_content_policies(self, users: list[dict]) -> list[dict]:
        """Apply non-ignored labels to users as badges"""

        if self.app.subscribed_labels:
            users = await self.client.label_users(users)

        result = []
        for user in users:
            labels = user.get('labels') or []
            badges = []
            for label in labels:
                if label['label'] not in self.app.content_policies:
                    continue
                policy = self.app.content_policies[label['label']]

                if policy['visibility'] != 'ignore':
                    badge = {
                        'label': label['label'],
                        'labeler': label['labeler'],
                        'severity': policy['severity'],
                    }
                    badges.append(badge)

            user['badges'] = badges
            result.append(user)

        return result

    async def generate_data(self, new_items: bool = False, reset_pagination: bool = False):
        """Make client calls to retrieve data for building feed."""

        match self.source.feed_type:

            case 'search':
                items = await self.client.search_users(query=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'follows':
                if not self.app.hide_metrics:
                    items = await self.client.get_follows_detailed(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)
                else:
                    items = await self.client.get_follows(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'followers':
                if not self.app.hide_metrics:
                    items = await self.client.get_followers_detailed(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)
                else:
                    items = await self.client.get_followers(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'likes':
                items = await self.client.get_likes(uri=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'reposts':
                items = await self.client.get_reposts(uri=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'mutes':
                items = await self.client.get_mute_list(limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'blocks':
                items = await self.client.get_block_list(limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'list_people':
                items = await self.client.get_list_people(uri=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

        if items is None: # e.g., when user profile is blocked
            return []

        if len(items) == 0 and not new_items:
            if len(self.feed_data) == 0:
                self.app.notify("No results found", severity="warning")
            else:
                self.app.notify("No more results", severity="warning")

        items = await self._apply_content_policies(items)

        return items

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Override default method to check if an action should be available."""

        # set enter keybinding depending on feed type
        if action == "handle_block" and self.source.feed_type != 'blocks':
            return False
        elif action == "handle_mute" and self.source.feed_type != 'mutes':
            return False
        elif action == 'view_profile' and self.source.feed_type in ['blocks', 'mutes']:
            return False

        return True

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        highlighted = self._get_highlighted(suppress_notification=True)
        if highlighted:
            yield SystemCommand("Profile", "Open profile of highlighted user", self.action_view_profile)
            yield SystemCommand("Follow", "Follow (or unfollow) highlighted user", self.action_handle_follow)
            yield SystemCommand("Mute account", "Mute (or unmute) highlighted user", self.action_handle_mute_profile)
            yield SystemCommand("Block account", "Block (or unblock) highlighted user", self.action_handle_block)
            yield SystemCommand("Copy profile URL", "Copy the profile URL for highlighted user", self.action_copy_profile_link)
        yield from super().offer_widget_commands()

    def action_view_profile(self) -> None:
        """Request the app to build user feed for highlighted user"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.user.handle
            if getattr(self.source, 'target', '') != handle:
                self.screen.action_build_user_feed(handle)

    async def action_handle_follow(self) -> None:
        """Action to follow the highlighted user."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_follow(handle=highlighted.user.handle, following=highlighted.user.following)
            if result['success']:
                highlighted.user.following = result['following']
                highlighted.refresh()

    async def action_handle_mute_profile(self) -> None:
        """Action to mute the highlighted user."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_mute(handle=highlighted.user.handle, muted=highlighted.user.muted)
            if result['success']:
                highlighted.user.muted = result['muted']
                highlighted.refresh()

    async def action_handle_block(self) -> None:
        """Action to block the highlighted user."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_block(handle=highlighted.user.handle, blocking=highlighted.user.blocking, following=highlighted.user.following)
            if result['success']:
                highlighted.user.blocking = result['blocking']
                highlighted.user.following = result['following']
                highlighted.refresh()

    def action_copy_profile_link(self) -> None:
        """Action to copy the URL of the highlighted user."""
        link = self.client.get_profile_url(self.handle)
        self.notify(f"copied profile link to clipboard")
        pyperclip.copy(link)


    class Listed(FeedView.Listed):
        """Custom ListItem container to list UserPanel objects in UserFeedView"""

        def compose(self) -> ComposeResult:
            yield UserFeedView.UserPanel(self.data_obj)


    class UserPanel(FeedPanel):
        """Feed panel for rendering user information"""

        def __init__(self, user: User, **kwargs):
            self.user = user
            super().__init__(**kwargs)

        def render(self):
            body = self.build_body()
            title = self.build_title()
            if self.user.posts_count is not None and not self.app.hide_metrics:
                subtitle = self.build_subtitle()
            else:
                subtitle = Text()

            return Panel(
                body,
                title=title,
                title_align='left',
                subtitle=subtitle,
                border_style=self.app.theme_variables["foreground"],
                padding=(1, 2),
            )

        def build_body(self):
            """Build panel body text"""
            body = Text()

            if self.user.badges:
                for badge in self.user.badges:
                    color = self.app.theme_variables['text-accent'] if badge['severity'] == 'inform' else self.app.theme_variables['text-error']
                    body.append(f'[{badge['label'].replace('-',' ').title()}] ', style=color)

                body.append('\n\n')

            if self.user.blocking:
                body.append('[User Blocked]', style=self.app.theme_variables["text-error"])
            elif self.user.description is not None:
                body.append(self.user.description)

            return body

        def build_title(self):
            """Build panel title"""
            title = Text()
            if self.user.display_name:
                title.append(self.user.display_name + " ", style="bold")
            title.append(handle_to_link(self.user.handle))
            if self.user.blocking:
                title.append(' 🚫')
            if self.user.muted:
                title.append(' 🔇')
            return title

        def build_subtitle(self):
            """Build panel subtitle"""
            base_color = self.app.theme_variables["foreground"]
            followed_color = f"bold {self.app.theme_variables["text-success"]}"
            following_color = f"bold {self.app.theme_variables["text-accent"]}"

            subtitle = Text()
            subtitle.append(f'{abbrev_num(self.user.followers_count)} followers' + " ", style=base_color if self.user.following is None else followed_color)
            subtitle.append(' | ' + " ")
            subtitle.append(f'{abbrev_num(self.user.follows_count)} following' + " ", style=base_color if self.user.followed_by is None else following_color)
            subtitle.append(' | ' + " ")
            subtitle.append(f'{abbrev_num(self.user.posts_count)} posts')

            return subtitle
