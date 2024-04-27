import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np

dash.register_page(__name__, path="/", name="Department Overview")

import pandas as pd

data = pd.read_csv("feedback.csv")
faculty_data = [
    {
        "Faculty": "A",
        "joined": 2016,
        "subjects": ["DBMS", "OS"],
    },
    {
        "Faculty": "B",
        "joined": 2017,
        "subjects": ["OS", "BDA"],
    },
    {
        "Faculty": "C",
        "joined": 2018,
        "subjects": ["BDA", "ML"],
    },
    {
        "Faculty": "D",
        "joined": 2019,
        "subjects": ["ML", "DC"],
    },
    {
        "Faculty": "E",
        "joined": 2020,
        "subjects": ["DC", "BCT"],
    },
    {
        "Faculty": "F",
        "joined": 2016,
        "subjects": ["NLP"],
    },
    {
        "Faculty": "G",
        "joined": 2017,
        "subjects": ["CC", "DAA"],
    },
    {
        "Faculty": "H",
        "joined": 2018,
        "subjects": ["DAA"],
    },
]

total_responses = len(data)
unique_faculty = data["Faculty"].unique()
unique_subjects = [
    "Blockchain Technology (BCT)",
    "Big Data Analytics (BDA)",
    "Cloud Computing (CC)",
    "Design and Analysis of Algorithms (DAA)",
    "Database Management (DBMS)",
    "Distributed Computing (DC)",
    "Machine Learning (ML)",
    "Natural Language Processing (NLP)",
    "Operating Systems (OS)",
]

# Group faculties by subjects
grouped_data = data.groupby("Subject")["Faculty"].apply(set).reset_index()
labels = [
    "CE Dept",
    "BCT",
    "BDA",
    "CC",
    "DAA",
    "DBMS",
    "DC",
    "ML",
    "NLP",
    "OS",
    "E1",
    "B1",
    "C1",
    "G2",
    "F1",
    "G1",
    "H",
    "A1",
    "E2",
    "D1",
    "C2",
    "D2",
    "F2",
    "B2",
    "A2",
]
parents = [
    "",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "CE Dept",
    "BCT",
    "BDA",
    "BDA",
    "CC",
    "CC",
    "DAA",
    "DAA",
    "DBMS",
    "DC",
    "DC",
    "ML",
    "ML",
    "NLP",
    "OS",
    "OS",
]
values = [
    100,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    12,
    11,
    5,
    6,
    5,
    6,
    5,
    6,
    11,
    5,
    6,
    5,
    6,
    11,
    6,
    6,
]
custom_colors = [
    "#e9ecef",  # whitish
    "#a1ff0a",  # green
    "#fee440",  # yellow
    "#ff9e00",  # orange
    "#f35b04",  # orange
    "#fc2f00",  # red
    "#b5179e",  # purple
    "#023e8a",  # blue
    "#40916c",  # dark green
    "#07c8f9",  # blue light
]


###Second layer of viz

corr_mat = [
    [
        1.0,
        0.877978187949003,
        0.881196646363806,
        0.8472059661562948,
        0.8418418086741752,
        0.8708624431786756,
        0.8936242202822464,
    ],
    [
        0.877978187949003,
        1.0,
        0.8819982206747585,
        0.8724074201689868,
        0.8176895467707801,
        0.8669906326393431,
        0.8780548035415802,
    ],
    [
        0.881196646363806,
        0.8819982206747585,
        1.0,
        0.8947142955721078,
        0.8794495870687387,
        0.8761875729304943,
        0.9227061146113161,
    ],
    [
        0.8472059661562948,
        0.8724074201689868,
        0.8947142955721078,
        1.0,
        0.8819158924735765,
        0.8719000890146078,
        0.8957710185913008,
    ],
    [
        0.8418418086741752,
        0.8176895467707801,
        0.8794495870687387,
        0.8819158924735765,
        1.0,
        0.8678672578680392,
        0.9032161416402958,
    ],
    [
        0.8708624431786756,
        0.8669906326393431,
        0.8761875729304943,
        0.8719000890146078,
        0.8678672578680392,
        1.0,
        0.9223587676793369,
    ],
    [
        0.8936242202822464,
        0.8780548035415802,
        0.9227061146113161,
        0.8957710185913008,
        0.9032161416402958,
        0.9223587676793369,
        1.0,
    ],
]

metrics = [
    "Subject Knowledge",
    "Regularity & Punctuality",
    "Communication Skills",
    "Syllabus Coverage",
    "Interest Generated in Subject",
    "Faculty Preparation",
    "Overall Acceptance",
]

# average metric per faculty

avgmetrics = [
    [
        "A",
        [
            4.07,
            4.31,
            4.03,
            4.15,
            3.99,
            4.15,
            4.09,
        ],
    ],
    [
        "B",
        [
            3.81,
            3.93,
            3.80,
            3.90,
            3.74,
            3.84,
            3.74,
        ],
    ],
    [
        "C",
        [
            4.15,
            4.11,
            3.84,
            3.85,
            3.72,
            4.23,
            3.92,
        ],
    ],
    [
        "D",
        [
            4.12,
            4.04,
            3.94,
            4.01,
            3.86,
            3.99,
            4.00,
        ],
    ],
    [
        "E",
        [
            4.63,
            4.64,
            4.55,
            4.61,
            4.53,
            4.66,
            4.62,
        ],
    ],
    [
        "F",
        [
            3.84,
            3.84,
            3.75,
            3.76,
            3.63,
            3.85,
            3.69,
        ],
    ],
    [
        "G",
        [
            4.82,
            4.73,
            4.78,
            4.78,
            4.78,
            4.76,
            4.76,
        ],
    ],
    [
        "H",
        [
            4.69,
            4.57,
            4.66,
            4.57,
            4.625,
            4.63,
            4.60,
        ],
    ],
]

alpha_faculty = ["A", "B", "C", "D", "E", "F", "G", "H"]

fig = go.Figure(
    go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
        branchvalues="total",
        marker=dict(
            colors=custom_colors,
        ),
    )
)

fig.update_layout(
    paper_bgcolor="#212529",
    # paper_bgcolor="white",
    autosize=True,
    margin=dict(l=0, r=0, b=0, t=0, pad=0),
)

# Coorelation heatmap

fig2 = go.Figure(
    data=go.Heatmap(
        x=metrics,
        y=metrics,
        z=corr_mat,
        colorscale="tempo",
        # coloraxis="coloraxis",
        colorbar=dict(tickfont=dict(color="white")),
    )
)

fig2.update_layout(
    height=650,
    width=850,
    paper_bgcolor="#212529",
    xaxis=dict(
        tickfont=dict(color="white", size=16), title_font=dict(color="white", size=20)
    ),
    yaxis=dict(
        tickfont=dict(color="white", size=16), title_font=dict(color="white", size=20)
    ),
    autosize=True,
    margin=dict(l=0, r=0, b=0, t=0, pad=0),
    coloraxis=dict(colorbar=dict(tickfont=dict(color="white"))),
)
# Add the coloraxis to the figure
fig2.update_layout(
    coloraxis=dict(
        colorbar=dict(
            title="Value", title_font=dict(color="white"), tickfont=dict(color="white")
        )
    ),
    # title="Correlation Heatmap",
    # title_font=dict(color="white", size=30),
)


# figure 3, stacked bar graph


bars = []
for i in range(7):
    temp = []
    for j in range(6):
        temp.append(avgmetrics[j][1][i])
    bar = go.Bar(
        name=metrics[i],
        x=alpha_faculty,
        y=temp,
    )
    bars.append(bar)


fig3 = go.Figure(data=bars)
fig3.update_layout(
    barmode="stack",
    width=1250,
    height=750,
    paper_bgcolor="#212529",
    plot_bgcolor="#212529",
    autosize=True,
    legend=dict(
        font=dict(
            size=20,
            color="white",
        ),
        yanchor="middle",
        y=0.5,
        xanchor="right",
        x=1.8,
    ),
    title="Faculty-wise average metrics",
    title_font=dict(color="white", size=30),
    xaxis=dict(
        tickfont=dict(color="white", size=16), title_font=dict(color="white", size=20)
    ),
    yaxis=dict(
        tickfont=dict(color="white", size=16), title_font=dict(color="white", size=20)
    ),
)
####################### PAGE LAYOUT #############################
layout = html.Div(
    className="container w-100 h-100 m-0 p-0 d-flex flex-column",
    children=[
        html.Div(
            className="container-fluid row my-4 mx-auto",
            children=[
                # Faculties Section
                html.Div(
                    className="col-md-4 pl-4 ml-4",  # Faculties on the left
                    children=[
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="col-md-12 text-center",
                                    children=[
                                        html.H4("Faculty", className="fs-2"),
                                        html.Div(
                                            className="row row-cols-3",  # Changed to 4 columns
                                            children=[
                                                html.Div(
                                                    className="col",
                                                    children=html.Div(
                                                        className="card bg-dark text-light border border-light my-2 mx-1",
                                                        style={
                                                            "height": "150px",
                                                            "width": "130px",
                                                        },  # Set a fixed height
                                                        children=[
                                                            html.Div(
                                                                className="card-body",
                                                                children=[
                                                                    html.H5(
                                                                        f"Faculty {faculty['Faculty']}",
                                                                        className="card-title mb-3",
                                                                        style={
                                                                            "text-decoration": "underline"
                                                                        },  # Underline the heading
                                                                    ),
                                                                    html.Div(
                                                                        children=[
                                                                            html.P(
                                                                                "Subjects",
                                                                                className="m-0 p-0 fw-bold",
                                                                            ),
                                                                            html.Div(
                                                                                children=[
                                                                                    (
                                                                                        html.P(
                                                                                            subject, className="m-0"
                                                                                        )
                                                                                    )
                                                                                    for subject in faculty[
                                                                                        "subjects"
                                                                                    ]
                                                                                ],
                                                                                className="m-0 p-0"
                                                                            ),
                                                                        ],
                                                                        className="card-text",
                                                                    ),
                                                                ],
                                                            )
                                                        ],
                                                    ),
                                                )
                                                for faculty in faculty_data
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                # Subjects Section
                html.Div(
                    className="col-md-3 text-center ml-4",  # Centering subjects in the middle
                    children=[
                        html.H4(
                            "Subjects", className="fs-2 mb-4"
                        ),  # Set heading size to fs-2
                        html.Div(
                            [
                                html.Div(
                                    subject,
                                    className="btn",
                                    style={
                                        "margin-bottom": "10px",
                                        "background-color": custom_colors[i + 1],
                                        "font-weight": "bold",
                                        "width": "40%",
                                        "margin-left": "5%",
                                        "margin-right": "5%",
                                    },
                                )
                                for i, subject in enumerate(unique_subjects)
                            ],
                            # style={
                            #     "margin-right": "10px"
                            # },  # Adding margin between subjects
                        ),
                    ],
                ),
                # Sunburst Chart Section
                html.Div(
                    className="col-md-5 mt-5",  # Sunburst chart on the right
                    children=[
                        html.Div([dcc.Graph(figure=fig)]),
                    ],
                ),
            ],
        ),  # first row of stuff
        html.Div(
            className="row d-flex mt-5 p-2",
            children=[
                html.Div([dcc.Graph(figure=fig2)], className="col-9"),
                html.Div(
                    style={"color": "#439E81", "padding": "0"},
                    children=[
                        html.H1("Correlation Heatmap", style={"color": "white"}),
                        html.H3("Evaluation Metrics", className="pl-4"),
                        html.Ul(
                            [
                                html.Li(
                                    metric,
                                    style={"fontSize": "25px"},
                                    className="my-2 font-weight-bold",
                                )
                                for metric in metrics
                            ],
                        ),
                    ],
                    className="col-3",
                ),
            ],
        ),  # second row of stuff
        html.Div([dcc.Graph(figure=fig3)], className="mt-5 ml-5 pl-5"),
    ],
)
