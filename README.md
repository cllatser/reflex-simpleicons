# Reflex Simple Icons

A Reflex wrapper for [Simple Icons](https://simpleicons.org/), the best library of SVG icons from the most popular brands. 

## Installation

```bash
pip install reflex-simpleicons
```

## Usage

Import like so:

```python
from reflex_simpleicons import simpleicons
```

Search for the logo you want to use on [Simple Icons](https://simpleicons.org/) and click on the name. This will copy its name and you can paste it into the component.

![reflex-simpleicons-web.PNG](img%2Freflex-simpleicons-web.PNG)

Use in your Reflex UI:

By default it will have the color of the main text, switching automatically between light and dark mode. The default size is 48px.

```python
simpleicons("python")
```
![python-icon.PNG](img%2Fpython-icon.PNG)

## Styling

You can customize the color and size of the icon by passing the color and size properties.

```python
simpleicons("python"),
simpleicons("python", color="#3776AB", size=24),
simpleicons("python", color="red", size=48),
simpleicons("python", color="#ECD53F", size=67),
simpleicons("python", color="#5F259F", size=97),
```
![python-icon-size-colors.PNG](img%2Fpython-icon-size-colors.PNG)

## Example

If you want to use the default HEX color of the brand you can add the property:

```python
brand_color=True
```

```python
import reflex as rx
from reflex_simpleicons import simpleicons


def demo_brands() -> rx.Component:
    return rx.el.div(
        simpleicons("7zip", brand_color=True, size=90),
        simpleicons(tag="Dell", brand_color=True, size=90),
        simpleicons(tag="Microsoft", brand_color=True, size=90),
        simpleicons(tag="Amazon", brand_color=True, size=90),
        simpleicons(tag="Apple", brand_color=True, size=90),
        simpleicons(tag="Spotify", brand_color=True, size=90),
        simpleicons(tag="3m", brand_color=True, size=90),
        simpleicons(tag="bitwarden", brand_color=True, size=90),
        simpleicons(tag="Dotenv", brand_color=True, size=90),
        class_name="demo-brands"
    )
```
![brands_color.PNG](img%2Fbrands_color.PNG)

## Disclaimer

By using this wrapper to access and use logos, you agree to the following terms and conditions:

1. Intellectual property: Logos and trademarks found in this wrapper are the property of their respective owners. You do not acquire any ownership rights to the logos by using this plugin.

2. Responsible use: You agree to use the logos responsibly and in accordance with intellectual property laws. You may not modify, distribute, reproduce, or use the logos in any way that may infringe the rights of their owners.

3. Owner's permission: You are responsible for obtaining permission from the trademark owner before using their logo in any commercial or advertising context. The plugin does not give you permission to use the logos in this way.

4. Limitation of liability: The plugin creators are not responsible for the misuse of logos by users. You are solely responsible for any damage or harm you may cause to brand owners by misusing logos.

5. Indemnity: You agree to indemnify and hold harmless the wrapper creators from any claims, damages, or losses that may arise from your misuse of logos.

By using this wrapper, you represent that you have read and agree to the terms and conditions of this disclaimer.

Recommendation: It is recommended that users research the logo usage policies of the brands they are interested in before using their logos.