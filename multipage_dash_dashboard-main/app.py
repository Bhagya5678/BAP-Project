from dash import Dash, html, dcc
import dash
import plotly.express as px

px.defaults.template = "ggplot2"

external_css = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
]

app = Dash(
    __name__, pages_folder="pages", use_pages=True, external_stylesheets=external_css
)

app.layout = html.Div(
    [
        html.Br(),
        html.P(
            "Faculty Feedback | Semester 4 | 2023-24",
            className="text-light text-center fw-bold fs-1 m-0 p-0",
        ),
        html.Div(
            children=[
                dcc.Link(
                    page["name"],
                    href=page["relative_path"],
                    className="btn btn-dark border border-light m-2 fs-5",
                )
                for page in dash.page_registry.values()
            ], className="container-fluid",
        ),
        dash.page_container,
    ],
    className="container-fluid bg-dark text-light w-100 h-100 p-0",
)

if __name__ == "__main__":
    app.run(debug=True)
