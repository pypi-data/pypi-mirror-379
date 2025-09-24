from textual.app import ComposeResult
from textual.widgets import Header
from textual.containers import Container

from skyter.bsky import BlueSkyClient
from skyter.data_classes import FeedSource
from skyter.feeds.posts import PostFeedView
from skyter.feeds.users import UserFeedView
from skyter.feeds.notifications import NotificationFeedView
from skyter.feeds.thread import ThreadFeedView
from skyter.feeds.custom_feeds import CustomFeedView
from skyter.feeds.starter_packs import StarterPackFeedView


class FeedViewContainer(Container):
    """Container for remounting different FeedView types"""

    FV_CLASS_REGISTRY = {
        'PostFeedView': PostFeedView,
        'UserFeedView': UserFeedView,
        'NotificationFeedView': NotificationFeedView,
        'ThreadFeedView': ThreadFeedView,
        'CustomFeedView': CustomFeedView,
        'StarterPackFeedView': StarterPackFeedView,
    }

    def __init__(self, client: BlueSkyClient, source: FeedSource, **kwargs):
        self.client = client
        self.source = source
        self.current_feed = self.source.feedview_type()
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        if self.current_feed in self.FV_CLASS_REGISTRY:
            feedview_class = self.FV_CLASS_REGISTRY[self.current_feed]
            yield feedview_class(client=self.client, source=self.source, id="the-feed")
        yield Header()


    async def change_feed(self, source: FeedSource) -> None:
        """Handle feed switching"""

        change_to = source.feedview_type()

        if change_to == self.current_feed: return

        self.loading = True
        self.source = source
        self.current_feed = change_to

        feed_instance = self.query_one("#the-feed")
        await feed_instance.remove()

        if self.current_feed in self.FV_CLASS_REGISTRY:
            feedview_class = self.FV_CLASS_REGISTRY[self.current_feed]
            new_feed = feedview_class(client=self.client, source=self.source, id="the-feed")
        else:
            return

        await self.mount(new_feed)
        self.loading = False
        new_feed.focus()

    async def reload_feed(self, state: dict) -> None:
        """Switch feed using stored feed state"""

        change_to = state['source'].feedview_type()

        if change_to == self.current_feed: return

        self.loading = True
        self.source = state['source']
        self.current_feed = change_to

        feed_instance = self.query_one("#the-feed")
        await feed_instance.remove()

        if self.current_feed in self.FV_CLASS_REGISTRY:
            feedview_class = self.FV_CLASS_REGISTRY[self.current_feed]
            new_feed = feedview_class(client=self.client, source=self.source, mount_empty=True, id="the-feed")

        else:
            return

        await self.mount(new_feed)
        self.loading = False
        await new_feed.refresh_from_data(
            feed_data=state['data'],
            paginator=state['paginator'],
            idx=state['idx'],
        )
        new_feed.focus()
