import dash_mantine_components as dmc

stepper = dmc.Stepper(
    active=1,
    orientation="vertical",
    children=[
        dmc.StepperStep(label="First step", description="Create an account", pt="lg"),
        dmc.StepperStep(label="Second step", description="Verify email"),
        dmc.StepperStep(label="Third", description="Get full access"),
        dmc.StepperStep(label="Final step", description="Explore App"),
    ],
)

card = dmc.Card(dmc.Center(stepper), w=400, h=400, withBorder=True)
