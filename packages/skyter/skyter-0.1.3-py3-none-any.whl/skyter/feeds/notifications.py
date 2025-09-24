from typing import Iterable

from textual.app import ComposeResult, SystemCommand
from textual.widgets import ListView
from textual.binding import Binding
from rich.text import Text
from rich.panel import Panel

from skyter.utils import format_time, abbrev_num, handle_to_link
from skyter.data_classes import Post, Notification
from skyter.user_actions import UserActions
from skyter.feeds.feed import FeedView, FeedPanel


class NotificationFeedView(FeedView, UserActions):
    """FeedView for custom feed-based feeds (i.e., feed search results, suggested feeds)"""

    BINDINGS = [
        Binding("p", "view_profile", "Profile"),
        Binding("f", "handle_follow", "Follow"),
        Binding("m", "handle_mute_profile", "Mute"),
        Binding("b", "handle_block", "Block"),
        Binding(">", "view_mentions", "Mentions"),
        Binding(">", "view_notifications", "All notifications"),
    ]

    async def create_list_items(self, items: list[dict]) -> list[FeedView.Listed]:
        """Create Listed objects from list of dictionaries"""
        return [self.Listed(Notification.from_dict(item)) for item in items if item is not None]

    async def generate_data(self, new_items: bool = False, reset_pagination: bool = False):
        """Make client calls to retrieve data for building feed."""

        items = await self.client.get_notifications(
            reasons=self.source.params['reasons'] if 'reasons' in self.source.params else [],
            limit=self.app.page_limit,
            new_items=new_items,
            reset_pagination=reset_pagination
        )

        # once notifications are retrieved, mark all as read
        read_result = await self.client.read_notifications()
        if not read_result:
            self.app.notify("Error reading notifications", severity="error")

        if items is None:
            return []

        if len(items) == 0 and not new_items:
            if len(self.feed_data) == 0:
                self.app.notify("No results found", severity="warning")
            else:
                self.app.notify("No more results", severity="warning")

        return items

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Override default method to check if an action should be available."""

        # set notification type switch action
        if action == "view_mentions" and ('title' in self.source.params and self.source.params['title'] == 'Mentions'):
            return False
        elif action == "view_notifications" and ('title' not in self.source.params or self.source.params['title'] == 'Notifications'):
            return False

        return True

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        highlighted = self._get_highlighted(suppress_notification=True)
        if highlighted:
            yield SystemCommand("Profile", "Open profile for the highlighted notification", self.action_view_profile)
            yield SystemCommand("Follow", "Follow (or unfollow) profile for the highlighted notification", self.action_handle_follow)
            yield SystemCommand("Mute account", "Mute (or unmute) highlighted notification user", self.action_handle_mute_profile)
            yield SystemCommand("Block account", "Block (or unblock) highlighted notification user", self.action_handle_block)
        yield from super().offer_widget_commands()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Mark unread notifications as read when highlighted"""
        # super called automatically
        highlighted = self._get_highlighted(suppress_notification=True)
        if highlighted is not None and not highlighted.notification.is_read:
            highlighted.notification.is_read = True

    def action_view_profile(self) -> None:
        """Request the app to build user feed for highlighted user"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.notification.handle
            self.screen.action_build_user_feed(handle)

    async def action_handle_follow(self) -> None:
        """Action to follow the profile of the highlighted notification."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_follow(handle=highlighted.notification.handle, following=highlighted.notification.following)
            if result['success']:
                highlighted.notification.following = result['following']
                highlighted.refresh()

    async def action_handle_mute_profile(self) -> None:
        """Action to mute the profile of the highlighted notification."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_mute(handle=highlighted.notification.handle, muted=highlighted.notification.muted)
            if result['success']:
                highlighted.notification.muted = result['muted']
                highlighted.refresh()

    async def action_handle_block(self) -> None:
        """Action to block the profile of the highlighted notification."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_block(handle=highlighted.notification.handle, blocking=highlighted.notification.blocking, following=highlighted.notification.following)
            if result['success']:
                self.app.notify(str(result['blocking']))
                highlighted.notification.blocking = result['blocking']
                highlighted.notification.following = result['following']
                highlighted.refresh()

    def action_view_mentions(self) -> None:
        """Action to show mentions / all notifications."""
        self.loading = True
        self.screen.action_build_mentions()

    def action_view_notifications(self) -> None:
        """Action to show all notifications."""
        self.loading = True
        self.screen.action_build_notifications()

    class Listed(FeedView.Listed):
        """Custom ListItem container to list UserPanel objects in UserFeedView"""

        def compose(self) -> ComposeResult:
            """Determine FeedPanel class based on notification type"""
            reason = self.data_obj.reason
            if reason == 'follow':
                yield NotificationFeedView.FollowNotificationPanel(self.data_obj)
            elif reason in ['like', 'repost']:
                yield NotificationFeedView.PostInteractionNotificationPanel(self.data_obj)
            elif reason in ['reply', 'mention', 'quote']:
                yield NotificationFeedView.MentionNotificationPanel(self.data_obj)
            else:
                yield NotificationFeedView.NotificationPanel(self.data_obj)


    class NotificationPanel(FeedPanel):
        """Feed panel for rendering notification information. Title, subtitle and body methods should be overridden by child classes."""

        def __init__(self, notification: Notification, **kwargs):
            self.notification = notification
            super().__init__(**kwargs)

        def render(self):
            title = self.build_title()
            body = self.build_body()
            subtitle = self.build_subtitle() if not self.app.hide_metrics else ''
            border_style = self.app.theme_variables["foreground"] if self.notification.is_read else self.app.theme_variables["accent"]
            return Panel(
                body,
                title=title,
                title_align="left",
                subtitle=subtitle,
                border_style=border_style,
                padding=(1, 2),
            )

        def build_title(self):
            """Build panel title"""
            base_color = self.app.theme_variables["foreground"]
            title = Text()
            if self.notification.display_name:
                title.append(self.notification.display_name + " ", style=f"bold {base_color}")
            title.append(handle_to_link(self.notification.handle))
            title.append(' {self.notification.reason}', style=base_color)
            title.append(" · " + format_time(timestamp=self.notification.created_at, relative=self.app.relative_dates), style=base_color)
            if self.notification.blocking:
                title.append(' 🚫')
            if self.notification.muted:
                title.append(' 🔇')
            return title

        def build_body(self):
            return Text('')

        def build_subtitle(self):
            return Text('')


    class FollowNotificationPanel(NotificationPanel):
        """Feed panel for rendering follow notification information"""

        def build_title(self):
            """Build panel title"""
            base_color = self.app.theme_variables["foreground"]
            title = Text('👥  ')
            if self.notification.display_name:
                title.append(self.notification.display_name + " ", style=f"bold {base_color}")
            title.append(handle_to_link(self.notification.handle))
            title.append(' followed you', style=base_color)
            title.append(" · " + format_time(timestamp=self.notification.created_at, relative=self.app.relative_dates), style=base_color)
            if self.notification.blocking:
                title.append(' 🚫')
            if self.notification.muted:
                title.append(' 🔇')
            return title

        def build_subtitle(self):
            """Build panel subtitle"""
            base_color = self.app.theme_variables["foreground"]
            followed_color = f"bold {self.app.theme_variables["text-success"]}"
            following_color = f"bold {self.app.theme_variables["text-accent"]}"

            subtitle = Text()
            subtitle.append(f'{abbrev_num(self.notification.subject['followers_count'])} followers' + " ", style=base_color if self.notification.following is None else followed_color)
            subtitle.append(' | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(self.notification.subject['follows_count'])} following' + " ", style=base_color if self.notification.followed_by is None else following_color)
            subtitle.append(' | ' + " ", style=base_color)

            subtitle.append(f'{abbrev_num(self.notification.subject['posts_count'])} posts', style=base_color)

            return subtitle

        def build_body(self):
            """Build panel content"""
            if self.notification.blocking:
                return Text('[User Blocked]', style=self.app.theme_variables["text-error"])
            elif self.notification.description is not None:
                return Text(self.notification.description)
            else:
                return Text('')


    class PostInteractionNotificationPanel(NotificationPanel):
        """Feed panel for rendering like and repost notification information"""

        def build_title(self):
            """Build panel title"""
            base_color = self.app.theme_variables["foreground"]
            title = Text()
            if self.notification.reason == 'like':
                title.append('♥️  ')
            elif self.notification.reason == 'repost':
                title.append('🔄  ')
            if self.notification.display_name:
                title.append(self.notification.display_name + " ", style=f"bold {base_color}")
            title.append(handle_to_link(self.notification.handle))
            if self.notification.reason == 'like':
                title.append(' liked your post', style=base_color)
            elif self.notification.reason == 'repost':
                title.append(' reposted your post', style=base_color)
            title.append(" · " + format_time(timestamp=self.notification.created_at, relative=self.app.relative_dates), style=base_color)
            if self.notification.blocking:
                title.append(' 🚫')
            if self.notification.muted:
                title.append(' 🔇')
            return title

        def build_subtitle(self):
            """Build panel subtitle"""
            base_color = self.app.theme_variables["foreground"]
            liked_color = f"bold {self.app.theme_variables["text-error"]}"
            reposted_color = f"bold {self.app.theme_variables["text-success"]}"

            subj = Post.from_dict(self.notification.subject)

            subtitle = Text()
            subtitle.append(f'{abbrev_num(subj.reply_count)} replies | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(subj.repost_count)} reposts' + " ", style=base_color if subj.reposted is None else reposted_color)
            subtitle.append(' | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(subj.quote_count)} quotes | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(subj.like_count)} likes', style=base_color if subj.liked is None else liked_color)
            return subtitle

        def build_body(self):
            """Build panel content"""
            if self.notification.subject['text'] is not None:
                return Text(self.notification.subject['text'])
            else:
                return Text('')

    class MentionNotificationPanel(NotificationPanel):
        """Feed panel for rendering reply notification information"""

        def build_title(self):
            """Build panel title"""
            base_color = self.app.theme_variables["foreground"]
            title = Text()
            if self.notification.reason == 'reply':
                title.append('↩️  ')
            elif self.notification.reason == 'mention':
                title.append('🏷️  ')
            elif self.notification.reason == 'quote':
                title.append('💬  ')
            if self.notification.display_name:
                title.append(self.notification.display_name + " ", style=f"bold {base_color}")
            title.append(handle_to_link(self.notification.handle))
            if self.notification.reason == 'reply':
                title.append(' replied to your post', style=base_color)
            elif self.notification.reason == 'mention':
                title.append(' mentioned you', style=base_color)
            elif self.notification.reason == 'quote':
                title.append(' quoted your post', style=base_color)
            title.append(" · " + format_time(timestamp=self.notification.created_at, relative=self.app.relative_dates), style=base_color)
            if self.notification.blocking:
                title.append(' 🚫')
            if self.notification.muted:
                title.append(' 🔇')
            return title

        def build_subtitle(self):
            """Build panel subtitle"""
            base_color = self.app.theme_variables["foreground"]
            liked_color = f"bold {self.app.theme_variables["text-error"]}"
            reposted_color = f"bold {self.app.theme_variables["text-success"]}"

            record = Post.from_dict(self.notification.record)

            subtitle = Text()
            subtitle.append(f'{abbrev_num(record.reply_count)} replies | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(record.repost_count)} reposts' + " ", style=base_color if record.reposted is None else reposted_color)
            subtitle.append(' | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(record.quote_count)} quotes | ' + " ", style=base_color)
            subtitle.append(f'{abbrev_num(record.like_count)} likes', style=base_color if record.liked is None else liked_color)
            return subtitle

        def build_body(self):
            """Build panel content"""
            if self.notification.blocking:
                return Text('[User Blocked]', style=self.app.theme_variables["text-error"])
            elif self.notification.record['text'] is not None:
                return Text(self.notification.record['text'])
            else:
                return Text('')
