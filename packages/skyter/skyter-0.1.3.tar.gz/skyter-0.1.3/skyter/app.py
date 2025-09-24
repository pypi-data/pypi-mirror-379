from typing import Iterable
import os
import logging
import argparse

from textual.app import App, SystemCommand
from textual.screen import Screen
from textual.binding import Binding
from textual.app import App
from textual.screen import Screen

from skyter.bsky import BlueSkyClient
from skyter.main_screen import MainScreen
from skyter.login import LoggedIn, LoginScreen
from skyter.compose.post_compose import PostSubmitted
from skyter.settings import Settings, SettingsScreen
from skyter import __version__


class MainApp(App):

    HORIZONTAL_BREAKPOINTS = [
        (0, "-narrow"),
        (130, "-wide"),
    ]

    CSS_PATH = "styles.tcss"

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
    ]

    NOTIFICATION_TIMEOUT = 2

    def __init__(self, credentials: tuple | None = None, settings: Settings = Settings.from_json(), pds: str | None = None, **kwargs):

        self.pds = pds or settings.default_pds
        self.client = BlueSkyClient(pds_url=self.pds)
        self.initial_source = settings.initial_source
        self.logged_in = False
        self._credentials = credentials

        # app settings
        self._settings = settings
        self.update_settings()

        # state variables
        self._previous_focus_palette = None
        self._feed_stack = [{'source': self.initial_source}]
        self._feed_stack_idx = 0

        super().__init__(**kwargs)

    def action_command_palette(self):
        """Store app focus before launching command palette."""
        self._previous_focus_palette = self.focused
        super().action_command_palette()

    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        """Add actions to the command palette."""
        yield from super().get_system_commands(screen)

        yield SystemCommand("Settings", "Open settings screen", self.action_open_settings)

        # Get custom actions from screen
        if hasattr(screen, 'offer_screen_commands'):
            try:
                yield from screen.offer_screen_commands()
            except Exception as e:
                self.log.error(f"Error getting commands from {screen}: {e}")

        # Get custom actions from focused widget
        active_widget = self._previous_focus_palette
        if active_widget and hasattr(active_widget, 'offer_widget_commands'):
            try:
                yield from active_widget.offer_widget_commands()
            except Exception as e:
                self.log.error(f"Error getting commands from {active_widget}: {e}")

    async def on_mount(self) -> None:
        """Set title and focus feed on mount"""
        if self._credentials:
            await self.login(self._credentials)
            self._credentials = None
            if self.logged_in:
                self.push_screen(MainScreen(client=self.client, source=self.initial_source))
            else:
                self.push_screen(LoginScreen())
        else:
            self.push_screen(LoginScreen())

    async def login(self, credentials: tuple[str]) -> bool:
        result = await self.client.login(*credentials, pds=self.pds)
        if result:
            self.app.notify(f"Successfully logged in as {credentials[0]}")
            self.logged_in = True
            self.content_policies = await self.client.get_content_policies(include_subscribed_labelers=self.subscribed_labels)
        else:
            self.app.notify("Invalid username or password", severity="error")
        return result

    def on_logged_in(self, message: LoggedIn) -> None:
        """Push main app screen on login"""
        self.pop_screen()
        self.push_screen(MainScreen(client=self.app.client, source=self.initial_source))

    async def on_post_submitted(self, message: PostSubmitted) -> None:
        """Make client call with data received from post compose"""
        images = message.media['images']
        video = message.media['videos'][0] if len(message.media['videos']) > 0 else None
        link = message.media['links'][0] if len(message.media['links']) > 0 else None
        if message.post_type == 'reply' and message.reference_uri:
            post_uri = await self.client.post(message.text, reply_to=message.reference_uri, images=images, video=video)
        elif message.post_type == 'quote' and message.reference_uri:
            post_uri = await self.client.post(message.text, quote=message.reference_uri, images=images, video=video, link=link)
        else:
            post_uri = await self.client.post(message.text, images=images, video=video, link=link)
        if post_uri:
            self.app.notify(f'posted message {post_uri}')
        else:
            self.app.notify('failed to post message', severity="error")

    def action_open_settings(self):
        """Open settings screen"""
        self.push_screen(SettingsScreen(settings=self._settings))

    def update_settings(self):
        """Updates app attributes from settings"""
        self.page_limit = self._settings.page_limit
        self.search_language = self._settings.search_language
        self.relative_dates = self._settings.relative_dates
        self.show_footer = self._settings.show_footer
        self.notification_check_interval = self._settings.notification_check_interval
        self.feed_new_items_check_interval = self._settings.feed_new_items_check_interval
        self.feed_new_items_action = self._settings.feed_new_items_action
        self.subscribed_labels = self._settings.subscribed_labels
        self.hide_metrics = self._settings.hide_metrics
        self.file_picker_location = self._settings.file_picker_location
        self.open_cmds = self._settings.open_cmds

def parse_args():
    """Parse command line options"""
    parser = argparse.ArgumentParser(description='bsky TUI')
    parser.add_argument('-l', '--log',
        nargs='?',
        const='app.log',
        default=None,
        type=str,
        help='Enable logging',
        metavar='LOG_FILE'
    )
    parser.add_argument('--config',
        type=str,
        default=None,
        help='Config JSON file location',
        metavar='CONFIG_FILE'
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'skyter {__version__}'
    )

    return parser.parse_args()

def main():
    """Look for environment variable credentials and load app"""

    args = parse_args()

    if args.log:

        log_level = logging.DEBUG

        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filename=args.log
        )
        logger = logging.getLogger(__name__)

    try:
        from dotenv import load_dotenv # type: ignore
        load_dotenv()
    except:
        pass
    try:
        credentials = (os.getenv("BSKY_LOGIN"), os.getenv("BSKY_APP_PASSWORD"))
        pds = os.getenv("BSKY_PDS")
        if any(x is None for x in credentials): credentials = None
    except:
        credentials = None
        pds = None

    app = MainApp(credentials=credentials, settings=Settings.from_json(args.config), pds=pds)
    app.run()

if __name__ == "__main__":
    main()
