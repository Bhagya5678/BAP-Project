import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objs as go

dash.register_page(
    __name__,
    path="/facultycontrast",
    name="Faculty Contrast",
    suppress_callback_exceptions=True,
)

data = {
    "A": [3, 1, 0, 5, 4, 2],
    "B": [2, 4, 1, 0, 3, 5],
    "C": [0, 5, 4, 2, 1, 3],
    "D": [4, 1, 2, 5, 0, 3],
    "E": [2, 4, 5, 0, 3, 1],
    "F": [5, 3, 0, 4, 1, 2],
    "G": [3, 1, 5, 4, 0, 2],
    "H": [1, 0, 4, 5, 2, 3],
}

avg_metrics = {
    "A": [4, 4.2, 4.3, 4.4, 4.5, 4.6],
    "B": [3.8, 3.9, 3.7, 3.8, 3.9, 4],
    "C": [4.2, 4.3, 4.4, 4.5, 4.6, 4.7],
    "D": [4, 4.1, 4.2, 4.3, 4.4, 4.5],
    "E": [3.9, 4, 4.1, 4.2, 4.3, 4.4],
    "F": [4.1, 4.2, 4.3, 4.4, 4.5, 4.6],
    "G": [4.2, 4.3, 4.4, 4.5, 4.6, 4.7],
    "H": [4.1, 4.2, 4.3, 4.4, 4.5, 4.6],
}

categories = [
    "Subject Knowledge",
    "Regularity & Punctuality",
    "Communication Skills",
    "Syllabus Coverage",
    "Interest Generated in Subject",
    "Faculty Preparation",
]


@callback(
    Output("graph-container", "figure"),
    [Input("dropdown1", "value"), Input("dropdown2", "value")],
)
def update_graph(value1, value2):
    # Create radar plot
    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=avg_metrics[value1], theta=categories, fill="toself", name=f"Faculty {value1}"
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=avg_metrics[value2], theta=categories, fill="toself", name=f"Faculty {value2}"
        )
    )

    fig.update_layout(
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=0),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                gridcolor="white",
                tickfont=dict(color="black", size=1),
            ),
            angularaxis=dict(
                tickfont=dict(color="white", size=16),
                tickmode="array",
                tickvals=categories,
                ticktext=categories,
                gridcolor="white",
            ),
            bgcolor="#212529",
        ),
        showlegend=False,
        paper_bgcolor="#212529",  # Setting paper background color
        plot_bgcolor="#212529",
        font=dict(color="white"),  # Change font color to white
    )
    return fig


@callback(
    [Output("faculty1-name", "children"), Output("faculty2-name", "children")],
    [Input("dropdown1", "value"), Input("dropdown2", "value")],
)
def update_faculty_names(value1, value2):
    return f"Faculty {value1}", f"Faculty {value2}"


@callback(
    Output("avg-metrics-1", "children"),
    [Input("dropdown1", "value")],
)
def update_avg_metrics_1(value):
    avg_values = avg_metrics[value]
    metric_elements = []
    for i, metric in enumerate(categories):
        metric_elements.append(
            html.P(
                children=[
                    html.Span(metric, style={"font-weight": "bold"}),
                    html.Span(": ", style={"margin-right": "4px"}),
                    html.Span(avg_values[i], style={"font-weight": "normal"}),
                ],
                style={"margin-bottom": "4px"},
            )
        )
    return metric_elements


@callback(
    Output("avg-metrics-2", "children"),
    [Input("dropdown2", "value")],
)
def update_avg_metrics_2(value):
    avg_values = avg_metrics[value]
    metric_elements = []
    for i, metric in enumerate(categories):
        metric_elements.append(
            html.P(
                children=[
                    html.Span(metric, style={"font-weight": "bold"}),
                    html.Span(": ", style={"margin-right": "4px"}),
                    html.Span(avg_values[i], style={"font-weight": "normal"}),
                ],
                style={"margin-bottom": "4px"},
            )
        )
    return metric_elements

team_stats = {
    'Team': ['Team A', 'Team B'],
    'Shots': [20, 10],
    'Color': ['blue', 'red']
}


####################### PAGE LAYOUT #############################
layout = html.Div(
    className="container mt-5",
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-2",
                    children=[
                        html.H2(id="faculty1-name", className="mb-4"),
                        dcc.Dropdown(
                            id="dropdown1",
                            options=[
                                {
                                    "label": html.Span(
                                        i,
                                        style={
                                            "padding-left": "4px",
                                            "backgroundColor": "#212529",
                                            "color": "white",
                                            "width": "100%",
                                            "height": "100%",
                                        },
                                    ),
                                    "value": i,
                                }
                                for i in list("ABCDEFGH")
                            ],
                            value="A",
                            clearable=False,
                            style={"width": "100%", "backgroundColor": "#212529"},
                            className="bg-dark text-light border border-light",
                        ),
                        html.Div(id="avg-metrics-1", style={"margin-top": "16px"}),
                    ],
                ),
                # radar
                html.Div([dcc.Graph(id="graph-container")], className="col-8"),
                html.Div(
                    className="col-2",
                    children=[
                        html.H2(id="faculty2-name", className="mb-4"),
                        dcc.Dropdown(
                            id="dropdown2",
                            options=[
                                {
                                    "label": html.Span(
                                        i,
                                        style={
                                            "padding-left": "4px",
                                            "backgroundColor": "#212529",
                                            "color": "white",
                                            "width": "100%",
                                            "height": "100%",
                                        },
                                    ),
                                    "value": i,
                                }
                                for i in list("ABCDEFGH")
                            ],
                            value="B",
                            clearable=False,
                            style={"width": "100%", "backgroundColor": "#212529"},
                            className="bg-dark text-light border border-light",
                        ),
                        html.Div(id="avg-metrics-2", style={"margin-top": "16px"}),
                    ],
                ),
            ],
        ),
    ],
)
