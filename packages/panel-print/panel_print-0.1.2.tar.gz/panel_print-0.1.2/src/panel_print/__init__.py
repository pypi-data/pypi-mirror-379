from typing import Any

from rich import print
from rich.console import Group
from rich.panel import Panel
from rich.pretty import Pretty, pprint
from itables import init_notebook_mode, show, options

init_notebook_mode(all_interactive=True)
options.columnControl = [  # pyright: ignore[reportAttributeAccessIssue]
    "searchDropdown",
]
options.buttons = [
    "pageLength",
    "copyHtml5",
    "csvHtml5",
    "excelHtml5",
]
options.footer = False
options.maxBytes = "1MB"
options.showIndex = True
options.classes = "display nowrap compact"

__version__ = "0.1.0"


def pp(*objects: Any, max_length: int = 20) -> None:
    """
    Pretty print objects in a panel format.

    Args:
        *objects (Any): An object or objects to pretty print.
        max_length (int, optional): Maximum length of containers before abbreviating. Defaults to 20.
    """
    if not objects:
        return

    print(
        Panel(
            Group(
                *(
                    Pretty(
                        obj,
                        expand_all=True,
                        max_length=max_length,
                    )
                    for obj in objects
                )
            ),
            expand=False,
            subtitle_align="center",
        )
    )


__all__ = ["pp", "print", "pprint", "show"]
