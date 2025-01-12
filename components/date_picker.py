import dash_mantine_components as dmc

card = dmc.Card(
    dmc.DatePickerInput(
        label="Select Dates",
        value=["2025-01-02", "2025-01-12"],
        type="range",
        popoverProps={"opened": True, "withinPortal": False},
    ),
    h=400,
    w=400,
    withBorder=True,
)
