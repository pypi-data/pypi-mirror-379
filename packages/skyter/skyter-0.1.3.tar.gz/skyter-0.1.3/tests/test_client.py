import pytest
import os
from dotenv import load_dotenv
import time

from atproto import client_utils

from skyter.bsky import BlueSkyClient


@pytest.fixture
def client():
    """Provides BlueSkyClient instance"""
    return BlueSkyClient()

@pytest.fixture
def example_post():
    return 'at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3ltmzy7cs5c22'

@pytest.fixture
def example_user_handle():
    return 'bsky.app'

@pytest.fixture
def example_verified_user_handle():
    return 'pfrazee.com'

@pytest.fixture
def example_feed():
    return 'at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.generator/whats-hot'

@pytest.fixture
def example_feed_2():
    return 'at://did:plc:mk6ifd3oztj2f2l3v3ysrw2c/app.bsky.feed.generator/aaakqsvp6kke4'

@pytest.fixture
def example_labeler():
    return 'did:plc:ar7c4by46qjdydhdevvrndac'

@pytest.fixture
def example_deleted_post():
    return 'at://did:plc:4d2snfeymcblmvoaxvgfs7i6/app.bsky.feed.post/3lunxp7e3k22c'

async def login(client):
    load_dotenv()
    creds = (os.getenv("BSKY_LOGIN"), os.getenv("BSKY_APP_PASSWORD"))
    pds = os.getenv("BSKY_PDS")
    return await client.login(*creds, pds)

@pytest.mark.asyncio
async def test_login(client):
    assert(await login(client))

@pytest.mark.asyncio
async def test_change_pds():
    load_dotenv()
    creds = (os.getenv("BSKY_LOGIN"), os.getenv("BSKY_APP_PASSWORD"))
    init_pds = 'https://example.com'
    client = BlueSkyClient(pds_url=init_pds)
    real_pds = os.getenv("BSKY_PDS") or 'https://bsky.social'
    result = await client.login(*creds, pds=real_pds)
    assert result

@pytest.mark.asyncio
async def test_auth_required(client):
    result = await client.post('test')
    assert result is None

def is_uri(uri, client):
    uri_parts = client._uri_parts(uri)
    return all([f in uri_parts for f in ['repo_did', 'collection', 'rkey']]) and uri_parts['repo_did'].startswith('did')

def test_uri_parts(example_post, client):
    assert is_uri(example_post, client)

@pytest.mark.asyncio
async def test_post_text_build(client):
    text='hello https://bsky.app/ dog #test #1 dad #1-dad #1800-500-1234 $#!t #https://google.com http://docs.bsky.app/docs/advanced-guides/oembed#oembed-endpoint # ## google.com https://test.lol.xyz'
    post = await client.build_post_text(text)
    assert isinstance(post, client_utils.TextBuilder)
    facets = post.build_facets()
    assert len(facets) == 6
    assert facets[0].features[0].uri == 'https://bsky.app/'
    assert facets[3].features[0].tag == 'https://google.com'
    assert facets[5].features[0].uri == 'https://test.lol.xyz'


# Get actions

@pytest.mark.asyncio
async def test_get_post(example_post, client):
    await login(client)
    result = await client.get_post_data(uri=example_post)
    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_get_post_url(example_post, client):
    await login(client)
    result = await client.get_post_url(example_post)
    assert isinstance(result, str)

@pytest.mark.asyncio
async def test_get_thread(example_post, client):
    await login(client)
    result = await client.get_thread(uri=example_post, limit=1, max_depth=1)
    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_get_timeline(client):
    await login(client)
    result = await client.get_timeline(limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_get_feed(example_feed, client):
    await login(client)
    feed_data = await client.get_feed_data(example_feed)
    assert isinstance(feed_data, dict)
    result = await client.get_feed(example_feed, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_get_user_profile(example_user_handle, client):
    await login(client)
    result = await client.get_profile(example_user_handle)
    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_verification(example_user_handle, example_verified_user_handle, client):
    await login(client)
    verifier_result = await client.get_profile(example_user_handle)
    assert verifier_result['verification'] == 'verifier'
    verified_result = await client.get_profile(example_verified_user_handle)
    assert verified_result['verification'] == 'verified'

@pytest.mark.asyncio
async def test_get_user_posts(example_user_handle, client):
    await login(client)
    result = await client.get_user_posts(example_user_handle, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_get_user_likes(example_user_handle, client):
    await login(client)
    result = await client.get_user_likes(example_user_handle, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_get_user_follows(example_user_handle, client):
    await login(client)
    result = await client.get_follows(example_user_handle, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_get_user_followers(example_user_handle, client):
    await login(client)
    result = await client.get_followers(example_user_handle, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_label_vis_prefs(client):
    await login(client)
    result = await client.get_label_visibility_prefs()
    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_adult_preference(client):
    await login(client)
    result = await client.get_adult_enabled()
    assert isinstance(result, bool)

@pytest.mark.asyncio
async def test_labeler_data(client, example_labeler):
    await login(client)
    result = await client.get_labeler_data(did=example_labeler)
    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_content_policies(client):
    await login(client)
    result = await client.get_content_policies()
    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_subscribed_labels(client, example_post, example_user_handle):
    await login(client)
    post_result = await client.get_post_data(uri=example_post)
    post_label_result = await client.label_posts(posts=[post_result])
    assert isinstance(post_label_result[0], dict)
    user_result = await client.get_profile(handle=example_user_handle)
    user_label_result = await client.label_users(users=[user_result])
    assert isinstance(user_label_result[0], dict)

@pytest.mark.asyncio
async def test_get_user_starter_packs(example_user_handle, client):
    await login(client)
    result = await client.get_user_starter_packs(example_user_handle, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_starter_pack_lists(client):
    await login(client)
    result = await client.get_suggested_starter_packs()
    assert isinstance(result[0], dict)
    list_uri = result[0]['list_uri']
    list_data_result = await client.get_list_data(uri=list_uri)
    assert isinstance(list_data_result, dict)
    list_people_result = await client.get_list_people(uri=list_uri, limit=1)
    assert isinstance(list_people_result[0], dict)

@pytest.mark.asyncio
async def test_search_posts(client):
    await login(client)
    query = '#photography'
    result = await client.search_posts(query=query, limit=1, top_posts=True)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_search_users(client):
    await login(client)
    query = 'bsky'
    result = await client.search_users(query=query, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_search_feeds(client):
    await login(client)
    query = 'sports'
    result = await client.search_feeds(query=query, limit=1)
    assert isinstance(result[0], dict)

@pytest.mark.asyncio
async def test_saved_feeds(client):
    await login(client)
    result = await client.get_saved_feeds()
    assert isinstance(result[0], dict)
    assert await client.is_feed_saved(result[0]['uri'])

@pytest.mark.asyncio
async def test_get_post_interactions(example_post, client):
    await login(client)
    likes_result = await client.get_likes(uri=example_post, limit=1)
    assert isinstance(likes_result[0], dict)
    reposts_result = await client.get_reposts(uri=example_post, limit=1)
    assert isinstance(reposts_result[0], dict)
    quotes_result = await client.get_quotes(uri=example_post, limit=1)
    assert isinstance(quotes_result[0], dict)


@pytest.mark.asyncio
async def test_get_notifications(client):
    await login(client)
    result = await client.get_notifications(limit=1)
    assert isinstance(result[0], dict)
    notification_count = await client.get_unread_notification_count()
    assert isinstance(notification_count, int)

@pytest.mark.asyncio
async def test_deleted_post(example_deleted_post, client):
    await login(client)
    result = await client.get_post_data(example_deleted_post)
    assert isinstance(result, dict)
    assert result['is_deleted_post']

@pytest.mark.asyncio
async def test_blocked_post(example_user_handle, client):
    await login(client)
    posts = await client.get_user_posts(handle=example_user_handle, limit=1)
    block_result = await client.block_user(handle=example_user_handle)
    time.sleep(2)
    result = await client.get_post_data(posts[0]['uri'])
    assert isinstance(result, dict)
    assert result['is_blocked_post']
    await client.delete_block(block_result)


# Post actions

@pytest.mark.asyncio
async def test_like_and_unlike(client, example_post):
    await login(client)
    like_result = await client.like(example_post)
    assert is_uri(like_result, client)
    delete_like_result = await client.delete_like(like_result)
    assert delete_like_result
    await client.like(example_post)
    unlike_result = await client.unlike(example_post)
    assert unlike_result

@pytest.mark.asyncio
async def test_follow_and_unfollow(client, example_user_handle):
    await login(client)
    unfollow_result = await client.unfollow(example_user_handle)
    assert unfollow_result
    follow_result = await client.follow(example_user_handle)
    assert is_uri(follow_result, client)
    remove_follow_result = await client.remove_follow_record(follow_result)
    assert remove_follow_result
    await client.follow(example_user_handle)

@pytest.mark.asyncio
async def test_mute_and_unmute(client, example_user_handle):
    await login(client)
    mute_result = await client.mute_user(example_user_handle)
    assert mute_result
    mute_list_result = await client.get_mute_list(limit=1)
    assert isinstance(mute_list_result[0], dict)
    unmute_result = await client.unmute_user(example_user_handle)
    assert unmute_result

@pytest.mark.asyncio
async def test_block_and_unblock(client, example_user_handle):
    await login(client)
    block_result = await client.block_user(example_user_handle)
    assert is_uri(block_result, client)
    delete_block_result = await client.delete_block(block_result)
    assert delete_block_result
    await client.block_user(example_user_handle)
    time.sleep(2) # block list does not update instantly
    unblock_result = await client.unblock_user(example_user_handle)
    assert unblock_result

@pytest.mark.asyncio
async def test_post_and_delete(client):
    await login(client)
    text = "hello blue yonder"
    post_result = await client.post(text=text)
    assert is_uri(post_result, client)
    post_delete_result = await client.delete_post(post_result)
    assert post_delete_result

@pytest.mark.asyncio
async def test_save_pin_unsave_feed(example_feed_2, client):
    await login(client)
    save_result = await client.save_feed(uri=example_feed_2, pin=True)
    assert save_result
    unpin_result = await client.unpin_feed(uri=example_feed_2)
    assert unpin_result
    pin_result = await client.pin_saved_feed(uri=example_feed_2)
    assert pin_result
    unsave_result = await client.remove_saved_feed(uri=example_feed_2)
    assert unsave_result
