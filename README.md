## Visualising Journeys With Plotyly Object

### Description

Using the Plotly graph library to visualize a journey using symbols to represent the means of transport.

### Case Study

A person drove from London to Dover, took a ferry from Dover to Calais, and drove from Calais to Charles de Gaulle Airport in Paris. The person then took a flight to Istanbul Airport.

### Requirements

- Python 3.7 or any higher version
- VS Code or any other IDE of choice
- All the necessary classes installed with Conda or pip
- Mapbox Account and token

### Create Mapbox Account

To make use of mapbox, you will need to go to the url: https:mapbox.com

- Create an account
- Verify your email
- Create and save a token.

We need these steps to be completed before the implementation.

### Implementation

We start with the imports. Please make sure you install these classes with pip or conda first.

    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go

From the case study we can hardcode a dataframe with the columns: lat, long, state and method of travel i.e.

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

Next, we read our token i.e.
token = open("./mapbox.token").read()

Please note that I already have my token saved here. You could simply copy and paste your token i.e.

    token = "your-copy-and-pasted-token"

Now, we draw our maps using the Plotly figure class i.e.

    fig = go.Figure(go.Scattermapbox(mode="markers+text+lines",
                                    lon=location_df.lon, lat=location_df.lat,
                                    marker={'size': 15,
                                            'symbol': location_df.method},
                                    text=location_df.State,
                                    textposition="bottom right"))

We then change the center to make the map look better

    fig.update_layout(mapbox={'accesstoken': token,
                            'center': {'lat': 51.5074, 'lon': 0.1278},
                            'style': "outdoors", 'zoom': 1})

Finally, we display our map

    fig.write_html('./map.html', auto_open=True)

![map showing journey](https://github.com/Emmanuel96/Visualising-Journeys-With-Plotyly/blob/master/images/img.jpg?raw=true)
