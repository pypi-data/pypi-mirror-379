from datetime import datetime, timezone
import re
from rich.text import Text
import aiohttp
import asyncio
from urllib.parse import urljoin, urlparse
import socket
from bs4 import BeautifulSoup


def time_since(timestamp: str) -> str:
    """Converts an ISO 8601 UTC timestamp to a human-readable relative time string like '2h' or '3d'."""
    now = datetime.now(timezone.utc)
    then = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    delta = now - then

    seconds = delta.total_seconds()

    # Define time units and their abbreviations
    intervals = [
        (31536000, "y"),   # 365 days
        (2592000, "mo"),   # 30 days
        (604800, "w"),     # 7 days
        (86400, "d"),      # 1 day
        (3600, "h"),       # 1 hour
        (60, "m"),         # 1 minute
        (1, "s")           # 1 second
    ]

    for interval_seconds, abbrev in intervals:
        if seconds >= interval_seconds:
            value = int(seconds // interval_seconds)
            return f"{value}{abbrev}"

    return "0s"

def time_str(timestamp: str) -> str:
    """Converts an ISO 8601 UTC timestamp to a human-readable localized time string like 'May 4 2025 at 1:03PM'."""
    utc_dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    local_dt = utc_dt.astimezone()
    return local_dt.strftime('%B %-d %Y at %-I:%M%p')

def format_time(timestamp: str, relative: bool = True) -> str:
    if relative:
        return time_since(timestamp)
    else:
        return time_str(timestamp)

def get_month_year(timestamp: str):
    """Converts an ISO 8601 UTC timestamp to Month Year."""
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    return dt.strftime("%B %Y")

def abbrev_num(n: int):
    """Converts integer to abbreviated string with 1 decimal accuracy."""
    abs_n = abs(n)
    sign = '-' if n < 0 else ''

    if abs_n >= 1_000_000_000:
        value = abs_n / 1_000_000_000
        suffix = 'b'
    elif abs_n >= 1_000_000:
        value = abs_n / 1_000_000
        suffix = 'm'
    elif abs_n >= 1_000:
        value = abs_n / 1_000
        suffix = 'k'
    else:
        return str(n)

    formatted = f"{value:.1f}"
    if formatted.endswith('.0'):
        formatted = formatted[:-2]

    return f"{sign}{formatted}{suffix}"

def handle_to_link(handle: str) -> str:
    """Converts handle into clickable link that loads profile"""
    if handle.startswith('@'): handle = handle[1:]
    return Text.from_markup(f'[@click=screen.build_user_feed(\'{handle}\')]@{handle}[/]')

def extract_tags_and_handles(text: str) -> Text:
    """Convert instances of hashtags and handles in string to clickable links"""

    handle_pattern = r'(?<=^|(?<=\s)|(?<=\s\.)|(?<=^\.))@(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}'

    tag_pattern = r'(?:(?<=\s)|(?<=^))#(?=\S*[a-zA-Z])[^\s]*[a-zA-Z0-9](?=\s|[^a-zA-Z0-9]+\s|$)'

    def replace_handle(match):
        handle = match.group(0)
        return f'[@click=screen.build_user_feed(\'{handle[1:]}\')]{handle}[/]'

    def replace_tag(match):
        tag = match.group(0)
        tag = tag.replace("'","\\'") # escape single quotes
        return f'[@click=screen.build_tag_result(\'{tag}\')]{tag}[/]'

    text = text.replace('[','\\[') # escape markup characters
    result = re.sub(tag_pattern, replace_tag, text)
    result = re.sub(handle_pattern, replace_handle, result)

    return Text.from_markup(result)

def remove_bidi_controls(text: str) -> str:
    """Remove Unicode bidirectional control characters"""
    if text is None: return None
    bidi_controls = re.compile(r'[\u202A-\u202E\u2066-\u2069]')
    return bidi_controls.sub('', text)

async def get_url_meta(url: str) -> dict:
    """
    Retrieve meta information from a URL.

    Args:
        url (str): The URL to fetch meta information from
        timeout (int): Request timeout in seconds (default: 10)

    Returns:
        Dict with keys: 'title', 'description', 'image', 'url'
    """

    timeout = 10

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    result = {
        'title': '',
        'description': '',
        'image': None,
        'url': url
    }

    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return None

                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                # Extract title
                og_title = soup.find('meta', property='og:title')
                if og_title and og_title.get('content'):
                    result['title'] = og_title.get('content').strip()
                else:
                    title_tag = soup.find('title')
                    if title_tag:
                        result['title'] = title_tag.get_text().strip()

                # Extract description
                og_desc = soup.find('meta', property='og:description')
                if og_desc and og_desc.get('content'):
                    result['description'] = og_desc.get('content').strip()
                else:
                    meta_desc = soup.find('meta', attrs={'name': 'description'})
                    if meta_desc and meta_desc.get('content'):
                        result['description'] = meta_desc.get('content').strip()

                # Extract image
                og_image = soup.find('meta', property='og:image')
                if og_image and og_image.get('content'):
                    img_url = og_image.get('content').strip()
                    result['image'] = urljoin(url, img_url)
                else:
                    twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
                    if twitter_image and twitter_image.get('content'):
                        img_url = twitter_image.get('content').strip()
                        result['image'] = urljoin(url, img_url)

        return result

    except asyncio.TimeoutError:
        print(f"Timeout while fetching {url}")
        return None

    except Exception as e:
        print(f"Error fetching meta for {url}: {str(e)}")
        return None

def validate_url(url: str) -> str:
    """
    Validate whether string is a well-formed URL and see if exists

    Args:
        url (str): The URL to validate

    Returns:
        URL with protocol if valid, otherwise None
    """
    url = url.strip()

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    if not url.endswith('/') and '/' not in url[8:]:
        url += '/'

    url_pattern = r'^https?://(?:[-\w.])+(?:\.[a-zA-Z]{2,})+(?:/.*)?$'
    valid_url_pattern = bool(re.match(url_pattern, url))

    if not valid_url_pattern: return None

    try:
        parsed = urlparse(url)
        socket.gethostbyname(parsed.netloc)
        return url

    except socket.gaierror:
        return None
