import json
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, _dash_renderer, Input, Output, State, callback
from components import progress_card
from components import theme_switch
from components import figures
from components import authentication
from components import sample_components
from components import stepper
from components import date_picker
import colorsys


_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

colors = dmc.DEFAULT_THEME["colors"]
color_picker_value_mapping = {color: codes[5] for color, codes in colors.items() if color != "dark"}
theme_name_mapping = {codes[5]: color for color, codes in colors.items() if color != "dark"}
size_name_mapping = {1: "xs", 2: "sm", 3: "md", 4: "lg", 5: "xl"}

color_picker = dmc.Stack(
    [
        dmc.Text("Color", size="xs"),
        dmc.ColorPicker(
            id="color-picker",
            size="sm",
            swatches=list(color_picker_value_mapping.values()),
            swatchesPerRow=7,
            value=color_picker_value_mapping["green"],
        ),
    ]
)


def generate_color_shades(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)

    shades_l = [1.0 - (i/9) for i in range(10)]
    shades_l[4] = l  # Put the original color in the middle

    shades = []
    for val in shades_l:
        rr, gg, bb = colorsys.hls_to_rgb(h, val, s)
        new_hex = f"#{int(rr*255):02x}{int(gg*255):02x}{int(bb*255):02x}"
        shades.append(new_hex)

    return shades

def make_slider(title, id):
    return dmc.Stack(
        [
            dmc.Text(title, size="sm"),
            dmc.Slider(
                min=1,
                max=5,
                value=2,
                id=id,
                updatemode="drag",
                styles={"markLabel": {"display": "none"}},
                marks=[
                    {"value": 1, "label": "xs"},
                    {"value": 2, "label": "sm"},
                    {"value": 3, "label": "md"},
                    {"value": 4, "label": "lg"},
                    {"value": 5, "label": "xl"},
                ],
            ),
        ],
        mt="md",
    )


customize_theme = dmc.Box(
    [
        dmc.Button("Customize Theme", id="modal-demo-button"),
        dmc.Modal(
            id="modal-customize",
            size="sm",
            children=[
                dmc.Box(
                    [
                        color_picker,
                        make_slider("Radius", "radius"),
                        make_slider("Shadow", "shadow"),
                        dmc.Group([theme_switch.theme_toggle, dmc.Text("light/dark color scheme", size="sm", pt="sm")])
                    ],
                    bd="1px solid gray.3",
                    p="sm",
                )
            ],
            zIndex=1000,
            withCloseButton=False,
            yOffset="0vh",
            styles={"overlay": {"background": "rgba(0, 0, 0, 0.3)"}},
        ),
    ]
)


see_code = dmc.Box(
    [
        dmc.Button("copy theme code", id="modal-code-button", variant="outline"),
        dmc.Modal(
            [
                dmc.CodeHighlight(id="json", code="", language="json", h=300, style={"overflow": "auto"}),
                dmc.Text("dmc.MantineProvider(theme=theme)"),
            ],
            zIndex=1000,
            withCloseButton=False,
            yOffset="0vh",
            id="modal-code",
        ),
    ]
)

github_link =  dmc.Anchor(
    dmc.ActionIcon(
        DashIconify(icon= "radix-icons:github-logo", width=25), variant="transparent", size="lg"
    ),
    href="https://github.com/AnnMarieW/dmc-theme-builder",
    target="_blank",
    visibleFrom="xs",
)


sample_app = dmc.Box(
    [
        dmc.Group(
            [
                sample_components.card,
                progress_card.card,
                figures.card,
                date_picker.card,
                authentication.card,
                stepper.card,
            ],
            gap="lg",
            justify="center",
        ),
    ]
)

layout = dmc.Container(
    [
        dmc.Group([
            dmc.Title("Dash Mantine Components Theme Builder", order=1, mt="lg"),
            github_link
        ], justify="space-between"),
        dmc.Title(
            "Set default color, radius, shadow, and color scheme", order=3, mb="lg"
        ),
        dmc.Group([customize_theme, see_code]),
        dmc.Divider(size="md", mt="lg"),
        dmc.Space(h=60),
        sample_app,
    ],
 #   fluid=True,
    mb="lg",
)

app.layout = dmc.MantineProvider(
    layout,
    theme={
        "primaryColor": "green",
        "defaultRadius": "sm",
        "components": {"Card": {"defaultProps": {"shadow": "sm"}}},
    },
    forceColorScheme="light",
    id="mantine-provider",
)


@callback(
    Output("mantine-provider", "theme"),
    Output("json", "code"),
    Input("color-picker", "value"),
    Input("radius", "value"),
    Input("shadow", "value"),
    State("mantine-provider", "theme"),
)
def update(color, radius, shadow, theme):
    try:
        theme["primaryColor"] = theme_name_mapping[color]
    except KeyError:
        new_colors = generate_color_shades(color)
        theme["colors"] = {
            "myColor": new_colors
        }
        theme["primaryColor"] = "myColor"
        theme["primaryShade"] = 4
    theme["defaultRadius"] = size_name_mapping[radius]
    theme["components"]["Card"]["defaultProps"]["shadow"] = size_name_mapping[shadow]
    return theme, "theme=" + json.dumps(theme, indent=4)


@callback(
    Output("modal-customize", "opened"),
    Input("modal-demo-button", "n_clicks"),
    State("modal-customize", "opened"),
    prevent_initial_call=True,
)
def modal_demo(n, opened):
    return not opened


@callback(
    Output("modal-code", "opened"),
    Input("modal-code-button", "n_clicks"),
    State("modal-code", "opened"),
    prevent_initial_call=True,
)
def modal_code(n, opened):
    return not opened


if __name__ == "__main__":
    app.run(debug=True)
