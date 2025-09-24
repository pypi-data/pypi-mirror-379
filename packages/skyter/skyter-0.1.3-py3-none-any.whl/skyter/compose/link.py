from textual.app import ComposeResult
from textual.widgets import Static, Input, Button, Footer, Label
from textual.binding import Binding
from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen

from skyter.utils import get_url_meta, validate_url


class LinkAddScreen(ModalScreen):
    """Embedded link creation screen"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield LinkAddWidget()
        if self.app.show_footer:
            yield Footer()

class LinkAddWidget(Widget):
    """Widget containing a form for embedded link data"""

    BINDINGS = [
        Binding("ctrl+s", "save_link", "Save"),
        Binding("escape", "close_screen", "Cancel"),
    ]

    link_fields = ['url', 'title', 'description', 'image']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        with Vertical(classes="compose-container"):
            yield Label('URL', classes='link-add-form-label')
            yield Input(placeholder='Enter URL', id="link-url-input", classes="link-add-form-field")
            with Horizontal(classes="compose-button-container"):
                yield Button("Cancel", id="link-cancel-btn", variant="default")
                yield Static("", classes="spacer")
                yield Button("Save", id="link-submit-btn", variant="primary", disabled=True)
            yield Label('Title', classes='link-add-form-label')
            yield Input(id="link-title-input", disabled=True, classes="link-add-form-field")
            yield Label('Description', classes='link-add-form-label')
            yield Input(id="link-description-input", disabled=True, classes="link-add-form-field")
            yield Label('Image', classes='link-add-form-label')
            yield Input(id="link-image-input", disabled=True, classes="link-add-form-field")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle when text is submitted in URL input field."""

        text = event.value.strip()
        if text:
            if event.input.id == "link-url-input":
                await self.handle_url_submitted(url=text)


    async def handle_url_submitted(self, url: str | None = None):
        """Read meta information from URL and populate form"""

        if not url:
            url = self.query_one('#link-url-input').value
        if not url:
            return

        url = validate_url(url)
        if not url:
            self.app.notify('Invalid URL', severity='warning')
            return

        meta = await get_url_meta(url)
        if meta:
            for k,v in meta.items():
                widget = self.query_one(f"#link-{k}-input")
                widget.value = v if v else ''
                widget.disabled = False
        else:
            for k in self.link_fields:
                self.query_one(f"#link-{k}-input").disabled = False
            self.app.notify('Unable to retrieve page data from URL', severity='warning')

        submit_btn = self.query_one('#link-submit-btn')
        submit_btn.disabled = False
        submit_btn.focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle save and cancel button presses"""
        if event.button.id == "link-submit-btn":
            self.action_save_link()
        elif event.button.id == "link-cancel-btn":
            self.action_close_screen()

    def action_save_link(self) -> None:
        """Save link data and exit screen"""
        link = {k: self.query_one(f"#link-{k}-input").value for k in self.link_fields}
        self.screen.dismiss(link)

    def action_close_screen(self) -> None:
        """Action for closing the screen."""
        self.app.pop_screen()
