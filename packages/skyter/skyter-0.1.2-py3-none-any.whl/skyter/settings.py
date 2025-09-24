from dataclasses import dataclass, field, asdict
from pathlib import Path
import os
import json

from textual.app import ComposeResult
from textual.widgets import Static, Button, Footer, Label, TextArea
from textual.binding import Binding
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual import work
from rich.text import Text

from skyter.data_classes import FeedSource

@dataclass
class Settings:
    """Data class for accessing app settings"""
    initial_source: FeedSource = field(default_factory=FeedSource)
    page_limit: int = 20
    default_pds: str | None = None # when None uses https://bsky.social
    search_language: str | None = None
    relative_dates: bool = True
    show_footer: bool = True
    notification_check_interval: int | None = 60 # set to None to turn off header notification display
    feed_new_items_check_interval: int | None = 60
    feed_new_items_action: str | None = 'alert' # 'alert', 'update', or None
    subscribed_labels: bool = True
    hide_metrics: bool = False
    file_picker_location: str = '.'
    open_cmds: dict = field(default_factory=lambda: { # commands to pass to subprocess. if None, uses webbrowser to open URLs
        'images': None, # or e.g., "feh"
        'video': None, # or e.g., "mpv --terminal=no"
        'external_link': None,
    })
    path: Path = Path(os.path.dirname(__file__)) / "data" / "settings.json"

    @classmethod
    def from_json(cls, filepath: Path | str | None = None) -> "Settings":
        """Create data class object from json file if it exists."""
        if filepath is None:
            filepath = Path(os.path.dirname(__file__)) / "data" / "settings.json"

        filepath = Path(filepath)

        # if file doesn't exist, create with defaults
        if not filepath.exists():
            settings = cls(path=filepath)
            settings.to_json()
            return settings

        with open(filepath) as f:
            data = json.load(f)
            data['path'] = Path(filepath)

        if "initial_source" in data:
            initial_source_data = data.pop("initial_source")
            initial_source = FeedSource(**initial_source_data)
            data["initial_source"] = initial_source

        field_names = {f.name for f in Settings.__dataclass_fields__.values()}
        data = {k: v for k, v in data.items() if k in field_names}

        return cls(**data)

    def to_json(self) -> None:
        """Write data class object to json file"""
        data = asdict(self)
        data["initial_source"] = self.initial_source.__dict__

        filepath = data.pop('path')

        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def get_json(self):
        """Returns a JSON string representation of the data class"""
        data = asdict(self)
        data["initial_source"] = self.initial_source.__dict__
        del data['path']
        return json.dumps(data, indent=4)

    def update_from_json_string(self, json_str: str):
        """Updates the data class from JSON string"""
        data = json.loads(json_str)
        if "initial_source" in data:
            initial_source_data = data.pop("initial_source")
            initial_source = FeedSource(**initial_source_data)
            data["initial_source"] = initial_source

        field_names = {f.name for f in Settings.__dataclass_fields__.values()}
        data = {k: v for k, v in data.items() if k in field_names}

        # keep path property
        data['path'] = self.path

        return self.__class__(**data)


class SettingsScreen(ModalScreen):
    """Settings config screen"""

    def __init__(self, settings: Settings, **kwargs) -> None:
        self.settings = settings
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield EditSettings(settings=self.settings)
        if self.app.show_footer:
            yield Footer()

class EditSettings(Widget):
    """Widget containing the editable JSON settings"""

    BINDINGS = [
        Binding("ctrl+s", "save_settings", "Save"),
        Binding("escape", "close_screen", "Cancel"),
    ]

    def __init__(self, settings: Settings, **kwargs) -> None:
        super().__init__(**kwargs)
        self.settings = settings

    def compose(self) -> ComposeResult:
        with Vertical(classes="settings-container"):
            title = Text()
            title.append('Editing ', style=self.app.theme_variables['foreground'])
            title.append(str(self.settings.path), style=self.app.theme_variables['text-secondary'])
            yield Label(title, id='settings-title')
            yield TextArea(text=self.settings.get_json(), language='json', show_line_numbers=True, id="settings-json-input")
            with Horizontal(classes="settings-button-container"):
                yield Button("Cancel", id="settings-cancel-btn", variant="default")
                yield Static("", classes="spacer")
                yield Button("Save", id="settings-submit-btn", variant="primary")

    def on_mount(self) -> None:
        self.text_area = self.query_one(TextArea)

    @work
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle save and cancel button presses"""
        if event.button.id == "settings-submit-btn":
            self.action_save_settings()
        elif event.button.id == "settings-cancel-btn":
            self.action_close_screen()

    def check_valid_json(self):
        """Check if text area contains valid JSON"""
        try:
            json.loads(self.text_area.text)
            return True
        except ValueError as e:
            return False

    def action_save_settings(self) -> None:
        """Action for saving settings."""
        if self.check_valid_json():
            self.settings = self.settings.update_from_json_string(self.text_area.text)
            self.settings.to_json()
            self.app._settings = self.settings
            self.app.update_settings()
            self.app.notify('Settings saved')
            self.action_close_screen()
        else:
            self.app.notify('Invalid JSON', severity="warning")

    def action_close_screen(self) -> None:
        """Action for closing the screen."""
        self.app.pop_screen()
