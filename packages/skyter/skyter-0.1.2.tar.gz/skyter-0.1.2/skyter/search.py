from datetime import datetime

from textual.widgets import Input, MaskedInput, Static, Button, Select, Label
from textual.widget import Widget
from textual.containers import Horizontal, Center
from textual import events


class SearchSubmitted(events.Message):
    """Custom message sent when search is submitted."""

    def __init__(self, query: str, params: dict) -> None:
        self.query = query
        self.params = params
        super().__init__()

class SearchView(Widget):
    """Panel for conducting search with search bar and search options."""

    select_mapping = {
        'select-search-type': {
            "Latest Posts": "latest",
            "Top Posts": "top",
            "Users": "users",
            "Feeds": "feeds",
        }
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def compose(self):
        yield Input(placeholder="Search for posts, users or feeds", id="search-bar", classes="search-field")

        with Horizontal(classes="drop-down-container"):
            yield Label("Search type", classes="drop-down-label")
            yield Select.from_values(values=[
                "Latest Posts",
                "Top Posts",
                "Users",
                "Feeds",
            ], allow_blank=False, id="select-search-type")

        with Horizontal(classes="date-input-container"):
            yield Label("From", classes="date-input-label")
            yield Static("", classes="spacer")
            yield MaskedInput('99-99-9999', placeholder='MM-DD-YYYY', valid_empty=True, id='search-since-input', classes='date-input search-field')

        with Horizontal(classes="date-input-container"):
            yield Label("To", classes="date-input-label")
            yield Static("", classes="spacer")
            yield MaskedInput('99-99-9999', placeholder='MM-DD-YYYY', valid_empty=True, id='search-until-input', classes='date-input search-field')

        with Center():
            yield Button("Search", id="search-btn", variant="primary")

    def on_select_changed(self, event: Select.Changed) -> None:
        """Handle when select search type is changed and disable/enable applicable form fields."""

        if event.select.id == 'select-search-type':
            date_inputs = self.query('.date-input')
            if "Posts" in event.value:
                for date_input in date_inputs:
                    date_input.disabled = False
            else:
                for date_input in date_inputs:
                    date_input.disabled = True

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle when text is submitted in an input field."""

        query = event.value.strip()
        if query:
            if event.input.id == "search-bar":
                self.handle_search()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "search-btn":
            self.handle_search()

    def handle_search(self) -> None:
        """Handle when text is submitted in an input field."""

        query = self.query_one("#search-bar", Input).value.strip()
        if query:

            since = None
            since_input = self.query_one('#search-since-input')
            if not since_input.disabled and since_input.value:
                since = self._validate_datetime_field(since_input)
                if since is None: return
            until = None
            until_input = self.query_one('#search-until-input')
            if not until_input.disabled and until_input.value:
                until = self._validate_datetime_field(until_input)
                if until is None: return

            params = {
                'search_type': self._get_select_mapping('select-search-type'),
                'since': since,
                'until': until,
            }

            self.screen.post_message(SearchSubmitted(query=query, params=params))

    def reset(self, query: str | None = None):
        """Reset form to default values, optionally setting search bar value."""
        fields = self.query('.search-field')
        for f in fields:
            if f.id == 'search-bar' and query:
                f.value = query
            else:
                f.value = ''

    def _get_select_mapping(self, item_id):
        """Return value associated with displayed Select text"""
        return self.select_mapping[item_id][self.query_one(f'#{item_id}', Select).value]

    def _validate_datetime_field(self, date_input: MaskedInput):
        """Check if date field contains valid input"""
        if date_input.validate(date_input.value).is_valid:
            result = self._str_to_datetime(date_input.value)
            if result is None:
                self.app.notify('Invalid date', severity="warning")
            return result
        else:
            self.app.notify('Invalid date', severity="warning")
            return None

    @staticmethod
    def _str_to_datetime(dt_str: str):
        """Convert %m-%d-%Y string to datetime format"""
        try:
            return datetime.strptime(dt_str, '%m-%d-%Y')
        except:
            return None

