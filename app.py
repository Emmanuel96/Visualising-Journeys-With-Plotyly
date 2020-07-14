import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

cols = ['State', 'lat', 'lon']
location_df = pd.DataFrame(columns=cols)

# I will manually include the needed locations and their lat and logintudes
location_df = location_df.append([
    {'State': 'London', 'method': 'car', 'lat': 51.5074, 'lon': 0.1278},
    {'State': 'Dover', 'method': 'ferry', 'lat': 51.126369, 'lon': 1.316198},
    {'State': 'Calais', 'method': 'car', 'lat': 50.954468, 'lon': 1.862801},
    {'State': 'Paris', 'method': 'airport', 'lat': 49.009724, 'lon': 2.547778},
    {'State': 'Instabul', 'method': 'airport', 'lat': 41.015137, 'lon': 28.979530}
], ignore_index=True)

token = open("./mapbox.token").read()

fig = go.Figure(go.Scattermapbox(mode="markers+text+lines",
                                 lon=location_df.lon, lat=location_df.lat,
                                 marker={'size': 15,
                                         'symbol': location_df.method},
                                 text=location_df.State,
                                 textposition="bottom right"))

fig.update_layout(mapbox={'accesstoken': token,
                          'center': {'lat': 51.5074, 'lon': 0.1278},
                          'style': "outdoors", 'zoom': 1})

fig.write_html('./marker.html', auto_open=True)
