"""Reflex custom component Simple Icons."""
from typing import Union

import reflex as rx
from .data.brands_color import default_color
from .data.brands_svg import brands


def simpleicons(tag="simpleicons", color: Union[str, rx.Color] ="", brand_color=False, size=48) -> rx.Component:
    """Create a Simple Icon"""
    if tag.lower() in brands:
        # Checks if the entered name exists in the dictionary
        if color == "":
            if brand_color:
                # If the user has not entered a custom color, it will look to see if the user wants to use the
                # brand's default color.
                if tag.lower() in default_color:
                    color = default_color[tag.lower()]
                else:
                    color = ""
            else:
                color = color
    else:
        # If the name entered in the dictionary is not found, it will prompt the user to look up a correct name.
        raise ValueError(f"Brand: {tag} it is not correct, check it in https://simpleicons.org")

    return rx.el.svg(
        # Returns an svg component
        rx.el.svg.path(d=brands[tag.lower()]),
        role="img",
        width=f"{size}px",
        color=color,
        custom_attrs={
            "fill": "currentColor",
            "viewBox": "0 0 24 24",
            "xmlns": "http://www.w3.org/2000/svg"
        }
    )
