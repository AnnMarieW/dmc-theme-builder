import json
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, Input, Output, State, callback
from components import progress_card
from components import theme_switch
from components import figures
from components import authentication
from components import sample_components
from components import stepper
from components import date_picker

_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

colors = dmc.DEFAULT_THEME["colors"]
color_picker_value_mapping = {color: codes[6] for color, codes in colors.items()}
theme_name_mapping = {codes[6]: color for color, codes in colors.items()}
radius_name_mapping = {1: "xs", 2: "sm", 3: "md", 4: "lg", 5: "xl"}

color_picker = dmc.Stack(
    [
        dmc.Text("Select a theme color", size="xs"),
        dmc.ColorPicker(
            id="color-picker",
            size="sm",
            withPicker=False,
            swatches=list(color_picker_value_mapping.values()),
            swatchesPerRow=7,
            value=color_picker_value_mapping["green"],
        ),
    ]
)


def make_slider(title, id):
    return dmc.Stack(
        [
            dmc.Text(title, size="xs", fw=500),
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
            size="xs",
            children=[
                dmc.Box(
                    [
                        color_picker,
                        make_slider("Select Radius", "radius"),
                        make_slider("Select Shadow", "shadow"),
                        theme_switch.theme_toggle,
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
                dmc.CodeHighlight(id="json", code="", language="json", h=300),
                dmc.Text("dmc.MantineProvider(theme=theme)"),
            ],
            zIndex=1000,
            withCloseButton=False,
            yOffset="0vh",
            id="modal-code",
        ),
    ]
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
        dmc.Title("Dash Mantine Components Theme Builder", order=1, mt="lg"),
        dmc.Title(
            "Set default color, radius, shadow, and color scheme", order=3, mb="lg"
        ),
        dmc.Group([customize_theme, see_code]),
        dmc.Divider(size="md", mt="lg"),
        dmc.Space(h=60),
        sample_app,
    ],
    fluid=True,
    mb="lg",
)

app.layout = dmc.MantineProvider(
    layout,
    theme={
        "primaryColor": "indigo",
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
    theme["primaryColor"] = theme_name_mapping[color]
    theme["defaultRadius"] = radius_name_mapping[radius]
    theme["components"]["Card"]["defaultProps"]["shadow"] = radius_name_mapping[shadow]
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
def modal_demo(n, opened):
    return not opened


if __name__ == "__main__":
    app.run(debug=True)
