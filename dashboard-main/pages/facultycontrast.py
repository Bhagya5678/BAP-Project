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

avg_metrics = {
    "A": [4.2, 3.7, 4.3, 4.4, 3.6, 4.6],
    "B": [4.4, 4.3, 3.6, 3.8, 4.6, 4],
    "C": [3.7, 4.6, 4.4, 4.1, 4.7, 4.2],
    "D": [4, 3.4, 4.2, 4.5, 3.7, 4.3],
    "E": [4.9, 4.6, 3.2, 4.2, 3.4, 3.9],
    "F": [3.7, 4.2, 4.8, 3.8, 3.8, 3.3],
    "G": [4.6, 4.5, 4.4, 4.1, 3.7, 4],
    "H": [4.1, 4.3, 3.9, 4.4, 3.6, 4.2],
}

categories = [
    "Subject Knowledge",
    "Regularity & Punctuality",
    "Communication Skills",
    "Syllabus Coverage",
    "Interest Generated in Subject",
    "Faculty Preparation",
]

colors = {
    "A": "#ffea00",  # yllow
    "B": "#db00b6",  # pink
    "C": "#2d00f7",  # orange
    "D": "#fc2f00",  # red
    "E": "#ff0000",  # purple
    "F": "#023e8a",  # blue
    "G": "#40916c",  # dark green
    "H": "#07c8f9",  # blue light
}


@callback(
    Output("graph-container", "figure"),
    [Input("dropdown1", "value"), Input("dropdown2", "value")],
)
def update_graph(value1, value2):
    # Create radar plot
    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=avg_metrics[value1],
            theta=categories,
            fill="toself",
            line_color=colors[value1],
            name=f"Faculty {value1}",
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=avg_metrics[value2],
            theta=categories,
            fill="toself",
            line_color=colors[value2],
            name=f"Faculty {value2}",
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
    return (
        html.H2(f"Faculty {value1}", style={"color": colors[value1]}),
        html.H2(f"Faculty {value2}", style={"color": colors[value2]}),
    )


@callback(
    Output("avg-metrics-1", "children"),
    [Input("dropdown1", "value")],
)
def update_avg_metrics_1(value):
    avg_values = avg_metrics[value]
    return [
        html.Div(avg_values[i], className="m-4", style={"color": colors[value]})
        for i in range(len(categories))
    ]


@callback(
    Output("avg-metrics-2", "children"),
    [Input("dropdown2", "value")],
)
def update_avg_metrics_2(value):
    avg_values = avg_metrics[value]
    return [
        html.Div(avg_values[i], className="m-4", style={"color": colors[value]})
        for i in range(len(categories))
    ]


####################### PAGE LAYOUT #############################
layout = html.Div(
    className="container mt-5",
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-2 d-flex flex-column justify-content-center align-items-center",
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
                            className="bg-dark text-light",
                        ),
                    ],
                ),
                # radar
                html.Div([dcc.Graph(id="graph-container")], className="col-8"),
                html.Div(
                    className="col-2 d-flex flex-column justify-content-center align-items-center",
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
                            className="bg-dark text-light",
                        ),
                    ],
                ),
            ],
        ),  # div 1
        html.Div(
            className="row mt-4",
            children=[
                html.Div(
                    id="avg-metrics-1", className="col-3 text-center fw-semibold fs-4"
                ),
                html.Div(
                    className="col-6 text-center",
                    children=[
                        html.Div(metric, className="m-4 fw-semibold fs-4")
                        for metric in categories
                    ],
                ),
                html.Div(
                    id="avg-metrics-2", className="col-3 text-center fw-semibold fs-4"
                ),
            ],
        ),
    ],
)
