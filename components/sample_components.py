import dash_mantine_components as dmc


card = dmc.Card(
    [
        dmc.CardSection("Sample Components", withBorder=True, p="md"),
        dmc.Group(
            [
                dmc.Button("button", mr="sm"),
                dmc.Badge("Badge", mr="sm"),
                dmc.Chip("Chip", checked=True),
                dmc.Checkbox(label="chekbox", checked=True),
                dmc.Radio(label="Radio", value="Radio"),
                dmc.Switch(label="Switch", checked=True),
                dmc.SegmentedControl(data=["A", "B", "C", "D"]),
                dmc.Select(data=["A", "B", "C", "D"], value="B", label="Select:"),
                dmc.Slider(w=200, value=25),
            ],
            p="md",
        ),
    ],
    w=400,
    h=400,
    withBorder=True,
)
