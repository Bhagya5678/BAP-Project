import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/facultyfocus", name="Faculty Focus")


faculty_data = [
    {
        "Faculty": "A",
        "joined": 2016,
        "areas_of_interest": ["Database", "Machine Learning"],
        "subjects": ["DBMS", "OS"],
        "image": "image.png",
    },
    {
        "Faculty": "B",
        "joined": 2017,
        "areas_of_interest": ["Artificial Intelligence", "Data Science"],
        "subjects": ["OS", "BDA"],
        "image": "image.png",
    },
    {
        "Faculty": "C",
        "joined": 2018,
        "areas_of_interest": ["Computer Networks", "Cybersecurity"],
        "subjects": ["BDA", "ML"],
        "image": "image.png",
    },
    {
        "Faculty": "D",
        "joined": 2019,
        "areas_of_interest": ["Software Engineering", "Web Development"],
        "subjects": ["ML", "DC"],
        "image": "image.png",
    },
    {
        "Faculty": "E",
        "joined": 2020,
        "areas_of_interest": ["Computer Graphics", "Machine Learning"],
        "subjects": ["DC", "BCT"],
        "image": "image.png",
    },
    {
        "Faculty": "F",
        "joined": 2016,
        "areas_of_interest": ["Natural Language Processing", "Big Data"],
        "subjects": ["NLP"],
        "image": "image.png",
    },
    {
        "Faculty": "G",
        "joined": 2017,
        "areas_of_interest": ["Cloud Computing", "Parallel Computing"],
        "subjects": ["CC", "DAA"],
        "image": "image.png",
    },
    {
        "Faculty": "H",
        "joined": 2018,
        "areas_of_interest": ["Operating Systems", "Computer Architecture"],
        "subjects": ["DAA"],
        "image": "image.png",
    },
]

unique_faculty = ["A", "B", "C", "D", "E", "F", "G", "H"]
####################### PAGE LAYOUT #############################
layout = html.Div(
    className="container-fluid mt-5",
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-md-2 col-sm-6 mb-4 mx-4",
                    children=[
                        dcc.Link(
                            html.Div(
                                className="card bg-dark border shadow p-2",
                                style={
                                    "width": "15rem",
                                    "height": "22rem",
                                    "color": "#ffffff",
                                    "border-color": "#ffffff",
                                },
                                children=[
                                    html.Div(
                                        className="card-body d-flex align-items-center justify-content-center",
                                        children=[
                                            html.Img(
                                                src="../assets/image.png",
                                                alt="Faculty Image",
                                                style={
                                                    "borderRadius": "50%",
                                                    "width": "10rem",
                                                },
                                                className="m-0 p-0",
                                            ),
                                        ],
                                    ),
                                    html.H5(
                                        f"Faculty {faculty['Faculty']}",
                                        className="card-title m-0 p-0",
                                    ),
                                    html.P(
                                        f"Joined in {faculty['joined']}",
                                        className="card-text m-0 p-0",
                                    ),
                                    html.P(
                                        f"Subjects: {', '.join(faculty['subjects'])}",
                                        className="card-text m-0 p-0",
                                    ),
                                    html.P(
                                        f"Areas of Interest: {', '.join(faculty['areas_of_interest'])}",
                                        className="card-text m-0 p-0",
                                    ),
                                ],
                            ),
                            href=f"/facultyfocus/{faculty['Faculty']}",
                            className="text-decoration-none text-center",
                        )
                    ],
                )
                for faculty in (faculty_data)
            ],
        )
    ],
)
