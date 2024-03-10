"""Reflex custom component Simpleicons."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx
from reflex.vars import Var


# Some libraries you may want to wrap may require dynamic imports.
# This is because they they may not be compatible with Server-Side Rendering (SSR).
# To handle this in Reflex all you need to do is subclass NoSSRComponent instead.
# For example:
# from reflex.components.component import NoSSRComponent
# class Simpleicons(NoSSRComponent):
#     pass


class Simpleicons(rx.Component):
    """Simpleicons component."""

    # The React library to wrap.
    library = "@icons-pack/react-simple-icons"

    # The React component tag.
    tag = "None"

    # Default Color.
    color = f"var(--accent-a10)"

    # Default Size.
    size = 24

    @classmethod
    def create(cls, *children, **props):
        if len(children) == 1 and type(children[0]) == str:
            props["tag"] = f"Si{children[0].capitalize()}"
        return super().create(*children, **props)
    # If the tag is the default export from the module, you must set is_default = True.
    # This is normally used when components don't have curly braces around them when importing.
    # is_default = True

    # If you are wrapping another components with the same tag as a component in your project
    # you can use aliases to differentiate between them and avoid naming conflicts.
    # alias = "OtherSimpleicons"

    # The props of the React component.
    # Note: when Reflex compiles the component to Javascript,
    # `snake_case` property names are automatically formatted as `camelCase`.
    # The prop names may be defined in `camelCase` as well.
    # some_prop: rx.Var[str] = "some default value"
    # some_other_prop: rx.Var[int] = 1

    # By default Reflex will install the library you have specified in the library property.
    # However, sometimes you may need to install other libraries to use a component.
    # In this case you can use the lib_dependencies property to specify other libraries to install.
    # lib_dependencies: list[str] = []

    # Event triggers, I did not understand the wording of the doc.
    # def get_event_triggers(self) -> dict[str, Any]:
    #     return {
    #         **super().get_event_triggers(),
    #         "on_change": lambda e0: [e0],
    #     }

    # To add custom code to your component
    # def _get_custom_code(self) -> str:
    #     return "const customCode = 'customCode';"


simpleicons = Simpleicons.create
