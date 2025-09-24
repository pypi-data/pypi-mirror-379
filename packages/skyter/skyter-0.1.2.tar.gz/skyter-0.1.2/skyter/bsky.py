from typing import Union, Any, Callable, TypeVar
import functools
import os
from datetime import datetime, timezone
import re
import aiohttp
from asyncio import iscoroutinefunction
from atproto import AsyncClient, models, client_utils
from atproto.exceptions import AtProtocolError
from atproto_client.models.app.bsky.feed.defs import ReasonRepost, ReasonPin

T = TypeVar("T", bound=Callable[..., Any])
Reason = Union[ReasonRepost, ReasonPin]


class FeedPaginator:
    """
    Tracks pagination state and handles API method calls for bsky get endpoints with cursors.
    """

    MAX_FETCH_PER_CALL = 100

    def __init__(self, feed: str, params: dict, id_extractor: callable, api_method: callable, response_data_field: str):
        self.feed = feed
        self.params = params if params else {}
        self.limit = self.params['limit'] if 'limit' in self.params else 100
        self.id_extractor = id_extractor
        self.api_method = api_method
        self.response_data_field = response_data_field
        self.cursor = None
        self.seen_items = set()
        self.has_more = True
        self.total_fetched = 0

    async def next_page(self) -> list:
        """
        Get next page of results using api_method and update state.

        Returns:
            list: List of feed items from API response
        """
        self.fetched_this_call = 0
        feed = []
        while len(feed) < self.limit and self.fetched_this_call < self.MAX_FETCH_PER_CALL:
            params = self._get_request_params()
            if not params: break
            params['limit'] = self.limit - len(feed)

            response = await self.api_method(params)
            response_data = self._get_value(response, self.response_data_field)
            if response_data is None: break
            feed.extend(response_data)
            cursor = self._get_value(response, 'cursor')

            self._update_from_response(cursor, len(response_data))
            feed = self._filter_seen(feed)

        self._mark_seen(feed)

        return feed

    async def check_new_available(self) -> bool:
        """
        Check if new items are available.

        Returns:
            bool: True if there are new items
        """
        tmp_params = self._get_new_items_request_params()
        if not tmp_params: return False
        tmp_params['limit'] = 1
        response = await self.api_method(tmp_params)
        response_data = self._get_value(response, self.response_data_field)
        if response_data:
            item_id = self.id_extractor(response_data[0])
            if item_id not in self.seen_items:
                return True
        return False

    async def new(self) -> list:
        """
        Get new items using api_method.

        Returns:
            list: List of feed items from API response
        """
        # if cursor hasn't been initialized, just get the first page as normal
        if not self.cursor: return self.next_page()

        tmp_params = self._get_new_items_request_params()
        if not tmp_params: return []

        self.fetched_this_call = 0
        no_seen = True
        feed = []
        while no_seen and self.fetched_this_call < self.MAX_FETCH_PER_CALL:
            response = await self.api_method(tmp_params)
            response_data = self._get_value(response, self.response_data_field)
            if not response_data: break
            tmp_params['cursor'] = self._get_value(response, 'cursor')

            for item in response_data:
                item_id = self.id_extractor(item)
                if item_id not in self.seen_items:
                    feed.append(item)
                else:
                    # stop once we run into the first seen item; may not work correctly for nonchronilogical feeds or feeds that allow duplicate items
                    no_seen = False
                    break

            self.fetched_this_call += len(response_data)
            self.total_fetched += len(response_data)

        self._mark_seen(feed)

        return feed

    def _get_request_params(self):
        """
        Get the parameters needed for the next API request.

        Returns:
            dict: Parameters for the API call, or None if no more posts available
        """
        if not self.has_more:
            return None

        params = self.params

        params["limit"] = min(params["limit"], 100)

        if self.cursor:
            params["cursor"] = self.cursor

        return params


    def _get_new_items_request_params(self):
        """
        Get the parameters needed for API request, ignoring cursor.

        Returns:
            dict: Parameters for the API call, or None if no more posts available
        """
        params = self._get_request_params()
        if not params: return None
        new_item_params = {k:v for k,v in params.items() if k not in ['cursor']}
        if 'include_pins' in new_item_params:
            new_item_params['include_pins'] = False
        return new_item_params

    def _get_value(self, source, field: str):
        """
        Get data from either object or dictionary response. For handling both atproto library responses + direct API http responses

        Args:
            source: Dictionary or object to get field from
            field (str): Attribute or key to get

        Returns:
            Value if found, otherwise default
        """
        if hasattr(source, '__getitem__'):
            try:
                return source[field]
            except (KeyError, TypeError):
                pass

        if hasattr(source, field):
            return getattr(source, field)

        return None

    def _update_from_response(self, cursor, posts_count) -> None:
        """
        Update paginator state based on API response.

        Args:
            cursor: cursor in the API response
            posts_count (int): Number of posts received in this response
        """
        self.cursor = cursor
        self.fetched_this_call += posts_count
        self.total_fetched += posts_count

        # Check if we have more posts available
        if not self.cursor:
            self.has_more = False

    def _filter_seen(self, feed) -> list:
        """
        Filter seen feed items from response, (e.g., for search results, user lists / custom feeds without stable pagination)

        Args:
            feed (list): data object in the API response

        Returns:
            list: List of feed item removing already seen items
        """
        new_feed = []
        for item in feed:
            item_id = self.id_extractor(item)
            if item_id not in self.seen_items:
                new_feed.append(item)
        return new_feed

    def _mark_seen(self, feed):
        """
        Add feed items to seen items.

        Args:
            feed (list): data object from the API response
        """
        for item in feed:
            item_id = self.id_extractor(item)
            if item_id not in self.seen_items:
                self.seen_items.add(item_id)

    def mark_error(self):
        """Mark that an error occurred (stops further pagination)."""
        self.has_more = False

    def get_status(self):
        """Get current pagination status."""
        return {
            "total_fetched": self.total_fetched,
            "has_more": self.has_more,
            "cursor": self.cursor,
            "params": self.params,
        }


def auth_required(func: T) -> T:
    """Decorator to check if the client is authenticated before trying function"""

    if iscoroutinefunction(func=func):
        @functools.wraps(func)
        async def async_wrapper(self, *args, **kwargs):
            if self.is_authenticated:
                return await func(self, *args, **kwargs)
            else:
                print(f"Must be logged in to use {func.__name__}")
                return None
        return async_wrapper

    else:
        @functools.wraps(func)
        def sync_wrapper(self, *args, **kwargs):
            if self.is_authenticated:
                return func(self, *args, **kwargs)
            else:
                print(f"Must be logged in to use {func.__name__}")
                return None
        return sync_wrapper


class BlueSkyClient:
    """Higher-level wrapper for atproto async operations."""

    def __init__(self, pds_url: str | None = None):
        """
        Initialize the Bluesky client, optionally setting a URL (for PDS)
        """
        self.pds_url = pds_url
        self.client = AsyncClient(base_url=pds_url)
        self.is_authenticated = False
        self.paginator = None
        self.default_labelers = [ # non-global labelers that are automatically applied
            'did:plc:ar7c4by46qjdydhdevvrndac'  # @moderation.bsky.app
        ]


    # Authentication

    async def login(self, username: str, password: str, pds: str | None = None) -> bool:
        """
        Login to Bluesky account.

        Args:
            username (str): Bluesky handle or email address
            password (str): Account password or app password

        Returns:
            bool: True if login successful
        """

        if pds:
            self.update_pds_url(url=pds)

        try:
            await self.client.login(username, password)
            self.handle = self.client.me.handle
            self.is_authenticated = True
            print(f"Successfully logged in as {self.handle}")
            return True
        except AtProtocolError as e:
            print(f"Login failed: {e}")
            self.is_authenticated = False
            return False

    def update_pds_url(self, url: str) -> bool:
        """
        Change base URL of client, i.e., to switch PDS

        Args:
            url (str): URL

        Returns:
            bool: True if changed
        """
        if self.client._base_url != url:
            self.pds_url = url
            self.client.update_base_url(base_url=url)
            return True
        return False


    # Utils

    @staticmethod
    def _uri_parts(uri: str) -> dict:
        """Returns uri components (repo did, collection, rkey) separated as a dict"""
        parts = uri.replace('at://', '').split('/')
        return {
            'repo_did': parts[0],  # e.g., did:plc:abc123
            'collection': parts[1],  # e.g., app.bsky.feed.repost
            'rkey': parts[2],  # e.g., xyz789
        }

    @auth_required
    async def _build_feed_item(self, obj, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, reason: Reason | None = None) -> dict:
        """
        Processes feed item with optional media/embed handling.

        Args:
            obj: The object to process. Expected to be a structured atproto response from feed endpoints.
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.

        Returns:
            dict: The processed result as a dict
        """
        result = {
            'uri': obj.uri,
            'cid': obj.cid,
            'created_at': obj.record.created_at,
            'langs': obj.record.langs,
            'author': {
                'did': obj.author.did,
                'handle': obj.author.handle,
                'display_name': obj.author.display_name,
                'avatar': obj.author.avatar,
                'following': obj.author.viewer.following,
                'followed_by': obj.author.viewer.followed_by,
                'muted': obj.author.viewer.muted,
                'blocking': obj.author.viewer.blocking,
                'blocked_by': obj.author.viewer.blocked_by,
                'labels': [
                    {
                        'label': label.val,
                        'labeler': label.src,
                    } for label in obj.author.labels
                ],
            },
            'text': getattr(obj.record, 'text', None),
            'like_count': obj.like_count,
            'quote_count': obj.quote_count,
            'reply_count': obj.reply_count,
            'repost_count': obj.repost_count,
            'viewer': {
                'like': obj.viewer.like,
                'repost': obj.viewer.repost,
                'muted': obj.viewer.thread_muted,
                'reply_disabled': obj.viewer.reply_disabled, # can be True, False or None / False or None -> replyable
                'embedding_disabled': obj.viewer.embedding_disabled,
                'pinned': obj.viewer.pinned, # None -> not pinnable
            },
            'labels': [
                {
                    'label': label.val,
                    'labeler': label.src,
                } for label in obj.labels
            ],
            'reason': reason.py_type.split('reason')[-1].lower() if reason is not None else None
        }

        if result['reason'] is not None and result['reason'] == 'repost':
           result['repost'] = {
                'handle': reason.by.handle,
                'display_name': reason.by.display_name,
                'uri': reason.uri,
            }

        # TODO option to ignore replies?
        if extract_reply_parents and obj.record.reply is not None:
            result['reply_parent'] = await self._build_reply_info(obj.record.reply)

        if extract_media:
            result['media'] = await self.extract_media_from_post(obj, media_types=media_types,
            include_quoted_media=include_quoted_media, quote_nesting=quote_nesting)

        return result

    @auth_required
    async def _build_reply_info(self, reply_obj):
        """
        Unpacks reply parent and root information from a post into a dictionary.

        Args:
            reply_obj: A ReplyRef object from atproto feed response

        Returns:
            dict: dictionary of containing the parent post, root post, and boolean representing whether there are intermediate posts between root and parent
        """

        parent_uri = getattr(reply_obj.parent, 'uri', None)
        root_uri = getattr(reply_obj.root, 'uri', None)

        result = {
            'parent': await self.get_post_data(parent_uri, extract_reply_parents=False),
            'root': await self.get_post_data(root_uri, extract_reply_parents=False),
            'intermediate_posts': await self._check_intermediate_reply_parents(parent=parent_uri, root=root_uri),
        }

        return result

    @auth_required
    async def _check_intermediate_reply_parents(self, parent: str, root: str) -> bool:
        """
        Check whether there are intermediate reply parent posts between parent and root.

        Args:
            parent (str): URI of reply parent
            root (str): URI of reply root

        Returns:
            bool: True if there are intermediate reply parent posts between parent and root. False if parent is a top-level post or direct child of root.
        """

        if parent == root:
            return False

        try:
            response = await self.client.app.bsky.feed.get_posts({'uris': [parent]}) #, root]})
            if len(response.posts) == 0:
                return False
            else:
                response=response.posts[0]
                if response.record.reply is not None and response.record.reply.parent.uri is not None:
                    return response.record.reply.parent.uri != root

            return False

        except Exception as e:
            print(f"Failed to get post data for {parent}: {e}")
            return None

    @auth_required
    async def _get_records(self, collection: str, repo: str | None = None, limit: int | None = None) -> list:
        """
        Helper method to get records from a repository.

        Args:
            collection (str): Collection name (e.g., 'app.bsky.graph.follow')
            repo (str): Repository DID (defaults to current user's DID)
            limit (int): max number of records (optional)

        Returns:
            list: List of records
        """

        try:
            target_repo = repo or self.client.me.did
            records_response = await self.client.com.atproto.repo.list_records(
                models.ComAtprotoRepoListRecords.Params(
                    repo=target_repo,
                    collection=collection,
                    limit=limit,
                )
            )
            return records_response.records
        except Exception as e:
            print(f"Failed to get records for {collection}: {e}")
            return []

    @staticmethod
    async def download_file(url: str) -> bytes:
        """Download file at url"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.read()
                else:
                    raise Exception(f"Failed to download file: {response.status}")

    async def build_post_text(self, text) -> client_utils.TextBuilder:
        """
        Build TextBuilder with regex pattern matching for hashtags, mentions and links.

        Args:
            text (str): text to process

        Returns:
            TextBuilder: TextBuilder object identifying tags, mentions, links
        """

        # name, match pattern, one-character lookbehind
        patterns = [
            ('tag', r'#((?=\S*[a-zA-Z])[^\s]*[a-zA-Z0-9](?=\s|[^a-zA-Z0-9]+\s|$))', r'\s'),
            ('mention', r'@((?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})', r'\s|\.'),
            ('link', r'https?://(?:[-\w.])+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?', r'\s'),
        ]

        look_behind = lambda pos, pattern: pos == 0 or re.match(pattern, text[pos-1])

        tb = client_utils.TextBuilder()
        position = 0
        while position < len(text):
            matched = False
            for link_type, regex, look_behind_regex in patterns:
                match = re.match(regex, text[position:])
                if match and look_behind(pos=position, pattern=look_behind_regex):
                    if link_type == 'link':
                        tb.link(match.group(0), match.group(0))
                    elif link_type == 'tag':
                        tb.tag(match.group(0), match.group(1))
                    elif link_type == 'mention':
                        profile = await self.get_profile(match.group(1))
                        if profile:
                            tb.mention(match.group(0), profile['did'])
                        else:
                            tb.text(match.group(0))
                    position += match.end()
                    matched = True
                    break

            if not matched:
                tb.text(text[position])
                position += 1

        return tb


    # Actions

    @auth_required
    async def like(self, uri: str, cid: str | None = None) -> str | None:
        """
        Like a post.

        Args:
            uri (str): URI of post to like
            cid (str, optional): Content ID of the post (will be fetched if not provided)

        Returns:
            str: created like record uri or None if unsuccessful
        """

        try:
            # Get CID if not provided
            if not cid:
                post_data = await self.get_post_data(uri, extract_media=False, extract_reply_parents=False)
                if not post_data:
                    print(f"Could not fetch post data for {uri}")
                    return None
                cid = post_data['cid']

            response = await self.client.like(uri, cid)
            print(f"Liked post: {uri}")
            return response.uri
        except AtProtocolError as e:
            print(f"Failed to like post: {e}")
            return None

    @auth_required
    async def unlike(self, uri: str) -> bool:
        """
        Unlike a post via post URI.

        Args:
            uri (str): URI of post to unlike

        Returns:
            bool: True if successful
        """

        try:
            my_did = self.client.me.did


            # List records from your like collection
            records = await self._get_records(collection='app.bsky.feed.like', repo=my_did)

            # Find the like record for this specific post
            for record in records:
                if hasattr(record, 'value') and hasattr(record.value, 'subject'):
                    if record.value.subject.uri == uri:
                        return await self.delete_like(uri=record.uri)

                print("Could not find like record to delete")
                return False

        except AtProtocolError as e:
            print(f"Failed to unlike post: {e}")
            return False

    @auth_required
    async def delete_like(self, uri: str) -> bool:
        """
        Unlike a post via like URI.

        Args:
            uri (str): URI of like to delete

        Returns:
            bool: True if successful
        """

        uri_parts = self._uri_parts(uri)

        try:
            await self.client.app.bsky.feed.like.delete(repo=uri_parts['repo_did'], rkey=uri_parts['rkey'])
            print(f"Unliked post: {uri}")
            return True
        except (AttributeError, AtProtocolError) as e:
            print(f"Built-in delete failed: {e}")
            return False

    @auth_required
    async def follow(self, handle: str) -> bool:
        """
        Follow a user.

        Args:
            handle (str): Handle of user to follow

        Returns:
            bool: True if successful
        """

        try:
            # Get the user's DID first
            profile = await self.client.get_profile(handle)
            result = await self.client.follow(profile.did)
            print(f"Successfully followed {handle}")
            return result.uri
        except AtProtocolError as e:
            print(f"Failed to follow {handle}: {e}")
            return None

    @auth_required
    async def unfollow(self, handle: str) -> bool:
        """
        Unfollow a user.

        Args:
            handle (str): Handle of user to unfollow

        Returns:
            bool: True if successful
        """

        try:
            profile = await self.client.get_profile(handle)
            target_did = profile.did

            # Find the follow record for this user
            follows = await self.get_follows()
            for follow in follows:
                if follow['did'] == target_did:
                    follow_uri = follow['following']
                    result = await self.remove_follow_record(uri=follow_uri)
                    if result:
                        print(f"Successfully unfollowed {handle}")
                    return result

            print(f"Follow record not found for {handle} - may not be following them")
            return False

        except AtProtocolError as e:
            print(f"Failed to unfollow {handle}: {e}")
            return False

    @auth_required
    async def remove_follow_record(self, uri: str) -> bool:
        """
        Unfollow user via follow uri.

        Args:
            uri (str): uri of follow record to delete.

        Returns:
            bool: True if successful
        """
        try:
            await self.client.unfollow(uri)
            return True
        except Exception as e:
            print(f'failed to unfollow {uri}: {e}')
            return False

    @auth_required
    async def mute_user(self, handle: str) -> str | None:
        """Mute a user by their handle.

        Args:
            handle (str): The user's handle

        Returns:
            bool: True if successful, False if failed
        """

        try:
            profile = await self.client.get_profile(handle)
            did = profile.did

            response = await self.client.app.bsky.graph.mute_actor({'actor': did})

            if response:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error muting user {handle}: {e}")
            return False

    @auth_required
    async def unmute_user(self, handle: str) -> str | None:
        """Unmute a muted user by their handle.

        Args:
            handle (str): The user's handle

        Returns:
            bool: True if successful, False if failed
        """

        try:
            profile = await self.client.get_profile(handle)
            did = profile.did

            response = await self.client.app.bsky.graph.unmute_actor({'actor': did})
            return response

        except Exception as e:
            print(f"Error unmuting user {handle}: {e}")
            return False

    @auth_required
    async def block_user(self, handle: str) -> str | None:
        """Block a user by their handle.

        Args:
            handle (str): The user's handle

        Returns:
            str: URI of the block record if successful, None if failed
        """

        try:
            profile = await self.client.get_profile(handle)
            did = profile.did

            record = {
                'subject': did,
                'createdAt': self.client.get_current_time_iso()
            }

            response = await self.client.com.atproto.repo.create_record({
                'repo': self.client.me.did,
                'collection': 'app.bsky.graph.block',
                'record': record
            })

            return response.uri if hasattr(response, 'uri') else None

        except Exception as e:
            print(f"Error blocking user {handle}: {e}")
            return None

    @auth_required
    async def unblock_user(self, handle: str) -> bool:
        """
        Unblock a user by handle.

        Args:
            handle (str): The user's handle

        Returns:
            bool: True if successful
        """

        try:
            # List block records
            block_list = await self.get_block_list()

            # Find the like record for this specific post
            for record in block_list:

                if record['handle'] == handle:
                    return await self.delete_block(record['blocking'])

            print("Could not find block record to delete")
            return False

        except AtProtocolError as e:
            print(f"Failed to unblock user: {e}")
            return False

    @auth_required
    async def delete_block(self, uri: str) -> bool:
        """
        Unblock a user via block URI.

        Args:
            uri (str): URI of block to delete

        Returns:
            bool: True if successful
        """

        uri_parts = self._uri_parts(uri)

        try:
            await self.client.app.bsky.graph.block.delete(
                repo=uri_parts['repo_did'],
                rkey=uri_parts['rkey']
            )
            print(f"Deleted block: {uri}")
            return True
        except (AttributeError, AtProtocolError) as e:
            print(f"Built-in delete failed: {e}")
            return False

    @auth_required
    async def post(self, text: str, reply_to: str | None = None, images: list[dict] | None = None, video: dict | None = None, link: str | None = None, quote: str | None = None, no_rich_text: bool = False) -> str | None:
        """
        Create a new post.

        Args:
            text (str): Post content
            reply_to (str, optional): URI of post to reply to
            images (list[dict], optional): List of image dictionaries to attach
            video (dict, optional): Video dictionary to attach
            link (dict, optional): External link dictionary to attach
            quote (str, optional): URI of post to quote
            no_rich_text (bool): If True, will skip link/tag/mention processing for post content. Defaults to False

        Returns:
            str: URI of created post, or None if failed
        """

        if not no_rich_text:
            text = await self.build_post_text(text)

        try:
            media_embed = None
            record_embed = None

            # Handle image uploads
            if images:
                uploaded_images = []
                for img in images[:4]:  # Max 4 images
                    img_path = img['path']
                    alt = img.get('alt')
                    if os.path.exists(img_path):
                        with open(img_path, 'rb') as f:
                            upload = await self.client.upload_blob(f.read())
                            uploaded_images.append(models.AppBskyEmbedImages.Image(
                                alt=alt if alt is not None else '',
                                image=upload.blob
                            ))

                if uploaded_images:
                    media_embed = models.AppBskyEmbedImages.Main(images=uploaded_images)

            # handle video uploads. sometimes will result in "Video not found". more info: https://github.com/MarshalX/atproto/issues/418
            elif video:
                video_path = video['path']
                alt = video.get('alt')
                if os.path.exists(video_path):
                    with open(video_path, 'rb') as f:
                        upload = await self.client.upload_blob(f.read())
                    if upload:
                        media_embed = models.AppBskyEmbedVideo.Main(video=upload.blob, alt=alt)

            # handle link
            elif link:
                thumb = None
                if link.get('image'):
                    image_data = await self.download_file(link['image'])
                    if image_data:
                        upload = await self.client.upload_blob(image_data)
                        thumb = upload.blob

                media_embed = models.AppBskyEmbedExternal.Main(
                    external=models.AppBskyEmbedExternal.External(
                        description=link['description'],
                        title=link['title'],
                        uri=link['url'],
                        thumb=thumb,
                    )
                )

            # handle quote posts
            if quote:
                post_data = await self.get_post_data(quote, extract_media=False, extract_reply_parents=False)
                if post_data:
                    record_embed = models.AppBskyEmbedRecord.Main(
                        record=models.ComAtprotoRepoStrongRef.Main(
                            uri=post_data['uri'],
                            cid=post_data['cid'],
                        )
                    )

            # combine media and embed records if both used
            if record_embed and media_embed:
                embed = models.AppBskyEmbedRecordWithMedia.Main(
                    media=media_embed,
                    record=record_embed
                )
            else:
                embed = record_embed or media_embed

            # Handle reply
            reply = None
            if reply_to:
                parent = await self.get_post_data(reply_to, extract_media=False)
                if parent:
                    root = parent['reply_parent']['root'] if 'reply_parent' in parent else parent
                    reply = models.AppBskyFeedPost.ReplyRef(
                        root=models.ComAtprotoRepoStrongRef.Main(
                            uri=root['uri'],
                            cid=root['cid']
                        ),
                        parent=models.ComAtprotoRepoStrongRef.Main(
                            uri=reply_to,
                            cid=parent['cid']
                        )
                    )

            post = await self.client.send_post(
                text=text,
                reply_to=reply,
                embed=embed
            )

            print(f"Post created: {post.uri}")
            return post.uri

        except AtProtocolError as e:
            print(f"Failed to create post: {e}")
            return None

    @auth_required
    async def delete_post(self, uri: str) -> bool:
        """
        Delete a post.

        Args:
            uri (str): URI of post to delete

        Returns:
            bool: True if successful
        """

        try:
            return await self.client.delete_post(uri)

        except Exception as e:
            print(f"Failed to delete post: {e}")
            return False

    @auth_required
    async def repost(self, uri: str, cid: str | None = None) -> str | None:
        """
        Repost a post.

        Args:
            uri (str): URI of post to repost
            cid (str, optional): Content ID of the post (will be fetched if not provided)

        Returns:
            str: created repost record uri or None if unsuccessful
        """

        try:
            # Get CID if not provided
            if not cid:
                post_data = await self.get_post_data(uri, extract_media=False, extract_reply_parents=False)
                if not post_data:
                    print(f"Could not fetch post data for {uri}")
                    return None
                cid = post_data['cid']

            response = await self.client.repost(uri, cid)
            print(f"Reposted: {uri}")
            return response.uri
        except AtProtocolError as e:
            print(f"Failed to repost: {e}")
            return None

    @auth_required
    async def undo_repost(self, uri: str) -> bool:
        """
        Undo repost via original post URI.

        Args:
            uri (str): URI of post to undo repost of

        Returns:
            bool: True if successful
        """

        try:
            my_did = self.client.me.did


            # List records from your repost collection
            records = await self._get_records(collection='app.bsky.feed.repost', repo=my_did)

            # Find the repost record for this specific post
            for record in records:
                if hasattr(record, 'value') and hasattr(record.value, 'subject'):
                    if record.value.subject.uri == uri:
                        return await self.delete_repost(uri=record.uri)

                print("Could not find repost record to delete")
                return False

        except AtProtocolError as e:
            print(f"Failed to undo repost: {e}")
            return False

    @auth_required
    async def delete_repost(self, uri: str) -> bool:
        """
        Delete a repost via repost URI.

        Args:
            uri (str): URI of repost to delete

        Returns:
            bool: True if successful
        """

        uri_parts = self._uri_parts(uri)

        try:
            await self.client.app.bsky.feed.repost.delete(repo=uri_parts['repo_did'], rkey=uri_parts['rkey'])
            print(f"Deleted repost: {uri}")
            return True
        except (AttributeError, AtProtocolError) as e:
            print(f"Built-in delete failed: {e}")
            return False

    @auth_required
    async def read_notifications(self) -> bool:
        """
        Mark all current notifications as read

        Returns:
            bool: True if successful
        """

        latest_time = datetime.strftime(datetime.now(timezone.utc), '%Y-%m-%dT%H:%M:%SZ')
        result = await self.client.app.bsky.notification.update_seen({
            'seen_at': latest_time
        })
        return result


    # Update preferences

    @auth_required
    async def save_feed(self, uri: str, pin: bool = False) -> bool:
        """
        Add feed or list to list of saved feeds

        Args:
            uri (str): URI of feed/list to save
            pin (bool): If true, saves feed to pinned feeds

        Returns:
            bool: True if successful
        """

        try:
            p = await self.client.app.bsky.actor.get_preferences()
            prefs = p.preferences
            new_prefs = []
            for pref in prefs:
                if 'app.bsky.actor.defs#savedFeedsPref' in getattr(pref, 'py_type', ''):

                    # check if feed already saved
                    for feed in pref.items:
                        if feed.value == uri:
                            print(f'Feed "{uri}" is already saved')
                            return False

                    uri_parts = self._uri_parts(uri)
                    saved_feed = models.AppBskyActorDefs.SavedFeed(
                        id=f'{uri_parts['repo_did'].split(':')[-1]}{uri_parts['rkey']}',
                        pinned=pin,
                        type='list' if 'app.bsky.graph.list' in uri else 'feed',
                        value=uri,
                    )

                    pref.items.append(saved_feed)

                new_prefs.append(pref)

            result = await self.client.app.bsky.actor.put_preferences(
                models.AppBskyActorPutPreferences.Data(preferences=new_prefs)
            )

            return result

        except Exception as e:
            print(f"Error updating saved feed preferences: {e}")
            return False

    @auth_required
    async def remove_saved_feed(self, uri: str) -> bool:
        """
        Remove saved feed

        Args:
            uri (str): URI of feed to remove

        Returns:
            bool: True if successful
        """

        try:
            p = await self.client.app.bsky.actor.get_preferences()
            prefs = p.preferences
            new_prefs = []
            for pref in prefs:
                if 'app.bsky.actor.defs#savedFeedsPref' in getattr(pref, 'py_type', ''):
                    found = False
                    saved_feeds = []
                    for feed in pref.items:
                        if feed.value == uri:
                            found = True
                        else:
                            saved_feeds.append(feed)
                    pref.items = saved_feeds
                new_prefs.append(pref)

            if found:
                result = await self.client.app.bsky.actor.put_preferences(
                    models.AppBskyActorPutPreferences.Data(preferences=new_prefs)
                )
                return result

            else:
                print(f'Could not find feed "{uri}" in saved feeds')
                return False

        except Exception as e:
            print(f"Error updating saved feed preferences: {e}")
            return False

    @auth_required
    async def pin_saved_feed(self, uri: str) -> bool:
        """
        Pin saved feed

        Args:
            uri (str): URI of saved feed to pin

        Returns:
            bool: True if successful
        """

        try:
            p = await self.client.app.bsky.actor.get_preferences()
            prefs = p.preferences
            new_prefs = []
            for pref in prefs:
                if 'app.bsky.actor.defs#savedFeedsPref' in getattr(pref, 'py_type', ''):
                    found = False
                    saved_feeds = []
                    for feed in pref.items:
                        if feed.value == uri:
                            found = True
                            if feed.pinned:
                                print(f'Feed "{uri}" is already pinned')
                                return False
                            else:
                                feed.pinned = True
                        saved_feeds.append(feed)
                    pref.items = saved_feeds
                new_prefs.append(pref)

            if found:
                result = await self.client.app.bsky.actor.put_preferences(
                    models.AppBskyActorPutPreferences.Data(preferences=new_prefs)
                )
                return result

            else:
                print(f'Could not find feed "{uri}" in saved feeds')
                return False

        except Exception as e:
            print(f"Error updating saved feed preferences: {e}")
            return False

    @auth_required
    async def unpin_feed(self, uri: str) -> bool:
        """
        Unpin a pinned feed. Feed will stay in saved feeds.

        Args:
            uri (str): URI of feed to unpin

        Returns:
            bool: True if successful
        """

        try:
            p = await self.client.app.bsky.actor.get_preferences()
            prefs = p.preferences
            new_prefs = []
            for pref in prefs:
                if 'app.bsky.actor.defs#savedFeedsPref' in getattr(pref, 'py_type', ''):
                    found = False
                    saved_feeds = []
                    for feed in pref.items:
                        if feed.value == uri:
                            found = True
                            if not feed.pinned:
                                print(f'Saved feed "{uri}" is not pinned')
                                return False
                            else:
                                feed.pinned = False
                        saved_feeds.append(feed)
                    pref.items = saved_feeds
                new_prefs.append(pref)

            if found:
                result = await self.client.app.bsky.actor.put_preferences(
                    models.AppBskyActorPutPreferences.Data(preferences=new_prefs)
                )
                return result

            else:
                print(f'Could not find feed "{uri}" in saved feeds')
                return False

        except Exception as e:
            print(f"Error updating saved feed preferences: {e}")
            return False


    # Retrieve data

    @auth_required
    async def get_timeline(self, limit: int = 20, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Fetch following timeline posts.

        Args:
            limit (int): Number of posts to fetch
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dicts
        """

        feed_id = 'following-timeline'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'limit': limit},
                id_extractor=lambda response: f'{response.post.uri}{response.reason.by.handle if hasattr(response, 'reason') and hasattr(response.reason, 'by') else ''}',
                api_method=self.client.app.bsky.feed.get_timeline,
                response_data_field='feed'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            posts = []
            for response in feed:
                result = await self._build_feed_item(response.post, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents, reason=response.reason)
                posts.append(result)

            return posts

        except Exception as e:
            print(f"Error fetching timeline: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_feed(self, uri: str, limit: int = 20, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Fetch custom feed posts.

        Args:
            uri (str): URI of feed
            limit (int): Number of posts to fetch
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dicts
        """

        feed_id = f'feed-{uri}'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'feed': uri, 'limit': limit},
                id_extractor=lambda response: response.post.uri,
                api_method=self.client.app.bsky.feed.get_feed,
                response_data_field='feed'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            posts = []
            for response in feed:
                result = await self._build_feed_item(response.post, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents, reason=response.reason)
                posts.append(result)

            return posts

        except Exception as e:
            print(f"Failed to get feed: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_list_feed(self, uri: str, limit: int = 20, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Fetch list feed posts.

        Args:
            uri (str): URI of list
            limit (int): Number of posts to fetch
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dicts
        """

        feed_id = f'list-{uri}'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'list': uri, 'limit': limit},
                id_extractor=lambda response: response.post.uri,
                api_method=self.client.app.bsky.feed.get_list_feed,
                response_data_field='feed'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            posts = []
            for response in feed:
                result = await self._build_feed_item(response.post, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents, reason=response.reason)
                posts.append(result)

            return posts

        except Exception as e:
            print(f"Failed to get list feed: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_thread(self, uri: str, limit: int | None = 20, max_depth: int = 10, parent_height: int = 10, tree_mode: bool = False) -> dict:
        """
        Get a post thread with replies organized hierarchically.

        Args:
            uri (str): URI of the post to get thread for
            limit (int or None): Number of posts to retrieve at given depth level. If tree_mode is False, will only use for depth level 1. Note: this will only limit reply reponses after they are received from the API. Default is 20
            max_depth (int): Maximum depth to traverse. Max depth for API call is 10
            parent_height (int): Maximum number of parent posts to retrieve. Default is 10
            tree_mode (bool): If True, respects limit at every depth level; if False, uses limit only for top level and max 1 for deeper levels. Default is False

        Returns:
            dict: Dictionary with post thread information
        """

        def _sort_replies(replies: list[dict], parent_author_handle: str, op_handle: str) -> list[dict]:
            """Sort replies in order of parent author, OP author, root author, default ordering"""
            parent_replies = []
            op_replies = []
            other_replies = []

            for reply in replies:
                author_handle = reply.post.author.handle
                if author_handle == parent_author_handle:
                    parent_replies.append(reply)
                elif author_handle == op_handle:
                    op_replies.append(reply)
                else:
                    other_replies.append(reply)

            return parent_replies + op_replies + other_replies

        async def _extract_parent_chain(thread_view: models.AppBskyFeedDefs.ThreadViewPost, max_parents: int = 10) -> list[dict]:
            """Extract parent posts up to max_parents limit."""
            parents = []
            current = thread_view

            # Traverse up the parent chain
            while getattr(current, 'parent', None) and len(parents) < max_parents:

                # check if parent is a deleted or blocked post
                if getattr(current.parent, 'not_found', None):
                    deleted = await self.is_post_deleted(current.parent.uri)
                    if deleted:
                        parent_info = {
                            'uri': current.parent.uri,
                            'is_deleted_post': True,
                        }
                    else:
                        parent_info = {
                            'uri': current.parent.uri,
                            'is_blocked_post': True,
                        }
                    parents.append(parent_info)
                    break

                else:
                    parent_info = await self._build_feed_item(current.parent.post, extract_reply_parents=False)
                    parents.append(parent_info)
                    current = current.parent

            return parents[::-1]

        async def _process_thread_recursive(thread_view: models.AppBskyFeedDefs.ThreadViewPost, current_depth: int, op_handle: str, parent_author_handle: str | None = None):
            """Recursively process thread replies."""
            if current_depth > max_depth:
                return []

            if not hasattr(thread_view, 'replies') or not thread_view.replies:
                return []

            # Determine reply limit for current depth
            if tree_mode or current_depth == 0:
                reply_limit = limit
            else:
                reply_limit = 1

            # Sort replies according to priority
            sorted_replies = _sort_replies(
                thread_view.replies,
                parent_author_handle or thread_view.post.author.handle,
                op_handle
            )

            processed_replies = []
            limited_replies = sorted_replies[:reply_limit] if reply_limit is not None else sorted_replies
            for reply in limited_replies:
                if not hasattr(reply, 'post') or not reply.post:
                    continue

                reply_info = await self._build_feed_item(reply.post, extract_reply_parents=False)

                # Recursively process nested replies
                reply_info['thread_replies'] = await _process_thread_recursive(
                    reply,
                    current_depth + 1,
                    op_handle,
                    reply.post.author.handle
                )

                processed_replies.append(reply_info)

            return processed_replies

        try:
            response = await self.client.app.bsky.feed.get_post_thread({
                'uri': uri,
                'depth': min(max_depth, 10),
            })

            if not response.thread or not hasattr(response.thread, 'post'):
                return None

            # Extract main post info
            main_post = await self._build_feed_item(response.thread.post, extract_reply_parents=False)

            # Get parents
            main_post['thread_parents'] = await _extract_parent_chain(
                thread_view=response.thread,
                max_parents=parent_height,
            ) if parent_height > 0 else []

            # Get replies
            main_post['thread_replies'] = await _process_thread_recursive(
                thread_view=response.thread,
                current_depth=0,
                op_handle=response.thread.post.author.handle
            )

            return main_post

        except Exception as e:
            print(f"Error fetching thread: {e}")
            return []

    @auth_required
    async def get_user_posts(self, handle: str | None = None, post_type: str = 'posts_with_replies', limit: int = 20, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get posts from a specific user's timeline.

        Args:
            handle (str, optional): User's handle  or DID
            post_type (str): Type of posts to include. Default is 'post_with_replies'. Valid options: 'posts_with_replies', 'posts_no_replies', 'posts_with_media', 'posts_and_author_threads', 'posts_with_video'
            limit (int): Number of posts to retrieve (default: 50, max: 100)
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dicts
        """
        try:
            # Get the target user's DID
            if handle:
                if handle.startswith('@'): handle = handle[1:]
                profile = await self.get_profile(handle)
                target_did = profile['did']

            else:
                target_did = self.client.me.did

            init_params = {'actor': target_did, 'include_pins': True, 'filter': post_type}
            feed_id = f'user-{hash(frozenset(init_params.items()))}'
            init_params['limit'] = limit
            if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
                self.paginator = FeedPaginator(
                    feed=feed_id,
                    params=init_params,
                    id_extractor=lambda response: response.post.uri,
                    api_method=self.client.app.bsky.feed.get_author_feed,
                    response_data_field='feed'
                )

            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            results = []
            for response in feed:

                result = await self._build_feed_item(response.post, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents, reason=response.reason)

                results.append(result)

            return results


        except Exception as e:
            print(f"Error fetching posts for {handle}: {e}")
            self.paginator.mark_error()
            return None

    @auth_required
    async def get_user_likes(self, handle: str | None = None, limit: int = 20, reverse_chronological: bool = True, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get liked posts by a specific user.

        Args:
            handle (str, optional): User's handle  or DID
            post_type (str): Type of posts to include. Default is 'post_with_replies'. Valid options: 'posts_with_replies', 'posts_no_replies', 'posts_with_media', 'posts_and_author_threads', 'posts_with_video'
            limit (int): Number of posts to retrieve (default: 50, max: 100)
            reverse_chronological (bool): If False, will start with first chronological likes. Defaults to True.
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dicts
        """

        async def _fetch_likes(params: dict):
            """
            Implement our own method for getting likes since atproto does not fetch likes for other users.

            Args:
                params (dict): Parameters to pass to the API (e.g. 'repo', 'limit', 'reverse', 'cursor'))

            Returns:
                list: List of like dicts
            """

            endpoint = "https://bsky.social/xrpc/com.atproto.repo.listRecords"
            params['collection'] = "app.bsky.feed.like"

            str_params = {k: str(v).lower() if isinstance(v, bool) else v for k, v in params.items() if v is not None}

            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint, params=str_params) as response:
                    return await response.json()

        try:
            if handle:
                if handle.startswith('@'): handle = handle[1:]

            else:
                handle = self.handle

            feed_id = f'liked-by-{handle}{'' if reverse_chronological else '-reverse'}'
            if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
                self.paginator = FeedPaginator(
                    feed=feed_id,
                    params={
                        'repo': handle,
                        'reverse': not reverse_chronological,
                        'limit': limit,
                    },
                    id_extractor=lambda like: like['value']['subject']['uri'],
                    api_method=_fetch_likes,
                    response_data_field='records'
                )

            records = await self.paginator.next_page() if not new_items else await self.paginator.new()

            results = []
            for like in records:
                result = await self.get_post_data(like['value']['subject']['uri'], extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents)

                results.append(result)

            return results

        except Exception as e:
            print(f"Error fetching likes for {handle}: {e}")
            self.paginator.mark_error()
            return None

    @auth_required
    async def search_posts(self, query: str, limit: int = 20, top_posts: bool = False, since: datetime | None = None, until: datetime | None = None, language: str | None = None, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Search for posts.

        Args:
            query (str): Search query
            limit (int): Number of results to return
            top_posts (bool): Whether to query 'top' posts. Defaults to False (queries 'latest' posts)
            since (Datetime): Query posts after this date. Defaults to None.
            until (Datetime): Query posts before this date. Defaults to None.
            language (str): Query posts in a specific language based on supplied shortcode, e.g. "en", "es", "fr". If no argument is supplied, results in any language will be returned.
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dicts
        """

        query_sort = 'top' if top_posts else 'latest'
        if since:
            since = datetime.strftime(since, '%Y-%m-%dT%H:%M:%SZ')
        if until:
            until = datetime.strftime(until, '%Y-%m-%dT%H:%M:%SZ')
        init_params = {
            'q': query,
            'sort': query_sort,
            'since': since,
            'until': until,
            'lang': language,
        }
        feed_id = f'query-{hash(frozenset(init_params.items()))}'
        init_params['limit'] = limit
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params=init_params,
                id_extractor=lambda post: post.uri,
                api_method=self.client.app.bsky.feed.search_posts,
                response_data_field='posts'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            posts = []
            for post in feed:
                result = await self._build_feed_item(post, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents)
                posts.append(result)

            return posts

        except Exception as e:
            print(f"Search failed: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def search_users(self, query: str, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Search for users.

        Args:
            query (str): Search query
            limit (int): Number of results to return
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of user dicts
        """

        feed_id = f'query-users-{query}'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'q': query, 'limit': limit},
                id_extractor=lambda actor: actor.handle,
                api_method=self.client.app.bsky.actor.search_actors,
                response_data_field='actors'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            users = []
            for actor in feed:
                user = await self.get_profile(actor.handle)
                users.append(user)

            return users

        except Exception as e:
            print(f"Search failed: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def search_feeds(self, query: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Search for custom feeds.

        Args:
            query (str, optional): Search query. If no query is provided, will return suggested feeds
            limit (int): Number of results to return
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of user dicts
        """

        feed_id = f'feeds-{query if query is not None else 'suggested'}'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'query': query, 'limit': limit},
                id_extractor=lambda feed: feed.uri,
                api_method=self.client.app.bsky.unspecced.get_popular_feed_generators,
                response_data_field='feeds'
            )

        try:
            feed_feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            feeds = []
            for feed in feed_feed:
                item = {
                    'uri': feed.uri,
                    'cid': feed.cid,
                    'display_name': feed.display_name,
                    'avatar': feed.avatar,
                    'description': feed.description,
                    'like_count': feed.like_count,
                    'liked': feed.viewer.like, # uri or None
                    'creator': {
                        'did': feed.creator.did,
                        'handle': feed.creator.handle,
                        'display_name': feed.creator.display_name,
                        'avatar': feed.creator.avatar,
                        'description': feed.creator.description,
                    }
                }
                feeds.append(item)

            return feeds

        except Exception as e:
            print(f"Search failed: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_saved_feeds(self, only_pinned: bool = False, get_feed_data: bool = True, include_timeline: bool = True) -> list[dict] | None:
        """
        Get saved feeds.

        Args:
            only_pinned (bool): If true, only include pinned feeds. Defaults to false.
            get_feed_data (bool): If true, fetch full feed information using feed URI. Defaults to true.
            include_timeline (bool): If true, include following timeline in results. Defaults to true.

        Returns:
            list: List of saved feed dicts.

        """
        try:
            p = await self.client.app.bsky.actor.get_preferences()
            prefs = p.preferences
            feeds = []
            for pref in prefs:
                if 'app.bsky.actor.defs#savedFeedsPref' in getattr(pref, 'py_type', ''):
                    for i in pref.items:
                        if i.type not in ['feed', 'list', 'timeline']: continue
                        if not include_timeline and i.type == 'timeline': continue
                        if only_pinned and not i.pinned: continue
                        item = {
                            'id': i.id,
                            'pinned': i.pinned,
                            'type': i.type,
                            'uri': i.value if i.type != 'timeline' else None,
                        }
                        if get_feed_data:
                            if item['type'] == 'feed':
                                item['feed'] = await self.get_feed_data(item['uri'])
                            elif item['type'] == 'list':
                                item['feed'] = await self.get_list_data(item['uri'])
                            else:
                                item['feed'] = None
                        feeds.append(item)
            return feeds

        except Exception as e:
            print(f"Error getting saved feeds: {e}")
            return None

    @auth_required
    async def is_feed_saved(self, uri: str) -> bool | None:
        """
        Checks whether feed URI is in saved feeds

        Args:
            uri (str): URI of feed to check

        Returns:
            bool: True if saved
        """

        try:
            p = await self.client.app.bsky.actor.get_preferences()
            prefs = p.preferences
            for pref in prefs:
                if 'app.bsky.actor.defs#savedFeedsPref' in getattr(pref, 'py_type', ''):
                    for feed in pref.items:
                        if feed.value == uri:
                            return True
            return False

        except Exception as e:
            print(f"Error getting saved feeds: {e}")
            return None

    @auth_required
    async def get_feed_data(self, uri: str) -> dict | None:
        """
        Get detailed information about a feed from URI.

        Args:
            uri (str): The URI of the feed

        Returns:
            dict: Dictionary containing feed information or None if not found

        """
        try:
            response = await self.client.app.bsky.feed.get_feed_generators({'feeds':[uri]})

            if not response.feeds or len(response.feeds) == 0:
                print(f"Feed not found: {uri}")
                return None

            feed = response.feeds[0]

            item = {
                'uri': feed.uri,
                'cid': feed.cid,
                'display_name': feed.display_name,
                'avatar': feed.avatar,
                'description': feed.description,
                'like_count': feed.like_count,
                'liked': feed.viewer.like,
                'creator': {
                    'did': feed.creator.did,
                    'handle': feed.creator.handle,
                    'display_name': feed.creator.display_name,
                    'avatar': feed.creator.avatar,
                    'description': feed.creator.description,
                }
            }
            return item

        except Exception as e:
            print(f"Error getting feed info for {uri}: {e}")
            return None

    @auth_required
    async def get_list_data(self, uri: str) -> dict | None:
        """
        Get detailed information about a list from URI. (Does not include users, use get_list_people to get users of a list.)

        Args:
            uri (str): The URI of the list

        Returns:
            dict: Dictionary containing list information or None if not found

        """
        try:
            response = await self.client.app.bsky.graph.get_list({'list':uri, 'limit': 1})

            if not response.list:
                print(f"List not found: {uri}")
                return None


            list_data = response.list

            item = {
                'uri': list_data.uri,
                'cid': list_data.cid,
                'display_name': list_data.name,
                'avatar': list_data.avatar,
                'description': list_data.description,
                'item_count': list_data.list_item_count,
                'creator': {
                    'did': list_data.creator.did,
                    'handle': list_data.creator.handle,
                    'display_name': list_data.creator.display_name,
                    'avatar': list_data.creator.avatar,
                    'description': list_data.creator.description,
                }
            }
            return item

        except Exception as e:
            print(f"Error getting feed info for {uri}: {e}")
            return None

    @auth_required
    async def get_list_people(self, uri: str, limit: int = 100, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get users included in a given list.

        Args:
            uri (str): The URI of the list
            limit (int): Number of results to return
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of dictionaries containing user information

        """

        feed_id = f'list-people-{uri}'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'list': uri, 'limit': limit},
                id_extractor=lambda user: user.subject.did,
                api_method=self.client.app.bsky.graph.get_list,
                response_data_field='items'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            list_people = []
            for user in feed:
                list_people.append({
                    'did': user.subject.did,
                    'handle': user.subject.handle,
                    'displayName': getattr(user.subject, 'displayName', None),
                    'avatar': getattr(user.subject, 'avatar', None),
                    'description': getattr(user.subject, 'description', None),
                    'created_at': user.subject.created_at,

                    'muted': user.subject.viewer.muted,
                    'mute_list': user.subject.viewer.muted_by_list,
                    'blocking': user.subject.viewer.blocking,
                    'blocking_by_list': user.subject.viewer.blocking_by_list,
                    'blocked_by': user.subject.viewer.blocked_by,
                    'following': user.subject.viewer.following,
                    'followed_by': user.subject.viewer.followed_by,
                })

            return list_people

        except Exception as e:
            print(f"Error getting list users: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_user_lists(self, handle: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get lists created by a given user

        Args:
            handle (str, optional): User handle. If no handle is provided, will return own created lists.
            limit (int): Number of results to return
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of list dicts
        """

        if not handle: handle = self.handle
        feed_id = f'{handle}-lists'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'actor': handle, 'limit': limit},
                id_extractor=lambda list_item: list_item.uri,
                api_method=self.client.app.bsky.graph.get_lists,
                response_data_field='lists'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            lists = []
            for list_item in feed:
                item = {
                    'uri': list_item.uri,
                    'cid': list_item.cid,
                    'display_name': list_item.name,
                    'avatar': list_item.avatar,
                    'description': list_item.description,
                    'item_count': list_item.list_item_count,
                    'creator': {
                        'did': list_item.creator.did,
                        'handle': list_item.creator.handle,
                        'display_name': list_item.creator.display_name,
                        'avatar': list_item.creator.avatar,
                        'description': list_item.creator.description,
                    }
                }
                lists.append(item)

            return lists

        except Exception as e:
            print(f"Error getting user lists: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_user_starter_packs(self, handle: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get starter packs created by a given user

        Args:
            handle (str, optional): User handle. If no handle is provided, will return own created lists.
            limit (int): Number of results to return
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of starter pack dicts
        """

        if not handle: handle = self.handle
        feed_id = f'{handle}-starter-packs'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'actor': handle, 'limit': limit},
                id_extractor=lambda starter_pack: starter_pack.uri,
                api_method=self.client.app.bsky.graph.get_actor_starter_packs,
                response_data_field='starter_packs'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            starter_packs = []
            for sp in feed:
                item = {
                    'uri': sp.uri,
                    'cid': sp.cid,
                    'display_name': sp.record.name,
                    'list_uri': sp.record.list,
                    'description': sp.record.description,
                    'joined_count': sp.joined_all_time_count,
                    'creator': {
                        'did': sp.creator.did,
                        'handle': sp.creator.handle,
                        'display_name': sp.creator.display_name,
                        'avatar': sp.creator.avatar,
                    }
                }
                starter_packs.append(item)

            return starter_packs

        except Exception as e:
            print(f"Error getting user lists: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_suggested_starter_packs(self) -> list[dict]:
        """
        Get suggested starter packs

        Returns:
            list: List of 3 suggested starter pack dicts
        """

        try:
            response = await self.client.app.bsky.unspecced.get_suggested_starter_packs()
            feed = response.starter_packs

            starter_packs = []
            for sp in feed:
                item = {
                    'uri': sp.uri,
                    'cid': sp.cid,
                    'display_name': sp.record.name,
                    'list_uri': sp.record.list,
                    'description': sp.record.description,
                    'joined_count': sp.joined_all_time_count,
                    'creator': {
                        'did': sp.creator.did,
                        'handle': sp.creator.handle,
                        'display_name': sp.creator.display_name,
                        'avatar': sp.creator.avatar,
                    }
                }
                starter_packs.append(item)

            return starter_packs

        except Exception as e:
            print(f"Error getting suggested starter packs: {e}")
            return []

    @auth_required
    async def get_post_data(self, uri: str, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True) -> dict | None:
        """
        Get detailed data from individual post using uri.

        Args:
            uri (str): Post URI
            extract_media (bool): If True, attempts to extract media content from the object. Defaults to True.
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to True.

        Returns:
            dict: dict of post data
        """

        try:

            response = await self.client.app.bsky.feed.get_posts({'uris': [uri]})

            if len(response.posts) == 0:
                deleted = await self.is_post_deleted(uri)
                if deleted:
                    return {
                        'uri': uri,
                        'is_deleted_post': True,
                    }
                else:
                    return {
                        'uri': uri,
                        'is_blocked_post': True,
                    }
            else:
                response=response.posts[0]

            result = await self._build_feed_item(response, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents)

            return result

        except Exception as e:
            print(f"Failed to get post data for {uri}: {e}")
            return None

    @auth_required
    async def get_likes(self, uri: str, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of users that have liked a given post.

        Args:
            uri (str): URI of post
            limit (int): Maximum number of users to return.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of user dictionaries
        """


        feed_id = f'{uri}-likers'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'uri': uri, 'limit': limit},
                id_extractor=lambda like: like.actor.did,
                api_method=self.client.app.bsky.feed.get_likes,
                response_data_field='likes'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            likes = []
            for like in feed:
                item = {
                    'did': like.actor.did,
                    'handle': like.actor.handle,
                    'display_name': like.actor.display_name,
                    'created_at': like.actor.created_at,
                    'avatar': getattr(like.actor, 'avatar', None),
                    'banner': getattr(like.actor, 'banner', None),
                    'description': getattr(like.actor, 'description', None),
                    'following': like.actor.viewer.following,
                    'followed_by': like.actor.viewer.followed_by,
                    'muted': like.actor.viewer.muted,
                    'mute_list': like.actor.viewer.muted_by_list,
                    'blocking': like.actor.viewer.blocking,
                    'blocking_by_list': like.actor.viewer.blocking_by_list,
                    'blocked_by': like.actor.viewer.blocked_by,
                }
                likes.append(item)
            return likes

        except Exception as e:
            print(f"Failed to get likes: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_reposts(self, uri: str, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of users that have reposted a given post.

        Args:
            uri (str): URI of post
            limit (int): Maximum number of users to return.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of user dictionaries
        """


        feed_id = f'{uri}-reposters'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'uri': uri, 'limit': limit},
                id_extractor=lambda repost: repost.did,
                api_method=self.client.app.bsky.feed.get_reposted_by,
                response_data_field='reposted_by'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            reposts = []
            for repost in feed:
                item = {
                    'did': repost.did,
                    'handle': repost.handle,
                    'display_name': repost.display_name,
                    'created_at': repost.created_at,
                    'avatar': getattr(repost, 'avatar', None),
                    'banner': getattr(repost, 'banner', None),
                    'description': getattr(repost, 'description', None),
                    'following': repost.viewer.following,
                    'followed_by': repost.viewer.followed_by,
                    'muted': repost.viewer.muted,
                    'mute_list': repost.viewer.muted_by_list,
                    'blocking': repost.viewer.blocking,
                    'blocking_by_list': repost.viewer.blocking_by_list,
                    'blocked_by': repost.viewer.blocked_by,
                }
                reposts.append(item)
            return reposts

        except Exception as e:
            print(f"Failed to get reposts: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_quotes(self, uri: str, limit: int = 20, extract_media: bool = True, media_types: list[str]= [], include_quoted_media: bool = True, quote_nesting: int = 1, extract_reply_parents: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of quote posts of a given post.

        Args:
            uri (str): URI of post
            limit (int): Maximum number of posts to return.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of post dictionaries
        """


        feed_id = f'{uri}-quotes'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:

            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'uri': uri, 'limit': limit},
                id_extractor=lambda post: post.uri,
                api_method=self.client.app.bsky.feed.get_quotes,
                response_data_field='posts'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            posts = []
            for post in feed:
                result = await self._build_feed_item(post, extract_media=extract_media, media_types=media_types, include_quoted_media=include_quoted_media, quote_nesting=quote_nesting, extract_reply_parents=extract_reply_parents)
                posts.append(result)

            return posts

        except Exception as e:
            print(f"Failed to get quotes: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_profile(self, handle: str | None = None) -> dict | None:
        """
        Get profile information.

        Args:
            handle (str, optional): Handle to get profile for (defaults to own profile)

        Returns:
            dict: Profile dictionary or None if failed
        """
        target_handle = handle or self.handle
        if not target_handle:
            print("No handle specified")
            return None

        try:
            profile = await self.client.get_profile(target_handle)

            verification = None
            if profile.verification:
                if profile.verification.trusted_verifier_status == 'valid':
                    verification = 'verifier'
                elif profile.verification.verified_status == 'valid':
                    verification = 'verified'

            return {
                'did': profile.did,
                'handle': profile.handle,
                'display_name': profile.display_name,
                'description': profile.description,
                'avatar': profile.avatar,
                'banner': profile.banner,
                'followers_count': profile.followers_count,
                'follows_count': profile.follows_count,
                'posts_count': profile.posts_count,
                'created_at': profile.created_at,
                'verification': verification,
                'known_followers_count': profile.viewer.known_followers.count if profile.viewer.known_followers is not None else 0,
                'following': profile.viewer.following,
                'followed_by': profile.viewer.followed_by,
                'muted': profile.viewer.muted,
                'mute_list': profile.viewer.muted_by_list,
                'blocking': profile.viewer.blocking,
                'blocking_by_list': profile.viewer.blocking_by_list,
                'blocked_by': profile.viewer.blocked_by,
                'labels': [
                    {
                        'label': label.val,
                        'labeler': label.src,
                    } for label in profile.labels
                ],
            }

        except AtProtocolError as e:
            print(f"Failed to get profile: {e}")
            return None

    @auth_required
    async def get_follows(self, handle: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of users that are being followed.

        Args:
            handle (str, optional): Handle to get follows for (defaults to current user)
            limit (int): Maximum number of follows to return.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of follower dictionaries
        """


        feed_id = f'{handle if handle is not None else 'my'}-follows'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'actor': handle or self.handle, 'limit': limit},
                id_extractor=lambda follow: follow.did,
                api_method=self.client.app.bsky.graph.get_follows,
                response_data_field='follows'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            follows = []
            for follow in feed:
                item = {
                    'did': follow.did,
                    'handle': follow.handle,
                    'display_name': follow.display_name,
                    'created_at': follow.created_at,
                    'avatar': getattr(follow, 'avatar', None),
                    'banner': getattr(follow, 'banner', None),
                    'description': getattr(follow, 'description', None),
                    'following': follow.viewer.following,
                    'followed_by': follow.viewer.followed_by,
                    'muted': follow.viewer.muted,
                    'mute_list': follow.viewer.muted_by_list,
                    'blocking': follow.viewer.blocking,
                    'blocking_by_list': follow.viewer.blocking_by_list,
                    'blocked_by': follow.viewer.blocked_by,
                }
                follows.append(item)
            return follows

        except Exception as e:
            print(f"Failed to get followers: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_follows_detailed(self, handle: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of users that are being followed with detailed info, including follow + post metrics.

        Args:
            handle (str, optional): Handle to get follows for (defaults to current user)
            limit (int): Maximum number of follows to return. Note: suspended accounts will not appear in results but will count towards the limit
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of follower profile dictionaries
        """

        follows = await self.get_follows(handle=handle, limit=limit, new_items=new_items, reset_pagination=reset_pagination)
        follows_detailed = [await self.get_profile(f['handle']) for f in follows]
        return follows_detailed

    @auth_required
    async def get_followers(self, handle: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of followers.

        Args:
            handle (str, optional): Handle to get followers for (defaults to current user)
            limit (int): Maximum number of followers to return. Note: suspended accounts will not appear in results but will count towards the limit
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of follower dictionaries
        """


        feed_id = f'{handle if handle is not None else 'my'}-followers'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'actor': handle or self.handle, 'limit': limit},
                id_extractor=lambda follower: follower.did,
                api_method=self.client.app.bsky.graph.get_followers,
                response_data_field='followers'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            followers = []
            for follower in feed:
                item = {
                    'did': follower.did,
                    'handle': follower.handle,
                    'display_name': follower.display_name,
                    'created_at': follower.created_at,
                    'avatar': getattr(follower, 'avatar', None),
                    'banner': getattr(follower, 'banner', None),
                    'description': getattr(follower, 'description', None),
                    'following': follower.viewer.following,
                    'followed_by': follower.viewer.followed_by,
                    'muted': follower.viewer.muted,
                    'mute_list': follower.viewer.muted_by_list,
                    'blocking': follower.viewer.blocking,
                    'blocking_by_list': follower.viewer.blocking_by_list,
                    'blocked_by': follower.viewer.blocked_by,
                }
                followers.append(item)
            return followers

        except Exception as e:
            print(f"Failed to get followers: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_followers_detailed(self, handle: str | None = None, limit: int = 20, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get list of followers with detailed info, including follow + post metrics.

        Args:
            handle (str): Handle to get followers for (defaults to current user)
            limit (int): Maximum number of followers to return. Note: suspended accounts will not appear in results but will count towards the limit
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of follower profile dictionaries
        """

        followers = await self.get_followers(handle=handle, limit=limit, new_items=new_items, reset_pagination=reset_pagination)
        followers_detailed = [await self.get_profile(f['handle']) for f in followers]
        return followers_detailed

    @auth_required
    async def get_mute_list(self, limit: int = 100, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """Get list of muted accounts.

        Args:
            limit (int): Maximum number of accounts to return.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of dictionaries containing account and viewer information
        """

        feed_id = 'mute-list'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'limit': limit},
                id_extractor=lambda user: user.did,
                api_method=self.client.app.bsky.graph.get_mutes,
                response_data_field='mutes'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            muted_accounts = []
            for mute in feed:
                muted_accounts.append({
                    'did': mute.did,
                    'handle': mute.handle,
                    'displayName': getattr(mute, 'displayName', None),
                    'avatar': getattr(mute, 'avatar', None),
                    'description': getattr(mute, 'description', None),
                    'created_at': mute.created_at,

                    'muted': mute.viewer.muted, # True or False
                    'mute_list': mute.viewer.muted_by_list, # URI or None
                    'blocking': mute.viewer.blocking, # URI or None
                    'blocking_by_list': mute.viewer.blocking_by_list, # URI or None
                    'blocked_by': mute.viewer.blocked_by, # True or False (whether this user is blocking you)
                    'following': mute.viewer.following,
                    'followed_by': mute.viewer.followed_by,
                })

            return muted_accounts

        except Exception as e:
            print(f"Error getting mute list: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_block_list(self, limit: int = 100, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """Get list of blocked accounts.

        Args:
            limit (int): Maximum number of accounts to return.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of dictionaries containing account and viewer information
        """

        feed_id = 'block-list'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'limit': limit},
                id_extractor=lambda user: user.did,
                api_method=self.client.app.bsky.graph.get_blocks,
                response_data_field='blocks'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            blocked_accounts = []
            for block in feed:
                blocked_accounts.append({
                    'did': block.did,
                    'handle': block.handle,
                    'displayName': getattr(block, 'displayName', None),
                    'avatar': getattr(block, 'avatar', None),
                    'description': getattr(block, 'description', None),
                    'created_at': block.created_at,

                    'blocking': block.viewer.blocking, # URI or None
                    'blocking_by_list': block.viewer.blocking_by_list, # URI or None
                    'blocked_by': block.viewer.blocked_by, # True or False (whether this user is blocking you)
                    'muted': block.viewer.muted, # True or False
                    'mute_list': block.viewer.muted_by_list, # URI or None
                    'following': block.viewer.following,
                    'followed_by': block.viewer.followed_by,
                })

            return blocked_accounts

        except Exception as e:
            print(f"Error getting block list: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_label_visibility_prefs(self) -> dict:
        """
        Get moderation label visibility preferences.

        Returns:
            dict: Dictionary of label content preferences.
        """

        prefs = await self.client.app.bsky.actor.get_preferences()

        label_prefs = {}
        for pref in prefs.preferences:
            if getattr(pref, 'py_type', '') == 'app.bsky.actor.defs#contentLabelPref':
                label_prefs[pref.label]={
                    'labeler_did': pref.labeler_did,
                    'visibility': pref.visibility,
                }
        return label_prefs

    @auth_required
    async def get_adult_enabled(self) -> bool:
        """
        Get moderation setting for adult content.

        Returns:
            bool: True if adult content enabled
        """

        prefs = await self.client.app.bsky.actor.get_preferences()

        for pref in prefs.preferences:
            if getattr(pref, 'py_type', '') == 'app.bsky.actor.defs#adultContentPref':
                return pref.enabled

        return None

    @auth_required
    async def get_subscribed_labelers(self, detailed: bool = False) -> list:
        """
        Get data and policies definition for subscribed labelers

        Returns:
            list: List of dictionaries containing subscribed labeler information and policies
        """
        prefs = await self.client.app.bsky.actor.get_preferences()
        labeler_dids = self.default_labelers[:]
        for pref in prefs.preferences:
            if hasattr(pref, 'labelers'):
                for l in pref.labelers:
                    labeler_dids.append(l.did)

        if detailed:
            labelers = [await self.get_labeler_data(label_did) for label_did in labeler_dids]
            return labelers
        else:
            return labeler_dids

    @auth_required
    async def get_labeler_data(self, did: str) -> dict:
        """
        Get detailed data for a labeler

        Args:
            did (str): The labeler's DID identifier

        Returns:
            dict: Dictionary containing labeler information and policies
        """
        labeler = await self.client.app.bsky.labeler.get_services(params={'dids': [did], 'detailed': True})
        item = {
            'uri': labeler.views[0].uri,
            'like_count': labeler.views[0].like_count,
            'policies': self._unpack_label_policy_defs(labeler.views[0].policies.label_value_definitions),
            'creator': {
                'did': labeler.views[0].creator.did,
                'handle': labeler.views[0].creator.handle,
                'display_name': labeler.views[0].creator.display_name,
                'avatar': labeler.views[0].creator.avatar,
                'description': labeler.views[0].creator.description,
            }
        }
        return item

    @staticmethod
    def _unpack_label_policy_defs(label_defs: list, preferred_lang: str = 'en'):
        """
        Convert label defintions to dictionary

        Args:
            label_defs (list): list containing LabelValueDefinition obects
            preferred_lang (str): preferred language if descriptions in multiple languages are provided. Defaults to 'en' (English)

        Returns:
            dict: Dictionary containing label defintions
        """
        result = {}
        for label_def in label_defs:
            locale = [l for l in label_def.locales if getattr(l, 'lang') == preferred_lang]
            description = locale[0].description if locale else label_def.locales[0].description
            result[label_def.identifier] = {
                'blurs': label_def.blurs,
                'description': description,
                'severity': label_def.severity,
                'adult_only': label_def.adult_only,
                'default_setting': label_def.default_setting,
            }
        return result

    @staticmethod
    def global_policies() -> dict:
        """
        Dictionary of hard-coded content policies with default options.

        Returns:
            dict: Dictionary of global policies
        """
        return {
            'porn': {
                'blurs': 'media',
                'severity': 'alert',
                'adult_only': True,
                'default_setting': 'warn',
                'description': 'Explicit sexual images.'
            },
            'sexual': {
                'blurs': 'media',
                'severity': 'alert',
                'adult_only': True,
                'default_setting': 'warn',
                'description': 'Does not include nudity.'
            },
            'graphic-media': {
                'blurs': 'media',
                'severity': 'alert',
                'adult_only': True,
                'default_setting': 'warn',
                'description': 'Explicit or potentially disturbing media.'
            },
            'nudity': {
                'blurs': 'media',
                'severity': 'inform',
                'adult_only': False,
                'default_setting': 'ignore',
                'description': 'E.g. artistic nudes.'
            },
            '!hide': {
                'blurs': 'content',
                'severity': 'none',
                'non_configurable': True,
                'default_setting': 'hide',
                'description': 'Generic warning on content that cannot be clicked through.'
            },
            '!warn': {
                'blurs': 'none',
                'severity': 'alert',
                'non_configurable': True,
                'default_setting': 'warn',
                'description': 'Generic warning on content but can be clicked through.'
            },
            '!no-unauthenticated': {
                'blurs': 'none',
                'severity': 'none',
                'non_configurable': True,
                'default_setting': 'ignore',
                'description': 'Makes the content inaccessible to logged-out users in applications which respect the label'
            },
        }

    @auth_required
    async def get_content_policies(self, include_subscribed_labelers: bool = True) -> dict:
        """
        Get label definitions with user's applied visibility settings

        Returns:
            dict: Dictionary of content policies
        """
        policies = self.global_policies()

        if include_subscribed_labelers:
            labelers = await self.get_subscribed_labelers(detailed=True)

        else:
            labelers = [await self.get_labeler_data(label_did) for label_did in self.default_labelers]

        for labeler in labelers:
            for name, policy in labeler['policies'].items():
                policies[name] = policy

        visibility_prefs = await self.get_label_visibility_prefs()

        adult_enabled = await self.get_adult_enabled()

        for policy_id, policy in policies.items():
            if not adult_enabled and policy['adult_only']:
                policy['visibility'] = 'hide'
            elif policy_id in visibility_prefs:
                policy['visibility'] = visibility_prefs[policy_id]['visibility']
            elif 'default_setting' in policy: # should always be true
                policy['visibility'] = policy['default_setting']

        return policies

    @auth_required
    async def query_labelers(self, targets: list[str], labelers: list[str] | None = None) -> dict:
        """
        Query URIs/DIDs with labeling services

        Args:
            targets (list): Post URIs and/or profile DIDs to query
            labelers (list, optional): list of labeler DIDs to query against. If None, will use subscribed labelers. Defaults to None

        Returns:
            dict: dict of label dictionaries with uri response as keys
        """
        if not labelers and not hasattr(self, 'subscribed_labelers'):
            subscribed_labelers = await self.get_subscribed_labelers(detailed=False)
            self.subscribed_labelers = [labeler for labeler in subscribed_labelers if labeler not in self.default_labelers]

        params = {
            'uri_patterns': targets,
            'sources': labelers or self.subscribed_labelers,
            'limit': 250, # replace with pagination?
        }

        if not params['sources'] or not params['uri_patterns']:
            return {}

        result = await self.client.com.atproto.label.query_labels(params=params)
        return {
            label.uri: {
                'label': label.val,
                'labeler': label.src,
            } for label in result.labels
        }

    @auth_required
    async def label_posts(self, posts: list[dict], labelers: list[str] | None = None) -> list[dict]:
        """
        Attach labels from subscribed labelers to posts

        Args:
            posts (list): Posts to query
            labelers (list, optional): list of labeler DIDs to query against. If None, will use subscribed labelers. Defaults to None

        Returns:
            list: list of post dictionaries with subscribed labels appended
        """

        targets = list(set([post['uri'] for post in posts] + [post['author']['did'] for post in posts if 'author' in post]))

        labels = await self.query_labelers(targets=targets, labelers=labelers)

        for post in posts:
            uri = post['uri']
            if uri in labels:
                post['labels'].append(labels[uri])
            if 'author' in post:
                did = post['author']['did']
                if did in labels:
                    post['author']['labels'].append(labels[did])

        return posts

    @auth_required
    async def label_users(self, users: list[dict], labelers: list[str] | None = None) -> list[dict]:
        """
        Attach labels from subscribed labelers to users

        Args:
            users (list): Users to query
            labelers (list, optional): list of labeler DIDs to query against. If None, will use subscribed labelers. Defaults to None

        Returns:
            list: list of user dictionaries with subscribed labels appended
        """

        targets = list(set([user['did'] for user in users]))

        labels = await self.query_labelers(targets=targets, labelers=labelers)

        for user in users:
            if user['did'] in labels:
                if 'labels' not in user: user['labels'] = []
                user['labels'].append(labels[user['did']])

        return users


    @auth_required
    async def get_notifications(self, reasons: list[str] = [], limit: int = 20, unpack_records: bool = True, new_items: bool = False, reset_pagination: bool = False) -> list[dict]:
        """
        Get notifications.

        Args:
            reasons (list): List of notification reasons to include (e.g., follow, like, repost, reply, mention, quote). Defaults to all
            limit (int): Number of notifications to retrieve
            unpack_records (bool): If True, includes post/profile data for record and subject fields, if applicable.
            new_items (bool): If True, will fetch any new items since the paginator was initialized instead of fetching the next page. Defaults to False
            reset_pagination (bool): If True, resets FeedPaginator to first page of results.

        Returns:
            list: List of notification dictionaries
        """

        feed_id = f'notifications-{'|'.join(reasons)}'
        if self.paginator is None or self.paginator.feed != feed_id or reset_pagination:
            self.paginator = FeedPaginator(
                feed=feed_id,
                params={'reasons': reasons, 'limit': limit},
                id_extractor=lambda notification: notification.uri,
                api_method=self.client.app.bsky.notification.list_notifications,
                response_data_field='notifications'
            )

        try:
            feed = await self.paginator.next_page() if not new_items else await self.paginator.new()

            notifications = []
            for notification in feed:
                item = {
                    'uri': notification.uri,
                    'cid': notification.cid,
                    'user': {
                        'did': notification.author.did,
                        'handle': notification.author.handle,
                        'display_name': notification.author.display_name,
                        'avatar': notification.author.avatar,
                        'description': notification.author.description,
                        'following': notification.author.viewer.following,
                        'followed_by': notification.author.viewer.followed_by,
                        'muted': notification.author.viewer.muted,
                        'blocking': notification.author.viewer.blocking,
                        'blocked_by': notification.author.viewer.blocked_by,
                    },
                    'reason': notification.reason,
                    'is_read': notification.is_read,
                    'created_at': notification.record.created_at,
                    'reason_subject': notification.reason_subject,
                }

                if unpack_records:
                    if item['reason'] in ['repost', 'like']:
                        item['subject'] = await self.get_post_data(item['reason_subject'], media_types=['images', 'videos', 'external_links', 'starter_packs', 'lists', 'feeds'], extract_reply_parents=False)
                        item['record'] = None

                    elif item['reason'] in ['reply', 'quote']:
                        item['subject'] = await self.get_post_data(item['reason_subject'], media_types=['images', 'videos', 'external_links', 'starter_packs', 'lists'], extract_reply_parents=False)
                        item['record'] = await self.get_post_data(item['uri'], media_types=['images', 'videos', 'external_links', 'starter_packs', 'lists', 'feeds'], extract_reply_parents=False)

                    elif item['reason'] == 'mention':
                        item['subject'] = None
                        item['record'] = await self.get_post_data(item['uri'], media_types=['images', 'videos', 'external_links', 'starter_packs', 'lists', 'feeds'], extract_reply_parents=False)

                    elif item['reason'] == 'follow':
                        item['subject'] = await self.get_profile(item['user']['handle'])
                        item['record'] = None

                    #TODO confirm no other notification types need to be caught
                    else:
                        item['subject'] = None
                        item['record'] = None

                notifications.append(item)

            return notifications

        except Exception as e:
            print(f"Failed to get notifications: {e}")
            self.paginator.mark_error()
            return []

    @auth_required
    async def get_unread_notification_count(self) -> int:
        """
        Get number of unread notifications.

        Returns:
            int: Number of unread notifications
        """
        try:
            response = await self.client.app.bsky.notification.get_unread_count()
            return response.count

        except AtProtocolError as e:
            print(f"Failed to get notification count: {e}")
            return None

    @auth_required
    async def get_post_url(self, uri: str, handle: str | None = None) -> str:
        """
        Extract URL from post URI.

        Args:
            uri (str): URI of post
            handle (str): handle of post author. Will retrieve from URI if not supplied. Optional

        Returns:
            str: URL of post
        """
        try:
            uri_parts = self._uri_parts(uri)

            if not handle:
                post = await self.get_post_data(uri, extract_media=False, extract_reply_parents=False)
                handle = post['author']['handle']

            return f'{self.get_profile_url(handle)}/post/{uri_parts["rkey"]}'

        except:
            print(f'Failed to get URL for post: {uri}')
            return None

    def get_profile_url(self, handle: str) -> str:
        """
        Return profile URL for handle.

        Args:
            handle (str): handle of profile

        Returns:
            str: URL of profile
        """

        return f'https://bsky.app/profile/{handle}'

    @auth_required
    async def is_post_deleted(self, uri: str) -> bool:
        """
        Determine whether a URI represents a deleted post (i.e., missing post not due to being blocked)

        Args:
            uri (str): post URI to query

        Returns:
            bool: True if deleted
        """
        try:
            uri_parts = self._uri_parts(uri)
            response = await self.client.com.atproto.repo.get_record({
                'repo': uri_parts['repo_did'],
                'collection': uri_parts['collection'],
                'rkey': uri_parts['rkey']
            })
            return False

        except:
            return True


    # Handle media

    @auth_required
    async def extract_media_from_post(self, post, media_types: list[str] = [], include_quoted_media: bool = True, quote_nesting: int = 1):
        """
        Extract specified media types from a post object

        Args:
            post: post object retrieved from atproto feed endpoint
            media_types (list[str]): A list of media types (e.g., ['image', 'video']) to extract. Defaults to an empty list, which includes all supported types.
            include_quoted_media (bool): If True, also includes media found in quoted content. Defaults to True.
            quote_nesting (int): The maximum depth of quote nesting to process. Only applies if include_quoted_media is True. Defaults to 1.

        Returns:
            dict: Dictionary of embedded media (images, videos, external links, quote posts)
        """

        if len(media_types) == 0:
            media_types = ['images', 'videos', 'external_links', 'quote_posts', 'starter_packs', 'lists', 'feeds']

        # Validate media types
        valid_types = {'images', 'videos', 'external_links', 'quote_posts', 'starter_packs', 'lists', 'feeds'}
        media_types = [t for t in media_types if t in valid_types]

        if quote_nesting < 1 and 'quote_posts' in media_types: media_types.remove('quote_posts')

        media = self._empty_media_result(media_types)

        if not post.record.embed:
            return media

        embed = post.record.embed

        # Handle different embed types using py_type
        if hasattr(post.record.embed, 'py_type'):
            embed_type = post.record.embed.py_type

            # Images embed
            if embed_type == 'app.bsky.embed.images' and 'images' in media_types:
                media['images'] = self._extract_images(post)

            # Video embed
            elif embed_type == 'app.bsky.embed.video' and 'videos' in media_types:
                media['videos'] = self._extract_videos(post)

            # External link embed
            elif embed_type == 'app.bsky.embed.external' and 'external_links' in media_types:
                media['external_links'] = self._extract_external_links(post)

            # Starter pack embed
            elif hasattr(post.embed.record, 'record') and post.embed.record.record.py_type == 'app.bsky.graph.starterpack':
                if 'starter_packs' in media_types:
                    media['starter_packs'] = self._extract_starter_packs(post)

            # Record embed (quoted posts, as well as embedded list and feed links)
            elif embed_type == 'app.bsky.embed.record':

                record_embed_type = self._uri_parts(post.record.embed.record.uri)['collection'].split('.')[-1]

                if record_embed_type == 'post' and 'quote_posts' in media_types:
                    media['quote_posts'] = await self._extract_quote_posts(post, include_quoted_media, quote_nesting)

                elif record_embed_type == 'list' and 'lists' in media_types:
                    media['lists'] = await self._extract_lists(post)

                elif record_embed_type == 'generator' and 'feeds' in media_types:
                    media['feeds'] = await self._extract_feeds(post)

            # Record embed with media (quoted posts that also contain other media)
            elif embed_type == 'app.bsky.embed.recordWithMedia':

                if hasattr(embed.media, 'py_type'):
                    rwm_media_embed_type = embed.media.py_type

                    if rwm_media_embed_type == 'app.bsky.embed.images' and 'images' in media_types:
                        media['images'] = self._extract_images(post, rwm=True)

                    elif rwm_media_embed_type == 'app.bsky.embed.video' and 'videos' in media_types:
                        media['videos'] = self._extract_videos(post, rwm=True)

                    elif rwm_media_embed_type == 'app.bsky.embed.external' and 'external_links' in media_types:
                        media['external_links'] = self._extract_external_links(post, rwm=True)

                if 'quote_posts' in media_types:
                    media['quote_posts'] = await self._extract_quote_posts(post, include_quoted_media, quote_nesting, rwm=True)

        return media

    def _empty_media_result(self, media_types):
        """Create empty media result structure"""
        empty_media = {}
        for media_type in media_types:
            empty_media[media_type] = []

        return empty_media

    def _extract_images(self, post, rwm: bool = False) -> list[dict]:
        """
        Extract image data from images embed

        Args:
            post: post object retrieved from atproto feed endpoint
            rwm (bool): whether to use the recordWithMedia object structure. Defaults to False

        Returns:
            list: List of image dicts
        """
        images = []

        record_embed = post.record.embed if not rwm else post.record.embed.media
        post_embed = post.embed if not rwm else post.embed.media

        if hasattr(record_embed, 'images'):
            for i, img in enumerate(record_embed.images):
                image_data = {
                    'blob_ref': img.image.ref.link if hasattr(img, 'image') and hasattr(img.image, 'ref') else None,
                    'mime_type': img.image.mime_type if hasattr(img, 'image') else None,
                    'size': img.image.size if hasattr(img, 'image') else None,
                    'alt': img.alt if hasattr(img, 'alt') else '',
                    'url': post_embed.images[i].fullsize if hasattr(post_embed.images[i], 'fullsize') else None,
                    'url_thumb': post_embed.images[i].thumb if hasattr(post_embed.images[i], 'thumb') else None,
                    'aspect_ratio': None
                }

                # Get aspect ratio if available
                if getattr(img, 'aspect_ratio', None) is not None:
                    image_data['aspect_ratio'] = {
                        'width': img.aspect_ratio.width,
                        'height': img.aspect_ratio.height
                    }

                images.append(image_data)

        return images

    def _extract_videos(self, post, rwm: bool = False) -> list[dict]:
        """
        Extract video data from video embed

        Args:
            post: post object retrieved from atproto feed endpoint
            rwm (bool): whether to use the recordWithMedia object structure. Defaults to False

        Returns:
            list: List containing video dict
        """
        videos = []

        record_embed = post.record.embed if not rwm else post.record.embed.media
        post_embed = post.embed if not rwm else post.embed.media

        if hasattr(record_embed, 'video'):
            video_data = {
                'blob_ref': record_embed.video.ref.link if hasattr(record_embed.video, 'ref') else None,
                'mime_type': record_embed.video.mime_type if hasattr(record_embed.video, 'mime_type') else None,
                'size': record_embed.video.size if hasattr(record_embed.video, 'size') else None,
                'alt': record_embed.alt if hasattr(record_embed, 'alt') else None,
                'thumb': post_embed.thumbnail if hasattr(post_embed, 'thumbnail') else None,
                'url': post_embed.playlist if hasattr(post_embed, 'playlist') else None,
                'aspect_ratio': None,
                'captions': record_embed.captions if hasattr(record_embed, 'captions') else None
            }

            if getattr(record_embed, 'aspect_ratio', None) is not None :
                video_data['aspect_ratio'] = {
                    'width': record_embed.aspect_ratio.width,
                    'height': record_embed.aspect_ratio.height
                }

            videos.append(video_data)

        return videos

    def _extract_external_links(self, post, rwm: bool = False) -> list[dict]:
        """
        Extract external link data

        Args:
            post: post object retrieved from atproto feed endpoint
            rwm (bool): whether to use the recordWithMedia object structure. Defaults to False

        Returns:
            list: List containing external link dict
        """
        links = []

        record_embed = post.record.embed if not rwm else post.record.embed.media

        if hasattr(record_embed, 'external'):
            external = record_embed.external
            link_data = {
                'uri': external.uri if hasattr(external, 'uri') else None,
                'title': external.title if hasattr(external, 'title') else '',
                'description': external.description if hasattr(external, 'description') else '',
                'thumb_blob_ref': external.thumb.ref.link if getattr(external, "thumb", None) is not None else None,
                'thumb_mime_type': external.thumb.mime_type if getattr(external, "thumb", None) is not None else None,
                'thumb_size': external.thumb.size if getattr(external, "thumb", None) is not None else None
            }
            links.append(link_data)

        return links

    def _extract_starter_packs(self, post) -> list[dict]:
        """
        Extract embedded starter pack data

        Args:
            post: post object retrieved from atproto feed endpoint

        Returns:
            list: List containing starter pack dict
        """
        starter_packs = []

        record_embed = post.embed.record

        sp_data = {
            'uri': record_embed.uri,
            'cid': record_embed.cid,
            'display_name': record_embed.record.name,
            'list_uri': record_embed.record.list,
            'description': record_embed.record.description,
            'joined_count': record_embed.joined_all_time_count,
            'creator': {
                'did': record_embed.creator.did,
                'handle': record_embed.creator.handle,
                'display_name': record_embed.creator.display_name,
                'avatar': record_embed.creator.avatar,
            }
        }

        starter_packs.append(sp_data)

        return starter_packs

    @auth_required
    async def _extract_lists(self, post) -> list[dict]:
        """
        Extract list data

        Args:
            post: post object retrieved from atproto feed endpoint

        Returns:
            list: List containing list dict
        """
        lists = []

        record_embed = post.embed.record
        list_data = await self.get_list_data(record_embed.uri)
        lists.append(list_data)

        return lists

    @auth_required
    async def _extract_feeds(self, post) -> list[dict]:
        """
        Extract feed data

        Args:
            post: post object retrieved from atproto feed endpoint

        Returns:
            list: List containing feed dict
        """
        feeds = []

        record_embed = post.embed.record
        feed_data = await self.get_feed_data(record_embed.uri)
        feeds.append(feed_data)

        return feeds

    @auth_required
    async def _extract_quote_posts(self, post, extract_media: bool = True, nesting: int = 0, rwm: bool = False, extract_reply_parents: bool = False) -> list[dict]:
        """
        Extract record embed data (quoted posts)

        Args:
            post: post object retrieved from atproto feed endpoint
            extract_media (bool): If True, attempts to extract media from posts. Defaults to True.
            nesting (int): The maximum depth of quote nesting to process. Defaults to 0.
            rwm (bool): whether to use the recordWithMedia object structure. Defaults to False
            extract_reply_parents (bool): If True, attempts to extract parent posts from the object (if reply). Defaults to False.

        Returns:
            list: List of post dicts
        """

        records = []

        record_embed = post.record.embed if not rwm else post.record.embed.record

        if hasattr(record_embed, 'record'):
            record = record_embed.record
            try:
                record_data = await self.get_post_data(uri=record.uri, extract_media=extract_media, media_types=[], quote_nesting=nesting-1, extract_reply_parents=extract_reply_parents)
                records.append(record_data)
            except:
                pass

        return records
