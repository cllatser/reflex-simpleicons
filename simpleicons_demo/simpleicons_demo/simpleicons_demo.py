"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_simpleicons import simpleicons


@rx.page(title="Reflex Simple Icons")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.heading("Simple Icons Custom Component", size="7"),
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
