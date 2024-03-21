"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_simpleicons import simpleicons

filename = f"{config.app_name}/{config.app_name}.py"


class Brands(rx.State):
    """The app state."""


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
            rx.hstack(simpleicons("7zip", brand_color=True, size=90),
                      simpleicons(tag="Dell", brand_color=True, size=90),
                      simpleicons(tag="Microsoft", brand_color=True, size=90),
                      simpleicons(tag="Amazon", brand_color=True, size=90),
                      simpleicons(tag="Apple", brand_color=True, size=90),
                      simpleicons(tag="Spotify", brand_color=True, size=90),
                      simpleicons(tag="3m", brand_color=True, size=90),
                      simpleicons(tag="bitwarden", brand_color=True, size=90),
                      simpleicons(tag="Dotenv", brand_color=True, size=90),
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
