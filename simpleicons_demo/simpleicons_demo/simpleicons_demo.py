"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_simpleicons import simpleicons

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


@rx.page(title="Reflex Simple Icons")
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
                simpleicons(tag="Amazon"),
                simpleicons("microsoft"),
                simpleicons(tag="jetbrains"),
                simpleicons("7zip"),
                simpleicons("Python"),
                simpleicons("linux"),
                width="100%",
                justify="center",
                spacing="7"
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()

