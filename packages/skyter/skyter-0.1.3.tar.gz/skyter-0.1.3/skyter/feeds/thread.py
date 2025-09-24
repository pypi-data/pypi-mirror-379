from textual.widgets import ListView
from textual.binding import Binding
from textual import events

from skyter.feeds.posts import PostFeedView


class ThreadFeedView(PostFeedView):
    """Override certain PostFeedView methods and change keybindings for thread view."""

    BINDINGS = [
        Binding("enter", "view_thread", "Thread"),
        Binding("l", "handle_like", "Like"),
        Binding("p", "view_profile", "Profile"),
        Binding("f", "handle_follow", "Follow"),
        Binding("r", "handle_repost", "Repost"),
        Binding("ctrl+r", "reply", "Reply"),
        Binding("L", "view_likes", "Likes"),
        Binding("R", "view_reposts", "Reposts"),
        Binding("Q", "view_quotes", "Quotes"),
    ]

    def _unpack_replies(self, post: dict, level1: bool = True) -> list[dict]:
        """Recursively add replies to list of posts."""
        result = []
        for reply in post['thread_replies']:
            if level1:
                if len(reply['thread_replies']) == 0:
                    pass
                else:
                    reply['reply_position'] = 'root'
            else:
                if len(reply['thread_replies']) == 0:
                    reply['reply_position'] = 'node'
                else:
                    reply['reply_position'] = 'parent'
            result.append(reply)
            result.extend(self._unpack_replies(reply, level1=False))
        return result

    def _unpack_thread(self, main) -> list[dict]:
        """Unpack thread parent posts and replies and set reply positions"""
        replies = self._unpack_replies(main)
        parents = main['thread_parents']
        if len(parents) > 0:
            for i, parent in enumerate(parents):
                if i == 0:
                    parent['reply_position'] = 'root'
                else:
                    parent['reply_position'] = 'parent'
            main['reply_position'] = 'node'
        main['thread_main_post'] = True
        self.main_index = len(parents)
        return parents + [main] + replies

    async def generate_data(self, new_items: bool = False, reset_pagination: bool = False):
        """Make client calls to retrieve data for building feed."""

        thread = await self.client.get_thread(uri=self.source.target, limit=self.app.page_limit)

        if thread is None:
            self.app.notify("No results found", severity="warning")
            return []

        # Unpack thread after generating data
        thread = self._unpack_thread(thread)

        # Hide / add warnings for labeled content
        thread = await self._apply_content_policies(thread)

        return thread

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Override parent action to fetch more data on last index for feeds without pagination."""
        event.prevent_default()
        event.stop()

    def _scroll_to_main(self):
        self.index = self.main_index
        self.scroll_to_widget(self.query(ThreadFeedView.Listed)[self.main_index], animate=False, top=True)

    async def on_mount(self, event: events.Mount):
        """Override parent method and scroll to main post"""
        if not self.mount_empty:
            await self.more_items()
            self._scroll_to_main()
        event.prevent_default()
        event.stop()

    async def refresh_items(self):
        """Override parent method and scroll to main post"""
        self.loading = True
        self.clear()
        self.feed_data = []
        self._debounce = False
        await self.more_items()
        self.refresh_bindings()
        self._scroll_to_main()
