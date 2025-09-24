from typing import Iterable
import pyperclip

from textual.app import ComposeResult, SystemCommand
from textual.widgets import Markdown
from textual.binding import Binding
from textual.widget import Widget

from skyter.bsky import BlueSkyClient
from skyter.data_classes import User
from skyter.utils import get_month_year, abbrev_num
from skyter.user_actions import UserActions


class ProfileView(Widget, UserActions):
    """Panel for showing profile data"""

    BINDINGS = [
        Binding("f", "handle_follow", "Follow"),
        Binding("m", "handle_mute", "Mute"),
        Binding("b", "handle_block", "Block"),
        Binding("F", "show_follows", "Follows"),
        Binding("ctrl+f", "show_followers", "Followers"),
        Binding("l", "show_likes", "Likes"),
        Binding("L", "show_lists", "Lists"),
        Binding("S", "show_starter_packs", "Starter packs"),
    ]

    can_focus = True

    def __init__(self, client: BlueSkyClient, handle: str | None = None, **kwargs):
        self.client = client
        self.handle = handle
        self.user = None
        self.markdown = None
        super().__init__(**kwargs)

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""
        if not self.client.handle == self.handle: # hide user actions on own profile
            yield SystemCommand("Follow", "Follow (or unfollow) user", self.action_handle_follow)
            yield SystemCommand("Mute", "Mute (or unmute) user", self.action_handle_mute)
            yield SystemCommand("Block", "Block (or unblock) user", self.action_handle_block)
        yield SystemCommand("View follows", "Show users that user is following", self.action_show_follows)
        yield SystemCommand("View followers", "Show followers of user", self.action_show_followers)
        yield SystemCommand("View likes", "Show posts liked by user", self.action_show_lists)
        yield SystemCommand("View lists", "Show lists created by user", self.action_show_lists)
        yield SystemCommand("View starter packs", "Show starter packs created by user", self.action_show_starter_packs)
        yield SystemCommand("Copy profile URL", "Copy URL of profile to clipboard", self.action_copy_profile_link)

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Override default method to check if an action should be available."""

        # hide user actions on own profile
        if action in ["handle_follow", "handle_mute", "handle_block"]:
            if getattr(self.client, 'handle', '') == self.handle:
                return False
            else:
                return True

        return True

    async def on_mount(self):
        self.user = await self.get_user_data(self.handle) if self.handle else None

    def _generate_markdown_content(self) -> str:
        """Generate markdown content from user data."""
        if not self.user:
            return ""

        verified = self.user.verification is not None
        has_display_name = self.user.display_name is not None
        has_description = self.user.description is not None
        blocking =  self.user.blocking is not None
        its_me = self.client.handle == self.handle

        if has_display_name:
            content = f"# {self.user.display_name}"
        else:
            content = f"# {self.user.handle}"
        if verified:
            content += ' ✅'
        if blocking:
            content += ' 🚫'
        if self.user.muted:
            content += ' 🔇'
        content += "\n\n"
        if has_display_name:
            content += f"@{self.user.handle}"
        content += "\n\n"

        if self.user.badges:
            content += ', '.join([f"_{badge['label'].replace('-',' ').title()}_" for badge in self.user.badges])
            content += "\n\n"

        if not blocking:

            if has_description:
                content += f"{self._multiline_blockquote(self.user.description)}\n\n"

            if its_me:
                content += "_it's you_\n\n"
            elif self.user.following is not None:
                content += "_following_\n\n"
            else:
                content += "_not following_\n\n"

            if not its_me and self.user.followed_by is not None:
                content += "_follows you_\n\n"

            content += f"- Joined {get_month_year(self.user.created_at)}\n"
            if not self.app.hide_metrics:
                content += f"- Followers: {abbrev_num(self.user.followers_count)} ({abbrev_num(self.user.known_followers_count)} {'known' if not its_me else 'mutual'})\n"
                content += f"- Following: {abbrev_num(self.user.follows_count)}\n"
                content += f"- Posts: {abbrev_num(self.user.posts_count)}\n"

        else:
            content += 'User blocked'

        return content

    @staticmethod
    def _multiline_blockquote(s: str):
        """Convert string to markdown block-quote"""
        return '>' + s.replace('\n','\n>')

    async def action_refresh_panel(self, handle: str | None = None, refresh_data: bool = True):
        """Refresh the panel, optionally setting a new handle."""

        if handle:
            self.handle = handle

        if refresh_data:
            self.user = await self.get_user_data()

        if self.markdown is not None:
            markdown_content = self._generate_markdown_content()
            self.markdown.update(markdown_content)

        self.loading = False

    def compose(self) -> ComposeResult:
        markdown_content = self._generate_markdown_content()
        self.markdown = Markdown(markdown_content)
        yield self.markdown

    async def _get_badges(self, user: dict):
        """Apply non-ignored labels as badges"""

        if self.app.subscribed_labels:
            users = await self.client.label_users([user])
            user = users[0]

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

        return user

    async def get_user_data(self):
        if self.handle:
            self.loading = True
            response = await self.client.get_profile(self.handle)
            if response:
                profile_labeled = await self._get_badges(response)
                return User.from_dict(profile_labeled)
        return None

    def on_focus(self) -> None:
        """Manually add focused class for default non-focusable widget"""
        self.add_class("focused")

    def on_blur(self) -> None:
        """Manually remove focused class for default non-focusable widget"""
        self.remove_class("focused")

    async def action_handle_follow(self):
        """Action to follow/unfollow user"""

        result = await self._user_action_follow(handle=self.handle, following=self.user.following, followers_count=self.user.followers_count)

        if result['success']:
            self.user.following = result['following']
            self.user.followers_count = result['followers_count']
            await self.action_refresh_panel(refresh_data=False)

    async def action_handle_mute(self):
        """Action to mute/unmute user"""

        result = await self._user_action_mute(handle=self.handle, muted=self.user.muted)

        if result['success']:
            self.user.muted = result['muted']
            await self.action_refresh_panel(refresh_data=False)

    async def action_handle_block(self):
        """Action to block/unblock user"""

        result = await self._user_action_block(handle=self.handle, blocking=self.user.blocking, following=self.user.following, followers_count=self.user.followers_count)

        if result['success']:
            self.user.blocking = result['blocking']
            self.user.following = result['following']
            self.user.followers_count = result['followers_count']
            await self.action_refresh_panel(refresh_data=False)

    def action_show_follows(self):
        """Action to show user's follows."""
        self.screen.action_build_follows_list(handle=self.handle)

    def action_show_followers(self):
        """Action to show user's followers."""
        self.screen.action_build_follower_list(handle=self.handle)

    def action_show_likes(self):
        """Action to show user's lists."""
        self.screen.action_build_user_likes(handle=self.handle)

    def action_show_lists(self):
        """Action to show user's lists."""
        self.screen.action_build_user_lists(handle=self.handle)

    def action_show_starter_packs(self):
        """Action to show user's lists."""
        self.screen.action_build_user_starter_packs(handle=self.handle)

    def action_copy_profile_link(self) -> None:
        """Action to copy the URL of the profile."""
        link = self.client.get_profile_url(self.handle)
        self.notify(f"copied profile link to clipboard")
        pyperclip.copy(link)
