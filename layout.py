from dash import Dash,html
import dash_bootstrap_components as dbc
from components import dropdown, bar_charts,scatter


def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="🏎️", className="header-emoji"),
        html.H1(
                "Car Sales Analytics", className="header-title"
                ),
        html.P(
                "Based on 2021 data set we can analyze how many models of each model were sold at what price.",
                className="header-description",
                ),
        dropdown.render(app)
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(bar_charts.render(app),lg=6),
            dbc.Col(scatter.render(app),lg=6)
            
        ],className="mt-4")
    ])