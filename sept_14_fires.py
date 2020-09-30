from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

in_file = open('US_fires_9_14.json', 'r')

fires_data = json.load(in_file)


brightness, longs, lats = [], [], []


for dic in fires_data:
    long = dic['longitude']
    lat = dic['latitude']
    # brights = (dic['brightness'])
    if dic['brightness'] > 450:
        brights = dic['brightness']
        brightness.append(brights)
    longs.append(long)
    lats.append(lat)


data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'marker': {
        'size': [.06*brights for brights in brightness],
        'color': brightness,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {
            'title': 'Brightness'
        }
    }
}]

my_layout = Layout(title='US Fires - 9/14/2020 through 9/20/2020')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='cali_fires.html')
