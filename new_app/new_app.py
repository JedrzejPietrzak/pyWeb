"""Welcome to """

from new_app import styles

# Import all the pages.
from new_app.pages import *

import reflex as rx

# Create the app and compile it.

def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


app = rx.App(style=styles.base_style)
app.add_page(index)
app.compile()
