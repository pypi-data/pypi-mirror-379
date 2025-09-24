from typing import Iterable
import pyperclip
import subprocess
import webbrowser

from textual.app import ComposeResult, SystemCommand
from textual.binding import Binding
from textual.widget import Widget
from textual import work
from rich.text import Text
from rich.panel import Panel
from rich.console import Group
from rich import box

from skyter.utils import format_time, abbrev_num, handle_to_link, extract_tags_and_handles
from skyter.data_classes import Post, MissingPost, ThreadContext, StarterPack, CustomFeed
from skyter.ui import ROOT_REPLY_BOX, PARENT_REPLY_BOX, REPLY_BOX, THREAD_CONTEXT_BOX, SplitTitlePanel
from skyter.user_actions import UserActions
from skyter.feeds.feed import FeedView, FeedPanel
from skyter.feeds.starter_packs import StarterPackPanel
from skyter.feeds.custom_feeds import CustomFeedPanel


class PostFeedView(FeedView, UserActions):
    """FeedView for post-based feeds."""

    BINDINGS = [
        Binding("enter", "view_thread", "Thread"),
        Binding("l", "handle_like", "Like"),
        Binding("p", "view_profile", "Profile"),
        Binding("f", "handle_follow", "Follow"),
        Binding("r", "handle_repost", "Repost"),
        Binding("o", "open_embedded", "Open embedded"),
        Binding(">", "view_user_posts", "Posts"),       # active on user replies feeds
        Binding(">", "view_user_replies", "Replies"),   # active on user posts feeds
    ]

    async def create_list_items(self, items: list[dict]) -> list[FeedView.Listed]:
        """Create Listed objects from list of dictionaries"""
        list_items = []
        for item in items:
            if item.get('is_deleted_post') or item.get('is_blocked_post'):
                list_items.append(self.Listed(MissingPost.from_dict(item)))
            elif item.get('is_context'):
                list_items.append(self.Listed(ThreadContext.from_dict(item)))
            elif item is not None:
                list_items.append(self.Listed(Post.from_dict(item)))
        return list_items

    def _unpack_reply_parents(self, posts: list[dict]) -> list[dict]:
        """Add reply parents to list of posts."""

        result = []
        reply_parent_uris = set()
        for post in posts:
            if post is None:
                continue

            # avoid duplicating posts if reply parent already in feed, unless viewing liked posts
            if post['uri'] in reply_parent_uris and not self.source.feed_type == 'user_likes':
                continue

            if 'reply_parent' in post and post['reply_parent'] is not None:

                post['reply_position'] = 'node'

                rp = post['reply_parent']

                if rp['root']:
                    # ignore intermediate thread posts in user posts_and_author_threads feed
                    if rp['root']['uri'] in reply_parent_uris and self.source.feed_type == 'user' and (self.source.params.get('post_type') is None or self.source.params['post_type'] == 'posts_and_author_threads'):
                        continue
                    rp['root']['reply_position'] = 'root'
                    result.append(rp['root'])
                    reply_parent_uris.add(rp['root']['uri'])

                if rp['parent']:
                    if rp['root']:
                        # don't add re-add parent if root is parent
                        if rp['parent']['uri'] != rp['root']['uri']:

                            # if root is not grandparent, add thread context item

                            if rp['intermediate_posts']:

                                if not rp['root'].get('is_deleted_post'):
                                    thread_context_ref = rp['root']
                                else:
                                    thread_context_ref = rp['parent']

                                result.append({
                                    'uri': thread_context_ref['uri'],
                                    'handle': thread_context_ref['author']['handle'],
                                    'text': thread_context_ref['text'],
                                    'is_context': True
                                })

                            rp['parent']['reply_position'] = 'parent'
                            result.append(rp['parent'])
                            reply_parent_uris.add(rp['parent']['uri'])
                    else:
                        rp['parent']['reply_position'] = 'parent'
                        result.append(rp['parent'])
                        reply_parent_uris.add(rp['parent']['uri'])

            result.append(post)

        return result

    async def _apply_content_policies(self, posts: list[dict]) -> list[dict]:
        """Filter posts that have hide visibility label; attach policies for posts that have warn visibility label."""

        if self.app.subscribed_labels:
            posts = await self.client.label_posts(posts)

        result = []
        for i, post in enumerate(posts):
            labels = post.get('labels') or []
            author_labels = post['author'].get('labels') or [] if 'author' in post else []
            hide = False
            warn_labels = {
                'content': [],
                'media': [],
                'none': [],
            }
            for label in labels + author_labels:
                if label['label'] not in self.app.content_policies:
                    continue
                policy = self.app.content_policies[label['label']]

                if policy['visibility'] == 'hide':
                    hide = True

                elif policy['visibility'] == 'warn':
                    warn_label = {
                        'label': label['label'],
                        'labeler': label['labeler'],
                        'severity': policy['severity'],
                    }
                    warn_labels[policy['blurs']].append(warn_label)

            if not hide:
                post['warn_labels'] = warn_labels
                if warn_labels['media'] or warn_labels['content'] and i != getattr(self, 'main_index', -1):
                    post['blurred'] = True

                qps = post['media'].get('quote_posts') if 'media' in post else None
                if qps:
                    post['media']['quote_posts'] = await self._apply_content_policies(qps)

                result.append(post)

        return result

    async def generate_data(self, new_items: bool = False, reset_pagination: bool = False):
        """Make client calls to retrieve data for building feed."""

        match self.source.feed_type:

            case 'timeline':
                items = await self.client.get_timeline(limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'search':
                top_posts = self.source.params['search_type'] == 'top'
                items = await self.client.search_posts(
                    query=self.source.target,
                    limit=self.app.page_limit,
                    top_posts=top_posts,
                    since=self.source.params['since'],
                    until=self.source.params['until'],
                    language=self.app.search_language,
                    new_items=new_items,
                    reset_pagination=reset_pagination,
                )

            case 'user':
                items = await self.client.get_user_posts(
                    handle=self.source.target,
                    post_type=self.source.params['post_type'] if 'post_type' in self.source.params else 'posts_and_author_threads',
                    limit=self.app.page_limit,
                    new_items=new_items,
                    reset_pagination=reset_pagination
                )

            case 'user_likes':
                items = await self.client.get_user_likes(handle=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'quotes':
                items = await self.client.get_quotes(uri=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'custom_feed':
                items = await self.client.get_feed(uri=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

            case 'list_feed':
                items = await self.client.get_list_feed(uri=self.source.target, limit=self.app.page_limit, new_items=new_items, reset_pagination=reset_pagination)

        if items is None: # e.g., when user profile is blocked
            return []

        if len(items) == 0 and not new_items:
            if len(self.feed_data) == 0:
                self.app.notify("No results found", severity="warning")
            else:
                self.app.notify("No more results", severity="warning")

        # Unpack parents after generating data
        items = self._unpack_reply_parents(items)

        # Hide / add warnings for labeled content
        items = await self._apply_content_policies(items)

        return items

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Override default method to check if an action should be available."""

        # set post type switch action if user feed
        if action == "view_user_replies" and (self.source.feed_type != 'user' or ('post_type' in self.source.params and self.source.params['post_type'] == 'posts_with_replies')):
            return False
        elif action == "view_user_posts" and (self.source.feed_type != 'user' or 'post_type' not in self.source.params or self.source.params['post_type'] == 'posts_and_author_threads'):
            return False

        return True

    def offer_widget_commands(self) -> Iterable[SystemCommand]:
        """Add actions to the app's command palette."""

        highlighted = self._get_highlighted(suppress_notification=True)
        if highlighted:
            yield SystemCommand("View thread", "View thread for highlighted post", self.action_view_thread)
            yield SystemCommand("Like", "Like (or unlike) highlighted post", self.action_handle_like)
            yield SystemCommand("Repost", "Repost highlighted post (or undo repost)", self.action_handle_repost)
            yield SystemCommand("Reply", "Reply to highlighted post", self.action_reply)
            yield SystemCommand("Quote", "Quote highlighted post", self.action_quote)
            yield SystemCommand("Profile", "Open profile of highlighted post author", self.action_view_profile)
            if highlighted.post.handle == self.client.handle:
                yield SystemCommand("Delete", "Delete highlighted post", self.action_delete)
            yield SystemCommand("View likes", "View likes of highlighted posts", self.action_view_likes)
            yield SystemCommand("View reposts", "View reposts of highlighted posts", self.action_view_reposts)
            yield SystemCommand("View quotes", "View quotes of highlighted posts", self.action_view_quotes)
            yield SystemCommand("View quoted post", "View thread of quoted post", self.action_view_quoted)
            yield SystemCommand("View follows", "Show users that highlighted post author is following", self.action_show_follows)
            yield SystemCommand("View followers", "Show followers of highlighted post author", self.action_show_followers)
            yield SystemCommand("View user likes", "Show likes of highlighted post author", self.action_show_user_likes)
            yield SystemCommand("View lists", "Show lists created by highlighted post author", self.action_show_lists)
            yield SystemCommand("Follow", "Follow (or unfollow) profile of highlighted post author", self.action_handle_follow)
            yield SystemCommand("Mute account", "Mute (or unmute) highlighted post author", self.action_handle_mute_profile)
            yield SystemCommand("Block account", "Block (or unblock) highlighted post author", self.action_handle_block)
            if highlighted.post.blurred:
                yield SystemCommand("Show content", "Show content behind content warning label", self.action_show_blurred_content)
            if self.source.feed_type == 'user':
                if 'post_type' in self.source.params and self.source.params['post_type'] == 'posts_with_replies':
                    yield SystemCommand("Posts feed", "Show only posts and author threads in user feed", self.action_view_user_posts)
                else:
                    yield SystemCommand("Replies feed", "Show posts and replies in user feed", self.action_view_user_replies)
            yield SystemCommand("Copy URL", "Copy highlighted post URL to clipboard", self.action_copy_post_link)
            if highlighted.post.has_external_link():
                yield SystemCommand("Open external link", "Open highlighted post's external link", self.action_open_external_link)
                yield SystemCommand("Copy external link", "Copy highlighted post's external link to clipboard", self.action_copy_external_link)
            if highlighted.post.has_images():
                yield SystemCommand("Open image link", "Open highlighted post's images", self.action_open_image_links)
                yield SystemCommand("Copy image link", "Copy URL(s) of highlighted post's images to clipboard", self.action_copy_image_links)
            if highlighted.post.has_video():
                yield SystemCommand("Open video link", "Open highlighted post's video", self.action_open_video_link)
                yield SystemCommand("Copy video link", "Copy URL of highlighted post's video to clipboard", self.action_copy_video_link)
            if highlighted.post.has_starter_pack() or highlighted.post.has_list():
                yield SystemCommand("View users", "View users of highlighted post's list/starter pack", self.action_view_list_users)
            if highlighted.post.has_starter_pack() or highlighted.post.has_list() or highlighted.post.has_feed():
                yield SystemCommand("View feed", "View feed of highlighted post's feed/list/starter pack", self.action_load_embedded_feed)
            yield SystemCommand("Copy URI", "Copy highlighted post URI to clipboard", self.action_copy_uri)
            yield SystemCommand("Copy post text", "Copy highlighted post text to clipboard", self.action_copy_post_text)
        yield from super().offer_widget_commands()

    def _get_highlighted(self, suppress_notification: bool = False, allow_context: bool = False):
        """Don't return highlighted item if deleted/blocked post or thread context panel"""
        highlighted = super()._get_highlighted(suppress_notification=suppress_notification)
        if getattr(highlighted, 'missing_post', None):
            self.app.notify("Post unavailable", severity="warning")
            return None
        elif not allow_context and getattr(highlighted, 'is_context', None):
            self.app.notify("No post highlighted", severity="warning")
            return None
        else:
            return highlighted

    def action_view_thread(self) -> None:
        """Request the app to build thread for highlighted post"""
        highlighted = self._get_highlighted(allow_context=True) # allow thread context panel to launch thread

        if highlighted is not None:
            uri = highlighted.post.uri
            handle = highlighted.post.handle
            text_excerpt = highlighted.post.post_content if highlighted.post.post_content else None
            if getattr(self.source, 'target', '') != uri:
                self.screen.action_build_thread(uri, title_params={'handle': handle, 'text': text_excerpt})
            else:
                self.app.notify(f'Already viewing thread for {uri}', severity="warning")

    @work
    async def action_handle_like(self) -> None:
        """Action to like/unlike the highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted:

            author = highlighted.post.display_name
            uri = highlighted.post.uri
            cid = highlighted.post.cid
            liked = highlighted.post.liked

            if liked is None:
                result = await self.client.like(uri, cid)
                if result:
                    self.notify(f"Liked {author}'s post")
                    highlighted.post.liked = result
                    highlighted.post.like_count += 1
                    highlighted.refresh()
                else:
                    self.notify(f"Failed to like {author}'s post", severity="error")
            else:
                result = await self.client.delete_like(liked)
                if result:
                    self.notify(f"Unliked {author}'s post")
                    highlighted.post.liked = None
                    highlighted.post.like_count -= 1
                    highlighted.refresh()
                else:
                    self.notify(f"Failed to unlike {author}'s post", severity="error")

    @work
    async def action_handle_repost(self) -> None:
        """Action to repost/undo repost of the highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted:

            author = highlighted.post.display_name
            uri = highlighted.post.uri
            cid = highlighted.post.cid
            reposted = highlighted.post.reposted

            if reposted is None:
                result = await self.client.repost(uri, cid)
                if result:
                    self.notify(f"Reposted {author}'s post")
                    highlighted.post.reposted = result
                    highlighted.post.repost_count += 1
                    highlighted.refresh()
                else:
                    self.notify(f"Failed to like {author}'s post", severity="error")
            else:
                result = await self.client.undo_repost(uri)
                if result:
                    self.notify(f"Undid respost of {author}")
                    highlighted.post.reposted = None
                    highlighted.post.repost_count -= 1
                    highlighted.refresh()
                else:
                    self.notify(f"Failed to undo repost of {author}", severity="error")

    def action_reply(self) -> None:
        """Action to open the reply compose dialog for the highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted:
            self.screen.action_open_post_compose(reference=highlighted.post, post_type='reply')

    def action_quote(self) -> None:
        """Action to open the quote compose dialog for the highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted:
            self.screen.action_open_post_compose(reference=highlighted.post, post_type='quote')

    @work
    async def action_view_profile(self) -> None:
        """Request the app to build user feed for highlighted post author"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.post.handle
            if getattr(self.source, 'target', '') != handle:
                self.screen.action_build_user_feed(handle)
            else:
                profile_view = self.screen.query_one("#profile-view")
                profile_view.loading = True
                self.screen.show_edge_panel('profile-panel')
                await self.screen.build_profile_panel(handle)
    @work
    async def action_delete(self) -> None:
        """Action to delete the highlighted post if own post"""
        highlighted = self._get_highlighted()

        if highlighted:
            handle = highlighted.post.handle
            if handle != self.client.handle:
                self.notify(f"Cannot delete {handle}'s post", severity="warning")
            else:
                uri = highlighted.post.uri
                result = await self.client.delete_post(uri)
                if result:
                    self.highlighted_child.show_post_deleted()
                    self.notify(f"Deleted post {uri}")
                else:
                    self.notify(f"Failed to delete post", severity="error")

    def action_view_likes(self) -> None:
        """Request the app to build feed for likes of highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            uri = highlighted.post.uri
            handle = highlighted.post.handle
            text_excerpt = highlighted.post.post_content if highlighted.post.post_content else None
            self.screen.action_build_likes(uri, title_params={'handle': handle, 'text': text_excerpt})

    def action_view_reposts(self) -> None:
        """Request the app to build feed for reposts of highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            uri = highlighted.post.uri
            handle = highlighted.post.handle
            text_excerpt = highlighted.post.post_content if highlighted.post.post_content else None
            self.screen.action_build_reposts(uri, title_params={'handle': handle, 'text': text_excerpt})

    def action_view_quotes(self) -> None:
        """Request the app to build feed for quotes of highlighted post"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            uri = highlighted.post.uri
            handle = highlighted.post.handle
            text_excerpt = highlighted.post.post_content if highlighted.post.post_content else None
            self.screen.action_build_quotes(uri, title_params={'handle': handle, 'text': text_excerpt})

    def action_view_quoted(self) -> None:
        """Action to view thread of quoted post of highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_quote():
            quoted = highlighted.post.media['quote_posts'][0]
            if type(quoted).__name__ == 'MissingPost':
                self.app.notify("Post unavailable", severity="warning")
                return
            uri = quoted.uri
            handle = quoted.handle
            text_excerpt = quoted.post_content if quoted.post_content else None
            self.screen.action_build_thread(uri, title_params={'handle': handle, 'text': text_excerpt})

    def action_view_list_users(self) -> None:
        """Request the app to build list people feed for highlighted post's embedded starter pack or list"""
        highlighted = self._get_highlighted()

        if highlighted:

            if highlighted.post.has_starter_pack():
                item = highlighted.post.media['starter_packs'][0]
                uri = item['list_uri']
                name = item['display_name']
                self.screen.action_build_list_people(uri, name)

            elif highlighted.post.has_list():
                item = highlighted.post.media['lists'][0]
                uri = item['uri']
                name = item['display_name']
                self.screen.action_build_list_people(uri, name)

    def action_load_embedded_feed(self) -> None:
        """Request the app to rebuild the feed based on highlighted post's embedded starter pack"""
        highlighted = self._get_highlighted()

        if highlighted:

            if highlighted.post.has_starter_pack():
                item = highlighted.post.media['starter_packs'][0]
                uri = item['list_uri']
                name = item['display_name']
                self.screen.action_build_list_feed(uri, name)

            elif highlighted.post.has_list():
                item = highlighted.post.media['lists'][0]
                uri = item['uri']
                name = item['display_name']
                self.screen.action_build_list_feed(uri, name)

            elif highlighted.post.has_feed():
                item = highlighted.post.media['feeds'][0]
                uri = item['uri']
                name = item['display_name']
                self.screen.action_build_custom_feed(uri, name)

    def action_show_follows(self):
        """Action to show follows of highlighted post author."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.post.handle
            self.screen.action_build_follows_list(handle=handle)

    def action_show_followers(self):
        """Action to show followers of highlighted post author."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.post.handle
            self.screen.action_build_follower_list(handle=handle)

    def action_show_user_likes(self):
        """Action to show likes of highlighted post author."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.post.handle
            self.screen.action_build_user_likes(handle=handle)

    def action_show_lists(self):
        """Action to show lists of highlighted post author."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            handle = highlighted.post.handle
            self.screen.action_build_user_lists(handle=handle)

    @work
    async def action_handle_follow(self) -> None:
        """Action to follow the author of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_follow(handle=highlighted.post.handle, following=highlighted.post.following)
            if result['success']:
                highlighted.post.following = result['following']

    @work
    async def action_handle_mute_profile(self) -> None:
        """Action to mute the author of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_mute(handle=highlighted.post.handle, muted=highlighted.post.muted)
            if result['success']:
                highlighted.post.muted = result['muted']
                highlighted.refresh()

    @work
    async def action_handle_block(self) -> None:
        """Action to block the author of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            result = await self._user_action_block(handle=highlighted.post.handle, blocking=highlighted.post.blocking, following=highlighted.post.following)
            if result['success']:
                highlighted.post.blocking = result['blocking']
                highlighted.post.following = result['following']
                highlighted.refresh(recompose=True)

    def action_show_blurred_content(self) -> None:
        """Action to show content behind content/media blur label"""
        highlighted = self._get_highlighted()

        if highlighted is not None:
            highlighted.post.blurred= False
            highlighted.refresh(recompose=True)

    def action_view_user_posts(self) -> None:
        """Action to show posts and author threads for user post feed"""
        self.loading = True
        handle = self.source.target
        self.screen.action_build_user_feed(
            handle=handle,
            params = {
                'post_type': 'posts_and_author_threads',
                'title': f'@{handle}\'s posts'
            }
        )

    def action_view_user_replies(self) -> None:
        """Action to show posts and replies for user post feed"""
        self.loading = True
        handle = self.source.target
        self.screen.action_build_user_feed(
            handle=handle,
            params = {
                'post_type': 'posts_with_replies',
                'title': f'@{handle}\'s posts & replies'
            }
        )

    def action_copy_uri(self) -> None:
        """Action to copy the uri of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted:
            uri = highlighted.post.uri
            self.notify("copied URI to clipboard")
            pyperclip.copy(uri)

    def action_copy_post_text(self) -> None:
        """Action to copy the text of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted:
            text = highlighted.post.post_content
            self.notify("copied post text to clipboard")
            pyperclip.copy(text)

    @work
    async def action_copy_post_link(self) -> None:
        """Action to copy the URL of the highlighted post."""
        highlighted = self._get_highlighted()

        if highlighted:
            uri = highlighted.post.uri
            handle = highlighted.post.handle
            link = await self.client.get_post_url(uri, handle)
            self.notify("copied post link to clipboard")
            pyperclip.copy(link)

    def action_open_image_links(self) -> None:
        """Action to open the URLs of the highlighted post's images."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_images():
            imgs = highlighted.post.media['images']
            urls = [i['url'] for i in imgs]
            multiple = len(imgs) > 1
            self.notify(f"opening image{'s' if multiple else ''}")

            if self.app.open_cmds['images']:
                cmd = self.app.open_cmds['images'].split(' ') + urls
                process = subprocess.Popen(
                    cmd,
                    start_new_session=True
                )
            else:
                for url in urls:
                    webbrowser.open(url)

    def action_copy_image_links(self) -> None:
        """Action to copy the URLs of the highlighted post's images."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_images():
            imgs = highlighted.post.media['images']
            urls = [i['url'] for i in imgs]
            links = '\n'.join(urls)
            multiple = len(imgs) > 1
            self.notify(f"copied image link{'s' if multiple else ''} to clipboard")
            pyperclip.copy(links)

    @work
    async def action_open_video_link(self) -> None:
        """Action to open the highlighted post's video. If no video command is defined in settings, will open post URL in browser."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_video():
            self.notify("opening video")

            if self.app.open_cmds['video']:
                url = highlighted.post.media['videos'][0]['url']
                cmd = self.app.open_cmds['video'].split(' ') + [url]
                process = subprocess.Popen(
                    cmd,
                    start_new_session=True
                )
            else:
                uri = highlighted.post.uri
                handle = highlighted.post.handle
                post_url = await self.client.get_post_url(uri, handle)
                webbrowser.open(post_url)

    def action_copy_video_link(self) -> None:
        """Action to copy the highlighted post's video URL."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_video():
            url = highlighted.post.media['videos'][0]['url']
            self.notify("copied video link to clipboard")
            pyperclip.copy(url)

    def action_open_external_link(self) -> None:
        """Action to open the highlighted post's embedded external link."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_external_link():
            link = highlighted.post.media['external_links'][0]['uri']
            self.notify("opening external link")

            if self.app.open_cmds['external_link']:
                cmd = self.app.open_cmds['external_link'].split(' ') + [link]
                process = subprocess.Popen(
                    cmd,
                    start_new_session=True
                )
            else:
                webbrowser.open(link)

    def action_open_embedded(self) -> None:
        """Action to open the highlighted post's embedded content (image, video, link, quoted post, feed)"""
        highlighted = self._get_highlighted()

        if highlighted:
            # if post content is blurred, display content
            if highlighted.post.blurred:
                highlighted.post.blurred = False
                highlighted.refresh(recompose=True)

            elif highlighted.post.media:
                for media_type, media_item in highlighted.post.media.items():
                    if media_item:
                        match media_type:

                            case 'external_links':
                                self.action_open_external_link()
                                return
                            case 'images':
                                self.action_open_image_links()
                                return
                            case 'videos':
                                self.action_open_video_link()
                                return
                            case 'starter_packs':
                                self.action_view_list_users()
                                return
                            case 'lists':
                                self.action_load_embedded_feed()
                                return
                            case 'feeds':
                                self.action_load_embedded_feed()
                                return

                if highlighted.post.media['quote_posts']:   # check quote posts last
                    self.action_view_quoted()

        else:
            self.app.notify('No embedded media or post', severity="warning")


    def action_copy_external_link(self) -> None:
        """Action to copy the highlighted post's embedded external link."""
        highlighted = self._get_highlighted()

        if highlighted and highlighted.post.has_external_link():
            link = highlighted.post.media['external_links'][0]['uri']
            self.notify("copied external link to clipboard")
            pyperclip.copy(link)


    class Listed(FeedView.Listed):
        """Custom ListItem container to list PostPanel objects in PostFeedView"""

        def compose(self) -> ComposeResult:
            if self.cls == "MissingPost":
                yield PostFeedView.MissingPostPanel(self.data_obj)
            elif self.cls == "ThreadContext":
                yield PostFeedView.ThreadContextPanel(self.data_obj)
            else:
                yield PostFeedView.PostPanel(self.data_obj)

        def show_post_deleted(self) -> None:
            """Change post panel child to deleted post panel"""
            if self.cls == 'Post':
                deleted_post = MissingPost(uri=self.data_obj.uri, is_deleted=True, reply_position=self.data_obj.reply_position)
                self.swap_data(data_obj=deleted_post)

    class MissingPostPanel(FeedPanel):
        def __init__(self, post: MissingPost, is_quote: bool = False, **kwargs):
            self.post = post
            self.missing_post = True
            self.is_quote = is_quote
            super().__init__(**kwargs)

        def render(self) -> Panel:

            if getattr(self.post, 'reply_position', '') == 'root':
                box_style = ROOT_REPLY_BOX
                self.styles.margin = (1, 1, 0, 1)
            elif getattr(self.post, 'reply_position', '') == 'parent':
                box_style = PARENT_REPLY_BOX
                self.styles.margin = (0, 1, 0, 1)
            elif getattr(self.post, 'reply_position', '') == 'node':
                box_style = REPLY_BOX
                self.styles.margin = (0, 1, 1, 1)
            else:
                box_style = box.ROUNDED

            body = Text("[Post Deleted]" if self.post.is_deleted else "[User Blocked]", style=self.app.theme_variables["error"])

            if not self.is_quote:
                border_style = self.app.theme_variables["foreground"]
            else:
                border_style = self.app.theme_variables["foreground-darken-2"]

            return Panel(
                body,
                border_style=border_style,
                box=box_style,
                padding=(1, 2),
            )

    class ThreadContextPanel(FeedPanel):
        def __init__(self, post: ThreadContext, **kwargs):
            self.post = post
            self.is_context = True
            super().__init__(**kwargs)

        def render(self) -> Panel:
            title_params = {'handle': self.post.handle, 'text': None}
            body = Text.from_markup(f"[@click=screen.build_thread('{self.post.uri}', {str(title_params)})]View full thread[/]")

            return Panel(
                body,
                border_style=self.app.theme_variables["foreground"],
                box=THREAD_CONTEXT_BOX,
                padding=(1, 2),
            )

    class PostPanelLabel(Widget):
        """Widget that renders label alongside or in place of content."""

        def __init__(self, post: Post, blur: list, **kwargs):
            self.post = post
            self.blur = blur
            super().__init__(**kwargs)

        def render(self):
            text = Text()
            for label in self.blur:
                color = self.app.theme_variables['text-accent'] if label['severity'] == 'inform' else self.app.theme_variables['text-error']
                text.append(f'[{label['label'].replace('-',' ').title()}] ', style=color)
            return text


    class PostPanel(FeedPanel):
        """Feed panel for rendering post content"""

        def __init__(self, post: Post, is_quote: bool = False, **kwargs):
            self.post = post
            self.is_quote = is_quote
            super().__init__(**kwargs)

        def render(self) -> SplitTitlePanel:
            """Render background panel with post info"""

            # create title content
            title = self.build_title(
                display_name=self.post.display_name,
                handle=self.post.handle,
                created_at=self.post.created_at,
                blocking=self.post.blocking,
                muted=self.post.muted,
            )

            is_repost = self.post.repost is not None
            is_pin = self.post.reason is not None and self.post.reason == 'pin'

            right_title = None
            # TODO change display name for own reposts
            if is_repost:
                reposter = self.post.repost['display_name'] if self.post.repost['display_name'] else self.post.repost['handle']
                right_title = Text("🔁 Reposted by " + reposter)
            elif is_pin:
                right_title = Text("📌")

            # set style depending on repost, reply, quote status etc.
            use_inner_subtitle = False
            if is_pin:
                box_style = box.HEAVY
            elif is_repost:
                box_style = box.DOUBLE
            elif getattr(self.post, 'reply_position', '') == 'root':
                box_style = ROOT_REPLY_BOX
                self.styles.margin = (1, 1, 0, 1)
                use_inner_subtitle = True
            elif getattr(self.post, 'reply_position', '') == 'parent':
                box_style = PARENT_REPLY_BOX
                self.styles.margin = (0, 1, 0, 1)
                use_inner_subtitle = True
            elif getattr(self.post, 'reply_position', '') == 'node':
                box_style = REPLY_BOX
                self.styles.margin = (0, 1, 1, 1)
            else:
                box_style = box.ROUNDED

            if self.post.thread_main_post:
                self.parent.add_class("main-post")

            if not self.is_quote:
                border_style = self.app.theme_variables["foreground"]
            else:
                border_style = self.app.theme_variables["foreground-darken-2"]

            # create subtitle content
            if not self.is_quote and not self.app.hide_metrics and not use_inner_subtitle:
                subtitle = self.build_subtitle(
                    reply_count=self.post.reply_count,
                    repost_count=self.post.repost_count,
                    quote_count=self.post.quote_count,
                    like_count=self.post.like_count,
                    liked=self.post.liked,
                    reposted=self.post.reposted,
                )
            else:
                subtitle = ''

            return SplitTitlePanel(
                "", # build content in compose
                left_title=title,
                right_title=right_title,
                subtitle=subtitle,
                subtitle_align="center",
                border_style=border_style,
                box=box_style,
                padding=(1, 2),
            )

        def build_title(self, display_name: str, handle: str, created_at: str, blocking: bool = False, muted: bool = False):
            """Build panel title"""
            title = Text()
            if display_name:
                title.append(display_name + " ", style="bold")
            title.append(handle_to_link(handle))
            title.append(" · " + format_time(timestamp=created_at, relative=self.app.relative_dates))
            if blocking:
                title.append(' 🚫')
            if muted:
                title.append(' 🔇')
            return title

        def build_subtitle(self, reply_count: int, repost_count: int, quote_count: int, like_count: int, liked: str | None, reposted: str | None):
            """Build panel subtitle"""
            base_color = self.app.theme_variables["foreground"]
            liked_color = f"bold {self.app.theme_variables["text-error"]}"
            reposted_color = f"bold {self.app.theme_variables["text-success"]}"

            subtitle = Text()
            subtitle.append(f'{abbrev_num(reply_count)} replies | ' + " ")
            subtitle.append(f'{abbrev_num(repost_count)} reposts' + " ", style=base_color if reposted is None else reposted_color)
            subtitle.append(' | ' + " ")
            subtitle.append(f'{abbrev_num(quote_count)} quotes | ' + " ")
            subtitle.append(f'{abbrev_num(like_count)} likes', style=base_color if liked is None else liked_color)
            return subtitle

        def compose(self):
            """Compose content and embedded media widgets within the panel borders"""

            if self.post.blocking:
                yield self.PostPanelContent('[User Blocked]', style=self.app.theme_variables["text-error"])
                return


            if self.post.information_labels:
                yield PostFeedView.PostPanelLabel(post=self.post, blur=self.post.information_labels, classes='post-embedded-content')

            if self.post.content_blur and self.post.blurred:
                yield PostFeedView.PostPanelLabel(post=self.post, blur=self.post.content_blur, classes='post-embedded-content')

            elif len(self.post.post_content) > 0:
                yield self.PostPanelContent(post_content=self.post.post_content)

            if self.post.media_blur and self.post.blurred:
                yield PostFeedView.PostPanelLabel(post=self.post, blur=self.post.media_blur, classes='post-embedded-content')

            elif self.post.media and not (self.post.content_blur and self.post.blurred):

                if 'images' in self.post.media and len(self.post.media['images']) > 0:
                    for img in self.post.media['images']:
                        yield self.PostMediaPanel(img, media_type="image", classes='post-embedded-content')

                elif 'videos' in self.post.media and len(self.post.media['videos']) > 0:
                    yield self.PostMediaPanel(self.post.media['videos'][0], media_type="video", classes='post-embedded-content')

                elif 'external_links' in self.post.media and len(self.post.media['external_links']) > 0:
                    yield self.PostExternalEmbed(self.post.media['external_links'][0], classes='post-embedded-content')

                elif 'starter_packs' in self.post.media and len(self.post.media['starter_packs']) > 0:
                    yield StarterPackPanel(StarterPack.from_dict(self.post.media['starter_packs'][0]), is_embedded=True, classes='post-embedded-content')

                elif 'lists' in self.post.media and len(self.post.media['lists']) > 0:
                    l = self.post.media['lists'][0]
                    l['type'] = 'list'
                    yield CustomFeedPanel(CustomFeed.from_dict(l), is_embedded=True, classes='post-embedded-content')

                elif 'feeds' in self.post.media and len(self.post.media['feeds']) > 0:
                    f = self.post.media['feeds'][0]
                    f['type'] = 'feed'
                    yield CustomFeedPanel(CustomFeed.from_dict(f), is_embedded=True, classes='post-embedded-content')

                if 'quote_posts' in self.post.media and len(self.post.media['quote_posts']) > 0:
                    if type(self.post.media['quote_posts'][0]).__name__ == 'Post':
                        yield PostFeedView.PostPanel(self.post.media['quote_posts'][0], is_quote=True, classes="quote-post")
                    else:
                        yield PostFeedView.MissingPostPanel(self.post.media['quote_posts'][0], is_quote=True, classes="quote-post")

                if getattr(self.post, 'reply_position', '') in ['root', 'parent']:
                    subtitle = self.build_subtitle(
                        reply_count=self.post.reply_count,
                        repost_count=self.post.repost_count,
                        quote_count=self.post.quote_count,
                        like_count=self.post.like_count,
                        liked=self.post.liked,
                        reposted=self.post.reposted,
                    )
                    yield self.PostInnerSubtitle(subtitle)


        class PostPanelContent(Widget):
            """Widget that renders post content."""

            def __init__(self, post_content: str, style: str | None = None, **kwargs):
                self.post_content = post_content
                self.style = style
                super().__init__(**kwargs)

            def render(self):
                if self.style: #i.e., user blocked
                    return Text(self.post_content, style=self.style)
                return extract_tags_and_handles(self.post_content)

        class PostInnerSubtitle(Widget):
            """Widget that renders subtitle content inside panel borders."""

            def __init__(self, subtitle: Text, **kwargs):
                self.subtitle = subtitle
                super().__init__(**kwargs)

            def render(self):
                return self.subtitle


        class PostMediaPanel(Widget):
            """Container for post media"""

            def __init__(self, media_item: dict, media_type: str, display_media: bool = False, **kwargs):
                self.media_item = media_item
                self.media_type = media_type
                self.display_media = display_media
                super().__init__(**kwargs)

            def render(self):
                """Render background panel"""

                if self.media_type == 'image':
                    border_style = self.app.theme_variables["text-success"]
                else: # video
                    border_style = self.app.theme_variables["text-accent"]

                return Panel(
                    "",
                    title=Text(self.media_type),
                    title_align='left',
                    border_style=border_style,
                    padding=(1, 2),
                    box=box.HEAVY,
                )

            def compose(self):
                yield self.PostMediaAlt(self.media_item, media_type=self.media_type, classes='post-embedded-content')


            class PostMediaAlt(Widget):
                """Widget that renders post image and video alt text."""

                def __init__(self, media_item: dict, media_type: str, **kwargs):
                    self.media_item = media_item
                    self.media_type = media_type
                    super().__init__(**kwargs)

                def render(self):
                    alt = 'No alt text provided'
                    if self.media_item['alt'] is not None:
                        if len(self.media_item['alt']) > 0:
                            alt = 'alt: ' + self.media_item['alt'].strip()

                    body = Text(alt, style=self.app.theme_variables["text-secondary"], overflow='ellipsis')

                    return body


        class PostExternalEmbed(Widget):
            """Widget that renders post external links."""

            def __init__(self, external_link: dict, **kwargs):
                self.external_link = external_link
                super().__init__(**kwargs)

            def render(self):
                body_parts = []

                if self.external_link['description']:
                    body_parts.append(Text(self.external_link['description'], style=self.app.theme_variables["text-secondary"]))
                body_parts.append(Text(self.external_link['uri'], style="cyan", overflow='ellipsis'))
                body = Group(*body_parts)

                return Panel(
                    body,
                    title=Text(self.external_link['title'], style="bold cyan", overflow='ellipsis'),
                    title_align='left',
                    border_style="cyan",
                    padding=(1, 2),
                    box=box.HEAVY,
                )
