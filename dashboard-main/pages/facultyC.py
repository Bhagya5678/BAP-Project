import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objs as go

dash.register_page(__name__, path="/facultyfocus/C", name="Faculty C")

# Sample data
categories = [
    "Subject Knowledge",
    "Regularity & Punctuality",
    "Communication Skills",
    "Syllabus Coverage",
    "Interest Generated in Subject",
    "Faculty Preparation",
]
data_set1 = [4.2, 3.6, 2.4, 4.7, 3.1, 2.9]
data_set2 = [3.8, 4.6, 2.7, 3.3, 4.9, 2.1]

colors = ["#0f392b", "#134632", "#185339", "#1c603f", "#206d46", "#247a4d", "#247a4d"]

# Create radar plot
fig3 = go.Figure()

fig3.add_trace(
    go.Scatterpolar(r=data_set1, theta=categories, fill="toself", name="BDA")
)

fig3.add_trace(go.Scatterpolar(r=data_set2, theta=categories, fill="toself", name="ML"))

fig3.update_layout(
    autosize=True,
    margin=dict(l=46, r=46, b=46, t=40),
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 5]),
        angularaxis=dict(
            tickfont=dict(color="white"),
            tickmode="array",
            tickvals=categories,
            ticktext=categories,
        ),
        bgcolor="#212529",
    ),
    showlegend=True,
    paper_bgcolor="#212529",  # Setting paper background color
    plot_bgcolor="#212529",
    legend=dict(
        orientation="h",  # Set legend orientation to horizontal
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
    ),
    font=dict(color="white", size=16),  # Change font color to white
)

faculty_data = {
    "Faculty": "A",
    "joined": 2016,
    "areas_of_interest": ["Database", "Machine Learning"],
    "subjects": ["DBMS", "OS"],
    "image": "image.png",
}

# Sfor time series graph
data = {
    "Subject Knowledge": [4.5, 4.2, 3.9, 4.4, 4.1, 4.6],
    "Regularity & Punctuality": [3.7, 3.9, 4, 3.8, 4.1, 3.6],
    "Communication Skills": [4.4, 4.6, 4.2, 4.3, 4.7, 4.5],
    "Syllabus Coverage": [4.3, 4.1, 4.5, 4.2, 4, 4.4],
    "Interest Generated in Subject": [4.1, 3.9, 4.4, 4.2, 4.5, 4.3],
    "Faculty Preparation": [4.2, 4.4, 4.1, 4.6, 4.3, 4.5],
    "Overall Acceptance": [4.4, 4.1, 4.7, 4.2, 3.9, 4.5],
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

# for 6 bar plots
metricwise_avg = [
    {"Subject Knowledge": [10, 18, 27, 31, 14]},
    {"Regularity & Punctuality": [10, 20, 30, 25, 15]},
    {"Communication Skills": [20, 25, 30, 20, 5]},
    {"Syllabus Coverage": [8, 16, 28, 30, 18]},
    {"Interest Generated in Subject": [6, 12, 26, 30, 26]},
    {"Faculty Preparation": [12, 18, 27, 28, 15]},
    {"Overall Acceptance": [10, 18, 27, 31, 14]},
]


def create_graph(selected_metric="Overall Acceptance"):
    # Create a line chart
    fig = px.line(
        x=years,
        y=data[selected_metric],
        labels={"x": "Year", "y": selected_metric},
        markers=True,
    )
    fig.update_traces(line_color=colors[6], marker_color=colors[4])
    fig.update_layout(
        paper_bgcolor="#212529",
        plot_bgcolor="#212529",
        xaxis=dict(tickfont=dict(color="white"), showgrid=False),
        yaxis=dict(tickfont=dict(color="white"), showgrid=False, range=[0, 5]),
    )
    return fig


@callback(Output("timeseries-graph-C", "figure"), [Input("metric-dropdown", "value")])
def update_graph(selected_metric):
    # Plotly express line chart
    return create_graph(selected_metric)


####################### PAGE LAYOUT #############################
layout = html.Div(
    className="mt-4 p-4",
    children=[
        html.H1("Faculty C"),  # heading separate line
        html.Hr(),
        html.Div(
            className="row mt-4",
            children=[
                html.Div(
                    className="col-3 mt-2 p-2 text-center",
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
                    className="col-4",
                    children=[
                        dcc.Graph(
                            id="my-graph",
                            figure={
                                "data": [
                                    {
                                        "x": metrics,
                                        "y": [4.6, 4.3, 4.4, 4.2, 4.7, 4.5, 4],
                                        "type": "bar",
                                        "marker": {"color": colors},
                                    }
                                ],
                                "layout": {
                                    "title": {
                                        "text": "Average Scores for Each Metric",
                                        "font": {"color": "white"},
                                    },
                                    "plot_bgcolor": "#212529",
                                    "paper_bgcolor": "#212529",
                                    "xaxis": {"showticklabels": True, "tickfont": {"color": "white"}},
                                    "yaxis": {"tickfont": {"color": "white"}},
                                },
                            },
                        )
                    ],
                ),
                html.Div(
                    [  # time series graph
                        # Dropdown for selecting metric
                        dcc.Dropdown(
                            id="metric-dropdown",
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
                                for i in metrics
                            ],
                            value="Overall Acceptance",
                            style={"width": "100%", "backgroundColor": "#212529"},
                            className="bg-dark text-light border border-light",
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
                                            children=[
                                                dcc.Graph(id="timeseries-graph-C")
                                            ],
                                        )
                                    ],
                                )
                            ],
                        ),
                    ],
                    className="col-5",
                ),
            ],
        ),  # div 1 ends
        html.H1("Metric-wise Response Frequency"),
        html.Br(),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-3 m-0",
                    children=[
                        dcc.Graph(
                            figure={
                                "data": [
                                    {
                                        "x": [1, 2, 3, 4, 5],
                                        "y": list(metric_data.values())[0],
                                        "type": "bar",
                                        "marker": {"color": colors[index]},
                                    }
                                ],
                                "layout": {
                                    "autosize": True,
                                    "margin": {"l": 46, "r": 46, "b": 46, "t": 40},
                                    "title": {
                                        "text": f"{list(metric_data.keys())[0]}",
                                        "font": {"color": "white"},
                                    },
                                    "plot_bgcolor": "#212529",
                                    "paper_bgcolor": "#212529",
                                    "yaxis": {
                                        "tickfont": {"color": "white"},
                                        "showticklabels": True,
                                    },
                                    "xaxis": {
                                        "tickfont": {"color": "white"},
                                        "showticklabels": True,
                                        "tickvals": [1, 2, 3, 4, 5],
                                    },
                                },
                            },
                        )
                    ],
                    style={"marginLeft": "2rem"},
                )
                for index, metric_data in enumerate(metricwise_avg)
            ],
        ),  # div 2 ends
        html.H1("Subject-wise Comparison", className="text-center mt-4"),
        html.Div(html.Div([dcc.Graph(figure=fig3)])),
        html.H1("Textual Feedback Overview", className="text-center mt-4"),
        html.Img(
            src="../assets/C.png",
            className="",
            style={"width": "35%", "margin-left": "5%"},
        ),
        html.Img(
            src="../assets/C2.png",
            className="",
            style={"margin": "5%", "width": "50%"},
        ),
    ],
)
