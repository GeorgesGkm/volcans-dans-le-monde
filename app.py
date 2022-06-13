import streamlit as st
import pandas as pd
from curses import use_default_colors
import matplotlib.pyplot as plt
import plotly.graph_objs as go

st.title("Data visualisation")

st.markdown(":tada: Data visualisation des volcans dans le monde")

df = pd.read_csv("data/volcans.csv")


if st.sidebar.checkbox("Visualiser les données du Fichier Csv"):
    st.write(df.style.background_gradient(cmap='BuGn'))

H = df.query('alt >= 0').copy()
M = H['alt'].max()
B = df.query('alt < 0').copy()
m = B['alt'].min()



fig = go.Figure()

fig.add_scattergeo(
    mode = 'markers',
    lon = H['long'],
    lat = H['lat'],
    showlegend = True,
    name = 'Classiques',
    hovertext = H['nom'] + '<b>' + H['alt'].astype(str)+'m',
    marker = {
        'color' : H['alt'],
        'colorscale': 'reds',
        'symbol':'triangle-up',
        'line': {'color':'black',
                'width':2},
        'size':1 + (30 * H['alt'] / M).astype(int) 
    }
)

fig.update_geos(
    showcoastlines = True,
    showcountries = True,
    countrycolor = 'white',
    landcolor = '#DDD',
    projection_type = 'miller'
)

fig.update_layout(
    
    height=600, margin={"r":0,"t":0,"l":0,"b":0},
    title = {'text': "<b> Volcans dans le monde </b>",
            'font': {'family':'comic sans MS', 'size':16, 'color':'black'},
             'y':0.89, 'x':0.5
            },
    legend = {'x':0.9, 'y':0.95,
             'bordercolor':'gray',
             'font':{'family':'comic sans MS', 'size':16},
             'borderwidth':2, 
             },
    showlegend = True
)
fig.add_scattergeo(
    mode = 'markers',
    lon = B['long'],
    lat = B['lat'],
    showlegend = True,
    name = 'Sous marins',
    hovertext = B['nom'] + '<b>' + B['alt'].astype(str)+'m',
    marker = {
        'color' : - B['alt'],
        'colorscale': 'blues',
        'symbol':'triangle-down',
        'line': {'color':'black',
                'width':2},
        'size':1 + (B['alt'] / m * 30).astype(int) 
    }
)

st.plotly_chart(fig)