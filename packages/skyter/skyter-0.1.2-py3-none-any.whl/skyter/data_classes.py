from typing import Any
from dataclasses import dataclass, field

from skyter.utils import remove_bidi_controls


@dataclass
class FeedSource:
    """Data class for defining FeedView object source. Used to determine FeedView class, widget title, library methods to use."""
    target: str | None = None
    feed_type: str = "timeline"
    params: dict[str, Any] = field(default_factory=dict)

    def feedview_type(self):
        """Return FeedView class to be used based on feed type and parameters"""
        if self.feed_type == "search":
            if self.params['search_type'] == 'users':
                return "UserFeedView"
            elif self.params['search_type'] == 'feeds':
                return "CustomFeedView"
            else:
                return "PostFeedView"
        elif self.feed_type in ["follows", "followers", "mutes", "blocks", "likes", "reposts", "list_people"]:
            return "UserFeedView"
        elif self.feed_type == "notifications":
            return "NotificationFeedView"
        elif self.feed_type in ["saved_feeds", "user_lists"]:
            return "CustomFeedView"
        elif self.feed_type == "thread":
            return "ThreadFeedView"
        elif "starter_packs" in self.feed_type:
            return "StarterPackFeedView"
        return "PostFeedView"

    def feedview_title(self):
        """Return widget title based on feedview type and target"""
        if self.feed_type == 'timeline':
            return "Following timeline"
        elif self.feed_type == "user":
            return self.params['title'] if 'title' in self.params else f'@{self.target}\'s posts'
        elif self.feed_type in ["custom_feed", "list_feed"]:
            return f'{self.params.get("title") or "Custom"} feed'
        elif self.feed_type in ['follows', 'followers', 'user_lists', 'user_starter_packs', 'user_likes']:
            return f'{"@" + self.target + "'s" if self.target else 'My'} {self.feed_type.replace('user_', '').replace('_', ' ')}'
        elif self.feed_type == "search":
            if self.params['search_type'] == 'feeds' and self.target is None:
                return "Suggested Feeds"
            return f'Search results for "{self.target}"'
        elif self.feed_type == "notifications":
            return self.params.get('title') or 'Notifications'
        elif self.feed_type == "mutes":
            return "My Mute List"
        elif self.feed_type == "blocks":
            return "My Block List"
        elif self.feed_type == "saved_feeds":
            return "Saved Feeds"
        elif self.feed_type == "thread":
            return f'Thread for @{self.params["handle"]}\'s post{": \"" +self.params["text"] + "\"" if self.params["text"] else ""}'
        elif self.feed_type == "likes":
            return f'Likers of @{self.params["handle"]}\'s post{": \"" +self.params["text"] + "\"" if self.params["text"] else ""}'
        elif self.feed_type == "reposts":
            return f'Reposters of @{self.params["handle"]}\'s post{": \"" +self.params["text"] + "\"" if self.params["text"] else ""}'
        elif self.feed_type == "quotes":
            return f'Quotes of @{self.params["handle"]}\'s post{": \"" +self.params["text"] + "\"" if self.params["text"] else ""}'
        elif self.feed_type == 'list_people':
            return f'Users in list "{self.params.get("title") or ''}"'
        else:
            return ''

@dataclass
class Post:
    """Data class for listed items in PostFeedView."""
    uri: str
    cid: str
    display_name: str
    handle: str
    muted: bool
    blocked_by: bool
    post_content: str
    created_at: str
    reply_count: int = 0
    repost_count: int = 0
    quote_count: int = 0
    like_count: int = 0
    liked: str | None = None
    reposted: str | None = None # logged in user repost record
    media: dict | None = None
    reply_position: str | None = None # root, parent, node or None if not part of reply thread
    thread_main_post: bool = False
    reason: str | None = None
    repost: dict | None = None # reason repost, i.e., another user has reposted
    following: str | None = None
    followed_by: str | None = None
    blocking: str | None = None
    author_labels: list = field(default_factory=list)
    labels: list = field(default_factory=list)
    content_blur: list = field(default_factory=list)
    media_blur: list = field(default_factory=list)
    information_labels: list = field(default_factory=list)
    blurred: bool = False

    @classmethod
    def from_dict(cls, d: dict) -> "Post":
        """Create data class object from dictionary"""
        # create Posts for quoted posts
        media = d['media'].copy() if 'media' in d else None
        if media and 'quote_posts' in media and len(media['quote_posts']) > 0:
            media['quote_posts'] = [MissingPost.from_dict(q) if q.get("is_deleted_post") or q.get("is_blocked_post") else Post.from_dict(q) for q in media['quote_posts']]

        return Post(
            uri = d['uri'],
            cid = d['cid'],
            display_name = remove_bidi_controls(d['author']['display_name']),
            handle = d['author']['handle'],
            muted = d['author']['muted'],
            blocked_by = d['author']['blocked_by'],
            post_content = remove_bidi_controls(d['text']),
            created_at = d['created_at'],
            reply_count = d['reply_count'],
            repost_count = d['repost_count'],
            quote_count = d['quote_count'],
            like_count = d['like_count'],
            liked = d['viewer']['like'] if 'viewer' in d else None,
            reposted = d['viewer']['repost'] if 'viewer' in d else None,
            media = media,
            reply_position = d['reply_position'] if 'reply_position' in d else None,
            thread_main_post = d['thread_main_post'] if 'thread_main_post' in d else None,
            reason = d['reason'] if 'reason' in d else None,
            repost = {k:remove_bidi_controls(v) if k == 'display_name' else v for k,v in d['repost'].items()} if 'repost' in d else None,
            following = d['author']['following'],
            followed_by = d['author']['followed_by'],
            blocking = d['author']['blocking'],
            author_labels = d['author']['labels'],
            labels = d['labels'],
            content_blur = d['warn_labels']['content'] if 'warn_labels' in d else [],
            media_blur = d['warn_labels']['media'] if 'warn_labels' in d else [],
            information_labels = d['warn_labels']['none'] if 'warn_labels' in d else [],
            blurred = d['blurred'] if 'blurred' in d else False,
        )

    def has_external_link(self):
        """Check whether the post has an embedded external link"""
        if not self.media:
            return False
        if len(self.media['external_links']) == 0:
            return False
        else:
            return True

    def has_images(self):
        """Check whether the post has embedded images"""
        if not self.media:
            return False
        if len(self.media['images']) == 0:
            return False
        else:
            return True

    def has_video(self):
        """Check whether the post has an embedded video"""
        if not self.media:
            return False
        if len(self.media['videos']) == 0:
            return False
        else:
            return True

    def has_quote(self):
        """Check whether the post has an embedded quote"""
        if not self.media:
            return False
        if len(self.media['quote_posts']) == 0:
            return False
        else:
            return True

    def has_starter_pack(self):
        """Check whether the post has an embedded starter pack"""
        if not self.media:
            return False
        if len(self.media['starter_packs']) == 0:
            return False
        else:
            return True

    def has_list(self):
        """Check whether the post has an embedded list"""
        if not self.media:
            return False
        if len(self.media['lists']) == 0:
            return False
        else:
            return True

    def has_feed(self):
        """Check whether the post has an embedded feed"""
        if not self.media:
            return False
        if len(self.media['feeds']) == 0:
            return False
        else:
            return True

@dataclass
class MissingPost:
    """Data class for blocked/deleted posts in PostFeedView"""
    uri: str
    is_deleted: bool
    reply_position: str | None

    @classmethod
    def from_dict(cls, d: dict) -> "MissingPost":
        """Create data class object from dictionary"""
        return MissingPost(
            uri = d['uri'],
            is_deleted = d['is_deleted_post'] if 'is_deleted_post' in d else False,
            reply_position = d['reply_position'] if 'reply_position' in d else None,
        )

@dataclass
class ThreadContext:
    """Data class representing gap between parent and root replies in PostFeedView"""
    uri: str
    handle: str
    post_content: str | None

    @classmethod
    def from_dict(cls, d: dict) -> "ThreadContext":
        """Create data class object from dictionary"""
        return ThreadContext(
            uri = d['uri'],
            handle = d['handle'],
            post_content = remove_bidi_controls(d['text']),
        )

@dataclass
class User:
    """Data class for ProfileView and listed items in UserFeedView."""
    did: str
    handle: str
    display_name: str | None
    description: str | None
    avatar: str
    banner: str | None
    created_at: str
    following: str | None
    followers_count: int | None
    known_followers_count: int | None
    follows_count: int | None
    posts_count: int | None
    followed_by: str | None
    muted: bool
    mute_list: str | None
    blocking: str | None
    blocking_by_list: str | None
    blocked_by: bool
    verification: Any | None
    labels: list
    badges: list | None

    @classmethod
    def from_dict(cls, d: dict) -> "User":
        """Create data class object from dictionary"""
        return User(
            did=d['did'],
            handle=d['handle'],
            display_name=remove_bidi_controls(d['display_name']) if 'display_name' in d else None,
            description=remove_bidi_controls(d['description']) if 'description' in d else None,
            avatar=d['avatar'],
            banner=d['banner'] if 'banner' in d else None,
            created_at=d['created_at'],
            following=d['following'],
            followers_count=d['followers_count'] if 'followers_count' in d else None,
            known_followers_count=d['known_followers_count'] if 'known_followers_count' in d else None,
            follows_count=d['follows_count'] if 'follows_count' in d else None,
            posts_count=d['posts_count'] if 'posts_count' in d else None,
            followed_by=d['followed_by'],
            muted=d['muted'],
            mute_list=d['mute_list'],
            blocking=d['blocking'],
            blocking_by_list=d['blocking_by_list'],
            blocked_by=d['blocked_by'],
            verification=d['verification'] if 'verification' in d else None,
            labels=d['labels'] if 'labels' in d else [],
            badges=d['badges'] if 'badges' in d else [],
        )

@dataclass
class CustomFeed:
    """Data class for listed items in CustomFeedView."""
    uri: str | None
    item_type: str
    cid: str | None
    display_name: str
    avatar: str | None
    description: str | None
    like_count: int | None
    item_count: int | None
    liked: str | None
    pinned: bool | None
    creator: dict | None

    @classmethod
    def from_dict(cls, d: dict) -> "CustomFeed":
        """Create data class object from dictionary"""
        return CustomFeed(
            uri=d['uri'] if 'uri' in d else None,
            item_type=d['type'] if 'type' in d else 'feed',
            cid=d['cid'] if 'cid' in d else None,
            display_name=remove_bidi_controls(d['display_name']),
            avatar=d['avatar'] if 'avatar' in d else None,
            description=remove_bidi_controls(d['description']) if 'description' in d else None,
            like_count=d['like_count'] if 'like_count' in d else None,
            item_count=d['item_count'] if 'item_count' in d else None,
            liked=d['liked'] if 'liked' in d else None,
            pinned=d['pinned'] if 'pinned' in d else None,
            creator=d['creator'] if 'creator' in d else None,
        )

@dataclass
class StarterPack:
    """Data class for listed items in StarterPackFeedView."""
    uri: str
    cid: str
    list_uri: str
    display_name: str
    description: str | None
    joined_count: int
    creator: dict

    @classmethod
    def from_dict(cls, d: dict) -> "StarterPack":
        """Create data class object from dictionary"""
        return StarterPack(
            uri=d['uri'],
            cid=d['cid'],
            list_uri=d['list_uri'],
            display_name=remove_bidi_controls(d['display_name']),
            description=remove_bidi_controls(d['description']),
            joined_count=d['joined_count'],
            creator=d['creator'],
        )

@dataclass
class Notification:
    """Data class for listed items in NotificationFeedView."""
    uri: str
    cid: str
    reason: str
    reason_subject: str
    subject: dict | None
    record: dict | None
    handle: str
    display_name: str | None
    description: str | None
    is_read: bool
    created_at: str
    following: str | None
    followed_by: str | None
    muted: bool
    blocking: str | None
    blocked_by: bool

    @classmethod
    def from_dict(self, d: dict):
        """Create data class object from dictionary"""
        return Notification(
            uri=d['uri'],
            cid=d['cid'],
            reason=d['reason'],
            reason_subject=d['reason_subject'],
            subject=d['subject'],
            record=d['record'],
            handle=d['user']['handle'],
            display_name=remove_bidi_controls(d['user']['display_name']),
            description=remove_bidi_controls(d['user']['description']),
            is_read=d['is_read'],
            created_at=d['created_at'],
            following=d['user']['following'],
            followed_by=d['user']['followed_by'],
            muted=d['user']['muted'],
            blocking=d['user']['blocking'],
            blocked_by=d['user']['blocked_by'],
        )
