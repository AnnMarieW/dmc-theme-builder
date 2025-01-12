import dash_mantine_components as dmc

card_progress = dmc.Card(
    [
        dmc.Text("Monthly goal", fz="xs", tt="uppercase", fw=700, c="dimmed"),
        dmc.Text("$5.431 / $10.000", fz="lg", fw=500),
        dmc.Progress(value=54.31, mt="md", size="lg"),
    ],
    withBorder=True,
    padding="xl",
    w=300,
)


card_ring_progress = dmc.Card(
    [
        dmc.Text("Monthly goal", fz="xs", tt="uppercase", fw=700, c="dimmed"),
        dmc.Text("$5.431 / $10.000", fz="lg", fw=500),
        dmc.SemiCircleProgress(value=54, label="54%", labelPosition="center"),
    ],
    withBorder=True,
    padding="xl",
    w=300,
)
dmc.SemiCircleProgress(value=30, label="Center", labelPosition="center")

card = dmc.Card(
    dmc.Center(dmc.Stack([card_progress, card_ring_progress])),
    w=400,
    h=400,
    withBorder=True,
)
