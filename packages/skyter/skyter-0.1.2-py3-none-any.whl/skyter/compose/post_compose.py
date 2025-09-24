from textual.app import ComposeResult
from textual.widgets import Static, TextArea, Button, Footer, Label
from textual.binding import Binding
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual import events, work
from rich.text import Text
from rich.panel import Panel
from rich import box

from skyter.data_classes import Post
from skyter.compose.compose import ComposeWidget
from skyter.compose.link import LinkAddScreen
from skyter.compose.media import MediaOpen, AltComposeScreen


class PostSubmitted(events.Message):
    """Custom message sent when post is submitted."""

    def __init__(self, text: str, post_type: str, media: dict, reference_uri: str | None = None) -> None:
        self.text = text
        self.post_type = post_type
        self.media = media
        self.reference_uri = reference_uri
        super().__init__()


class PostComposeScreen(ModalScreen):
    """Post compose screen"""

    def __init__(self, reference: Post | None = None, post_type: str | None = None, **kwargs) -> None:
        self.reference = reference
        self.post_type = post_type if post_type else 'post'
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield PostComposeWidget(reference=self.reference, post_type=self.post_type)
        if self.app.show_footer:
            yield Footer()


class PostComposeWidget(ComposeWidget):
    """Widget containing a text area for composing post content"""

    BINDINGS = [
        Binding("ctrl+s", "submit_post", "Post"),
        Binding("escape", "close_screen", "Cancel"),
    ]

    MEDIA_LIMITS = {'images': 4, 'videos': 1, 'links': 1}

    def __init__(self, post_type: str = 'post', **kwargs) -> None:
        super().__init__(**kwargs)
        self.char_limit = 300
        self.post_type = post_type
        self.media = {
            'images': [],
            'videos': [],
            'links': [],
        }

    def compose(self) -> ComposeResult:
        with Vertical(classes="compose-container"):
            with Horizontal(classes="compose-button-container"):
                yield Button("Cancel", id="compose-cancel-btn", variant="default")
                yield Static("", classes="spacer")
                yield Button("Post", id="compose-submit-btn", variant="primary")

            if self.reference and self.post_type == 'reply':
                yield self.ReferencePostEmbed(post=self.reference, id='compose-post-reference')
                yield TextArea(id="compose-input")
                yield Static(f"0 / {self.char_limit}", id="compose-char-counter", classes='char-counter')
            elif self.reference and self.post_type == 'quote':
                yield TextArea(id="compose-input")
                yield Static(f"0 / {self.char_limit}", id="compose-char-counter", classes='char-counter')
                yield self.ReferencePostEmbed(post=self.reference, id='compose-post-reference')
            else:
                yield TextArea(id="compose-input")
                yield Static(f"0 / {self.char_limit}", id="compose-char-counter", classes='char-counter')

            with Vertical(id="media-button-container"):
                with Horizontal():
                    yield Button("Add link", id="link-add-btn", variant="default", classes="media-upload-btn")
                    yield Static(classes="small-spacer-2")
                    yield Vertical(id='link-info-container')
                with Horizontal():
                    yield Button("Add image", id="image-add-btn", variant="default", classes="media-upload-btn")
                    yield Static(classes="small-spacer-2")
                    yield Vertical(id='images-uploaded-container')
                with Horizontal():
                    yield Button("Add video", id="video-add-btn", variant="default", classes="media-upload-btn")
                    yield Static(classes="small-spacer-2")
                    yield Vertical(id='videos-uploaded-container')

    def action_submit_post(self) -> None:
        """Action for submitting post."""
        if self.check_submit_allowed():
            text_area = self.query_one("#compose-input", TextArea)
            text_content = text_area.text.strip()
            reference_uri = self.reference.uri if self.reference else None
            self.app.post_message(PostSubmitted(text=text_content, post_type=self.post_type, media=self.media, reference_uri=reference_uri))
            self.action_close_screen()

    @work
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle submit and cancel button presses"""

        if event.button.id == "compose-submit-btn":
            self.action_submit_post()
        elif event.button.id == "compose-cancel-btn":
            self.action_close_screen()
        elif event.button.id == "link-add-btn":
            await self.handle_link_add()
        elif event.button.id == "image-add-btn":
            await self.handle_file_selector('images')
        elif event.button.id == "video-add-btn":
            await self.handle_file_selector('videos')

    async def handle_link_add(self) -> None:
        """Get form response from link add screen"""
        if new_link := await self.app.push_screen_wait(LinkAddScreen()):
            new_link['id'] = new_link['url']
            self.media['links'].append(new_link)
            self.query_one(f'#link-info-container').mount(self.LinkLabel(new_link))
            self.check_char_limit()
            self.update_media_buttons()

    async def handle_file_selector(self, media_type: str) -> None:
        """Get file path from file selector screen"""
        if opened := await self.app.push_screen_wait(MediaOpen(media_type)):
            media_item = {
                'path': str(opened),
                'alt': None,
                'id': str(opened),
            }
            self.media[media_type].append(media_item)
            self.query_one(f'#{media_type}-uploaded-container').mount(self.MediaFileLabel(media_item))
            self.check_char_limit()
            self.update_media_buttons()

    def remove_attached_file(self, item_id: str):
        for key, lst in self.media.items():
            for i, item in enumerate(lst):
                if item.get('id') == item_id:
                    self.media[key] = lst[:i] + lst[i+1:]
                    break # only remove first instance
        self.check_char_limit()
        self.update_media_buttons()
        self.app.notify(f'Removed {item_id}')

    def edit_media_alt(self, item_id: str, alt: str):
        for key, lst in self.media.items():
            for item in lst:
                if item.get('id') == item_id:
                    item['alt'] = alt

    def update_media_buttons(self):
        """Enable or disable media buttons, based on media currently attached to post"""

        for media_type, attachments in self.media.items():
            btn = self.query_one(f"#{media_type[:-1]}-add-btn", Button)
            other_media = any(v for k, v in self.media.items() if k != media_type)
            btn.disabled = len(attachments) >= self.MEDIA_LIMITS[media_type] or other_media

    def check_has_media(self) -> bool:
        """Check if there is currently media attached to the post"""
        return any(v for k, v in self.media.items())

    def check_submit_allowed(self) -> bool:
        """Check if post submission is allowed"""
        text_area = self.query_one("#compose-input", TextArea)
        return 0 < len(text_area.text) <= self.char_limit or self.check_has_media()

    def check_char_limit(self) -> None:
        """Update character counter display and submit button state."""

        char_counter = self.query_one("#compose-char-counter", Static)
        submit_button = self.query_one("#compose-submit-btn", Button)

        self.update_char_counter(counter=char_counter, button=submit_button, empty_ok_when=self.check_has_media())


    class EmbedLabel(Label):
        """Common methods for labels displaying embedded content"""

        can_focus = True

        def __init__(self, media_item: dict, **kwargs):
            self.media_item = media_item
            super().__init__(**kwargs)

        def on_focus(self) -> None:
            """Manually add focused class for default non-focusable widget"""
            self.add_class("focused")

        def on_blur(self) -> None:
            """Manually remove focused class for default non-focusable widget"""
            self.remove_class("focused")

        def _compose_parent(self) -> "ComposeWidget":
            """Get ComposeWidget parent"""
            parent_widget = self.parent
            while parent_widget is not None:
                if isinstance(parent_widget, ComposeWidget):
                    return parent_widget
                parent_widget = parent_widget.parent

        def action_remove_embed(self):
            """Action to remove widget and delete stored media from parent"""
            compose_widget = self._compose_parent()
            if compose_widget:
                compose_widget.remove_attached_file(self.media_item['id'])
            return self.remove()

    class LinkLabel(EmbedLabel):
        """Label to display external link embed"""

        BINDINGS = [
            Binding("r", "remove_embed", "Remove"),
        ]

        def render(self):
            text = Text()
            text.append(Text.from_markup(f'[@click=remove_embed(\'{self.media_item['id']}\')]❌[/]  '))
            if self.media_item['title']:
                text.append(self.media_item['title'] + '  ', style=f'{self.app.theme_variables['text-primary']} italic')
            text.append(self.media_item['url'], style=f'{self.app.theme_variables['text-secondary']} italic')
            return text

    class MediaFileLabel(EmbedLabel):
        """Label to display attached media file"""

        BINDINGS = [
            Binding("r", "remove_embed", "Remove"),
            Binding("a", "edit_alt", "Alt text"),
        ]

        def render(self):
            text = Text()
            text.append(Text.from_markup(f'[@click=remove_embed(\'{self.media_item['id']}\')]❌[/]  '))
            text.append(Text.from_markup(f'[@click=edit_alt(\'{self.media_item['id']}\')]{'add' if not self.media_item['alt'] else 'edit'} alt[/]  '))
            text.append(self.media_item['path'], style=f'{self.app.theme_variables['text-secondary']} italic')
            return text

        @work
        async def action_edit_alt(self) -> None:
            """Action to edit alt text associated with an attached media file"""
            if alt := await self.app.push_screen_wait(AltComposeScreen(self.media_item)):
                self.media_item['alt'] = alt
                self.refresh()
                compose_widget = self._compose_parent()
                compose_widget.edit_media_alt(item_id=self.media_item['id'], alt=alt)
                self.app.notify('Updated alt text')


    class ReferencePostEmbed(Widget):
        """Content of original post being replied to or quoted"""

        def __init__(self, post: Post, **kwargs):
            self.post = post
            super().__init__(**kwargs)

        def render(self) -> Panel:
            author = self.post.display_name if self.post.display_name else self.post.handle
            title = Text(author, style=f'bold {self.app.theme_variables["foreground"]}')
            body = Text(self.post.post_content)
            return Panel(
                body,
                title=title,
                title_align="left",
                box=box.SIMPLE,
                padding=(0, 2),
            )
