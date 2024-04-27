import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path="/facultyfocus/A", name="Faculty A")


titanic_df = pd.read_csv("titanic.csv")





####################### PAGE LAYOUT #############################
layout = html.Div(
    
)
