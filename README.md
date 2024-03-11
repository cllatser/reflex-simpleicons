# Reflex Simple Icons

A Reflex wrapper for [Simple Icons](https://simpleicons.org/), the best library of SVG icons from the most popular brands. 

This wrap uses the [react-simple-icons](https://github.com/icons-pack/react-simple-icons)

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

![reflex-simpleicons-web.PNG](..%2F..%2F..%2F..%2FDownloads%2Freflex-simpleicons-web.PNG)

Use in your Reflex UI:

```python
simpleicons("python")
```
![python-icon.PNG](..%2F..%2F..%2F..%2FDownloads%2Fpython-icon.PNG)

## Styling

You can customize the color and size of the icon by passing the color and size properties.

```python
simpleicons("python"),
simpleicons("python", color="#3776AB", size=24),
simpleicons("python", color="red", size=48),
simpleicons("python", color="#ECD53F", size=67),
simpleicons("python", color="#5F259F", size=97),
```
![python-icon-size-colors.PNG](..%2F..%2F..%2F..%2FDownloads%2Fpython-icon-size-colors.PNG)

## Example

```python
import reflex as rx
from reflex_simpleicons import simpleicons


def demo_brands() -> rx.Component:
    return rx.el.div(
        simpleicons("7zip", color="#000000", size=90),
        simpleicons(tag="Dell", color="#007DB8", size=90),
        simpleicons(tag="Microsoft", color="#5E5E5E", size=90),
        simpleicons(tag="Amazon", color="#FF9900", size=90),
        simpleicons(tag="Apple", color="#000000", size=90),
        simpleicons(tag="Spotify", color="#1DB954", size=90),
        simpleicons(tag="3m", color="#FF0000", size=90),
        simpleicons(tag="Taichigraphics", color="#000000", size=90),
        simpleicons(tag="Dotenv", color="#ECD53F", size=90),
        class_name="demo-brands"
    )
```
![reflex-simpleicons.PNG](..%2F..%2F..%2F..%2FDownloads%2Freflex-simpleicons.PNG)

## Disclaimer

By using this wrapper to access and use logos, you agree to the following terms and conditions:

1. Intellectual property: Logos and trademarks found in this wrapper are the property of their respective owners. You do not acquire any ownership rights to the logos by using this plugin.

2. Responsible use: You agree to use the logos responsibly and in accordance with intellectual property laws. You may not modify, distribute, reproduce, or use the logos in any way that may infringe the rights of their owners.

3. Owner's permission: You are responsible for obtaining permission from the trademark owner before using their logo in any commercial or advertising context. The plugin does not give you permission to use the logos in this way.

4. Limitation of liability: The plugin creators are not responsible for the misuse of logos by users. You are solely responsible for any damage or harm you may cause to brand owners by misusing logos.

5. Indemnity: You agree to indemnify and hold harmless the wrapper creators from any claims, damages, or losses that may arise from your misuse of logos.

By using this wrapper, you represent that you have read and agree to the terms and conditions of this disclaimer.

Recommendation: It is recommended that users research the logo usage policies of the brands they are interested in before using their logos.