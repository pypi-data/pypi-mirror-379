from textual.containers import Container
from rich.text import Text
from rich.panel import Panel
from rich.console import Console, ConsoleOptions, RenderResult
from rich import box


ROOT_REPLY_BOX = box.Box(
    "╭─┬╮\n"
    "│ ││\n"
    "├─┼┤\n"
    "│ ││\n"
    "├─┼┤\n"
    "├─┼┤\n"
    "│ ││\n"
    "│ ││\n"
)

PARENT_REPLY_BOX = box.Box(
    "│ ││\n"
    "│ ││\n"
    "├─┼┤\n"
    "│ ││\n"
    "├─┼┤\n"
    "├─┼┤\n"
    "│ ││\n"
    "│ ││\n"
)

REPLY_BOX = box.Box(
    "│ ││\n"
    "│ ││\n"
    "├─┼┤\n"
    "│ ││\n"
    "├─┼┤\n"
    "├─┼┤\n"
    "│ ││\n"
    "╰─┴╯\n"
)

THREAD_CONTEXT_BOX = box.Box(
    "· ··\n"
    "· ··\n"
    "· ··\n"
    "· ··\n"
    "· ··\n"
    "· ··\n"
    "· ··\n"
    "· ··\n"
)

class BreakpointContainer(Container):
    """Container class with vertical/horizontal layout determined by breakpoints. Layout set in CSS file."""
    pass

class SplitTitlePanel(Panel):
    """Rich Panel class with ability to set simultaneous left aligned and right aligned titles."""

    def __init__(self, renderable="", *, left_title: Text | None = None, right_title: Text | None = None, **kwargs):
        self.left_title = left_title
        self.right_title = right_title

        # Only use split title behavior if we have both left and right titles
        if left_title and right_title:
            kwargs['title'] = "" # replaced during rendering

        elif left_title:
            kwargs['title'] = left_title
            kwargs['title_align'] = "left"
        elif right_title:
            kwargs['title'] = right_title
            kwargs['title_align'] = "right"

        super().__init__(renderable, **kwargs)

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        # Only use custom rendering if we have both left and right titles
        if self.left_title and self.right_title:

            # Convert titles to Text objects to get proper length
            left_text = Text.from_markup(str(self.left_title)) if self.left_title else Text("")
            right_text = Text.from_markup(str(self.right_title)) if self.right_title else Text("")

            left_len = len(left_text.plain)
            right_len = len(right_text.plain)

            title_width = options.max_width - 4  # Account for panel borders
            buffer_spaces = 5 # Account for buffer spaces
            title_separation = max(1, title_width - left_len - right_len - buffer_spaces)

            # Create the title with buffer spaces and border characters
            title_text = Text()
            title_text.append_text(self.left_title)
            title_text.append(" ")
            border_char = "─"  # default horizontal border characters for the middle section
            if hasattr(self.box, 'top') and self.box.top:
                border_char = self.box.top
            title_text.append(border_char * title_separation, style=self.border_style)
            title_text.append(" ")
            title_text.append_text(self.right_title)

            panel = Panel(
                self.renderable,
                title=title_text,
                subtitle=self.subtitle,
                subtitle_align=self.subtitle_align,
                border_style=self.border_style,
                box=self.box,
                safe_box=self.safe_box,
                expand=self.expand,
                padding=self.padding,
                width=self.width,
                height=self.height,
                style=self.style,
                highlight=self.highlight,
            )
            yield from panel.__rich_console__(console, options)

        else:
            yield from super().__rich_console__(console, options)
