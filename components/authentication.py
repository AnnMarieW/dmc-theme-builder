import dash_mantine_components as dmc
from dash_iconify import DashIconify


card = dmc.Card(
    [
        dmc.Text("Welcome! login with:", size="lg"),
        dmc.Group(
            [
                dmc.Button(
                    leftSection=DashIconify(icon="logos:google"),
                    variant="outline",
                ),
                dmc.Button(
                    "BlueSky",
                    leftSection=DashIconify(icon="logos:bluesky"),
                    variant="outline",
                ),
            ],
            grow=True,
            my="lg",
        ),
        dmc.Divider(
            label="Or continue with email",
            variant="dashed",
            labelPosition="center",
        ),
        dmc.Stack(
            [
                dmc.TextInput(label="Email:"),
                dmc.PasswordInput(label="Password:"),
            ],
            gap="md",
        ),
        dmc.Group(
            [
                dmc.Anchor(
                    dmc.Text("Don't have an account? Register", c="gray", size="sm"),
                    href="/",
                ),
                dmc.Button("Login"),
            ],
            grow=True,
            mt="lg",
        ),
    ],
    withBorder=True,
    p="lg",
    w=400,
    h=400,
)
