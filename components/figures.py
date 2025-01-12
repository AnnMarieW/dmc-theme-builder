import dash_mantine_components as dmc

data = [
    {"date": "Mar 22", "Apples": 2890, "Oranges": 2338, "Tomatoes": 2452},
    {"date": "Mar 23", "Apples": 2756, "Oranges": 2103, "Tomatoes": 2402},
    {"date": "Mar 24", "Apples": 3322, "Oranges": 986, "Tomatoes": 1821},
    {"date": "Mar 25", "Apples": 3470, "Oranges": 2108, "Tomatoes": 2809},
    {"date": "Mar 26", "Apples": 3129, "Oranges": 1726, "Tomatoes": 2290},
]

chart = dmc.LineChart(
    h=250,
    dataKey="date",
    data=data,
    series=[{"name": "Apples"}],
)

card = dmc.Card(
    dmc.Box([dmc.Text("Revenue", p="lg", mb="lg"), chart]),
    w=400,
    h=400,
    withBorder=True,
)
