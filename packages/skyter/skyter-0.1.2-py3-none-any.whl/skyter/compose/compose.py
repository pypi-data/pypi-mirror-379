from textual.widgets import Static, TextArea, Button

from skyter.data_classes import Post


class ComposeWidget(Static):
    """Common methods for text composition"""

    def __init__(self, reference: Post | str | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.char_limit = 0
        self.reference = reference

    def on_mount(self) -> None:
        self.text_area = self.query_one(TextArea)
        self.text_area.focus()
        self.check_char_limit()

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        """Handle text area changes to update character counter."""
        self.check_char_limit()

    def update_char_counter(self, counter: Static, button: Button, empty_ok_when: callable = None):
        """Check text against char limit and modify button state."""

        current_length = len(self.text_area.text)

        if current_length > self.char_limit:
            counter_color = f'{self.app.theme_variables['text-error']} bold'
            button.disabled = True
        elif current_length >= self.char_limit * 0.9:
            counter_color = self.app.theme_variables['text-warning']
            button.disabled = False
        elif current_length == 0 and not empty_ok_when:
            counter_color = self.app.theme_variables['foreground']
            button.disabled = True
        else:
            counter_color = self.app.theme_variables['foreground']
            button.disabled = False

        counter.update(f"[{counter_color}]{current_length} / {self.char_limit}[/]")

    def action_close_screen(self) -> None:
        """Action for closing the compose screen."""
        self.app.pop_screen()
