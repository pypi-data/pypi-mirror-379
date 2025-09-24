from textual.app import ComposeResult
from textual.widgets import Static, TextArea, Button, Footer, Label
from textual.binding import Binding
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual_fspicker import FileOpen
from textual_fspicker.path_filters import Filters as FileFilters
from rich.text import Text

from skyter.compose.compose import ComposeWidget


class MediaOpen(FileOpen):
    """File picker screen for attaching image and video files"""

    FORMATS = {
        'images': ['.png', '.jpg', '.jpeg', '.webp'],
        'videos': ['.mov', '.mp4', '.mpeg', '.webm'] # seemingly no gif conversion with API
    }

    def __init__(self, media_type: str, **kwargs) -> None:
        super().__init__(
            title="File upload",
            location=self.app.file_picker_location,
            filters=FileFilters(
                (media_type.title(), lambda p: p.suffix.lower() in self.FORMATS[media_type]),
                ("All", lambda _: True),
            ),
            **kwargs
        )


class AltComposeScreen(ModalScreen):
    """Alt text compose screen"""

    def __init__(self, media_item: dict, **kwargs) -> None:
        self.filepath = media_item['path']
        self.alt = media_item['alt']
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield AltComposeWidget(reference=self.filepath, alt=self.alt)
        if self.app.show_footer:
            yield Footer()


class AltComposeWidget(ComposeWidget):
    """Widget containing a text area for composing alt text"""

    BINDINGS = [
        Binding("ctrl+s", "save_alt", "Save"),
        Binding("escape", "close_screen", "Cancel"),
    ]

    def __init__(self, alt: str | None = None, **kwargs):
        super().__init__(**kwargs)
        self.alt = alt or ''
        self.char_limit = 2000

    def compose(self) -> ComposeResult:
        with Vertical(classes="compose-container"):
            title = Text()
            title.append('alt text for ', style=self.app.theme_variables['foreground'])
            title.append(self.reference, style=self.app.theme_variables['text-secondary'])
            yield Label(title, id='alt-compose-title')
            yield TextArea(text=self.alt, id="alt-compose-input")
            yield Static(f"0 / {self.char_limit}", id="alt-compose-char-counter", classes='char-counter')
            with Horizontal(classes="compose-button-container"):
                yield Button("Cancel", id="alt-cancel-btn", variant="default")
                yield Static("", classes="spacer")
                yield Button("Save", id="alt-save-btn", variant="primary")


    def check_char_limit(self) -> None:
        """Update character counter display and submit button state."""

        char_counter = self.query_one("#alt-compose-char-counter", Static)
        submit_button = self.query_one("#alt-save-btn", Button)

        self.update_char_counter(counter=char_counter, button=submit_button, empty_ok_when=lambda _: True)

    def action_save_alt(self) -> None:
        """Save alt text and exit screen"""
        text_area = self.query_one("#alt-compose-input", TextArea)
        text_content = text_area.text.strip()
        self.screen.dismiss(text_content)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle save and cancel button presses"""
        if event.button.id == "alt-save-btn":
            self.action_save_alt()
        elif event.button.id == "alt-cancel-btn":
            self.action_close_screen()