import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path="/facultyfocus/A", name="Faculty A")

faculty_data = {
    "Faculty": "A",
    "joined": 2016,
    "areas_of_interest": ["Database", "Machine Learning"],
    "subjects": ["DBMS", "OS"],
    "image": "image.png",
}

# Sample data for demonstration
data = {
    "Subject Knowledge": [4, 4.2, 4.3, 4.4, 4.5, 4.6],
    "Regularity & Punctuality": [3.8, 3.9, 3.7, 3.8, 3.9, 4],
    "Communication Skills": [4.2, 4.3, 4.4, 4.5, 4.6, 4.7],
    "Syllabus Coverage": [4, 4.1, 4.2, 4.3, 4.4, 4.5],
    "Interest Generated in Subject": [3.9, 4, 4.1, 4.2, 4.3, 4.4],
    "Faculty Preparation": [4.1, 4.2, 4.3, 4.4, 4.5, 4.6],
    "Overall Acceptance": [4.2, 4.3, 4.4, 4.5, 4.6, 4.7],
}

# Years for x-axis
years = [2019, 2020, 2021, 2022, 2023, 2024]

metrics = [
    "Subject Knowledge",
    "Regularity & Punctuality",
    "Communication Skills",
    "Syllabus Coverage",
    "Interest Generated in Subject",
    "Faculty Preparation",
    "Overall Acceptance",
]


def create_graph(selected_metric="Overall Acceptance"):
    # Create a line chart
    fig = px.line(
        x=years,
        y=data[selected_metric],
        labels={"x": "Year", "y": selected_metric},
    )
    
    fig.update_layout(
        paper_bgcolor="#212529",
        plot_bgcolor="#212529",
        xaxis=dict(tickfont=dict(color="white"), showgrid=False),
        yaxis=dict(tickfont=dict(color="white"), showgrid=False, range=[0, 5]),
    )
    return fig


@callback(Output("timeseries-graph", "figure"), [Input("metric-dropdown", "value")])
def update_graph(selected_metric):
    # Plotly express line chart
    return create_graph(selected_metric)


####################### PAGE LAYOUT #############################
layout = html.Div(
    className="mt-4 p-4",
    children=[
        html.H1("Faculty A"),  # heading separate line
        html.Hr(),
        html.Div(
            className="row mt-4",
            children=[
                html.Div(
                    className="col-4 mt-2 p-2 text-center",
                    children=[
                        html.Img(
                            src="../assets/image.png",
                            className="img-fluid ",
                            style={"border-radius": "50%"},
                        ),
                        html.Div(
                            className="mt-2",
                            children=[
                                html.H4(f"Joined in {faculty_data['joined']}"),
                                html.H4("Areas of Interest", className="m-0 p-0"),
                                html.P(
                                    "Database, Machine Learning", className="m-0 p-0"
                                ),
                                html.H4("Subjects", className="m-0 p-0"),
                                html.P("DBMS, OS", className="m-0 p-0"),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    [
                        # Dropdown for selecting metric
                        dcc.Dropdown(
                            id="metric-dropdown",
                            options=[{"label": html.Span(i, style={"padding-left": "4px", "backgroundColor": "#212529", "color": "white", "width" : "100%", "height": "100%"}), "value": i} for i in metrics],
                            value="Overall Acceptance",
                            style={"width": "100%", "backgroundColor": "#212529"},
                            className="bg-dark text-light border border-light"
                        ),
                        # Faculty info and graph container
                        html.Div(
                            className="mt-4",
                            children=[
                                html.Div(
                                    className="row",
                                    children=[
                                        # Graph column
                                        html.Div(
                                            className="col-md-12",
                                            children=[dcc.Graph(id="timeseries-graph")],
                                        )
                                    ],
                                )
                            ],
                        ),
                    ],
                    className="col-8",
                ),
            ],
        ),
    ],
)
