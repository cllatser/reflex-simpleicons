"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_simpleicons import simpleicons

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Test your custom component by editing ",
                rx.code(filename),
                font_size="2em",
            ),
            rx.hstack(
                simpleicons("facebook"),
                simpleicons("microsoft"),
                simpleicons("1001tracklists"),
                simpleicons("7zip"),
                simpleicons("Python", size=90, color="currentColor"),
                width="100%",
                justify="center"
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
