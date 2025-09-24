from pyfiglet import Figlet

from textual.widgets import Input, Button, Footer
from textual.widget import Widget
from textual.containers import Center, Middle
from textual.screen import Screen
from textual import events
from textual.app import ComposeResult
from rich.text import Text


class LoggedIn(events.Message):
    """Custom message sent when login is successful."""
    pass

class LoginScreen(Screen):
    """Login screen"""

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield Title(name="skyter", id='app-title')
                yield LoginForm(id='login-form')
        if self.app.show_footer:
            yield Footer()

class Title(Widget):
    """Render app title in figlet font"""

    def __init__(self, name: str, **kwargs) -> None:
        self.font = 'stellar'
        super().__init__(name=name, **kwargs)

    def render(self):
        return Text(
            Figlet(self.font).renderText(self.name),
            no_wrap=True,
            overflow='crop',
        )

class LoginForm(Widget):
    """Form widget to enter credentials"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Handle or email", id="username", classes="login-field")
        yield Input(password=True, placeholder="Password or app password", id="password", classes="login-field")
        yield Input(placeholder="PDS (optional)", value=self.app.pds, id="pds", classes="login-field", valid_empty=True)
        with Center():
            yield Button("Login", id="login-btn", variant="primary")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "login-btn":
            await self.handle_login()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle when text is submitted in an input field."""

        if event.input.id in ["username", "password", "pds"]:
            await self.handle_login()

    async def handle_login(self) -> None:
        """Handle login button press."""
        username_input = self.query_one("#username", Input)
        password_input = self.query_one("#password", Input)
        pds_input = self.query_one("#pds", Input)

        username = username_input.value
        password = password_input.value
        pds = pds_input.value

        if pds and pds != self.app.pds:
            self.app.pds = pds

        # validate credentials
        if username and password:
            response = await self.app.login((username, password))
            if response:
                self.app.post_message(LoggedIn())
        else:
            self.app.notify("Username and password are required", severity="warning")
