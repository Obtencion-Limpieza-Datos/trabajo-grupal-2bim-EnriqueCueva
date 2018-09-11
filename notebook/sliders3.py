''' Present an interactive function explorer with slider widgets.

Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve sliders.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/sliders

in your browser.

'''
import numpy as np

from bokeh.core.properties import List, String, Dict, Int
from bokeh.models import LayoutDOM
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
import pandas as pd
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
# plot = figure(plot_height=400, plot_width=400, title="my sine wave",
#              tools="crosshair,pan,reset,save,wheel_zoom",
#              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

### plot 2
datos = pd.read_csv('info.csv',encoding='utf-8', sep=";")
#fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [10, 12, 4, 22, 24, 16]

source = ColumnDataSource(data=dict(fruits=datos.Ciudad, counts=datos.Poblacion))

plot = figure(x_range=datos.Ciudad, plot_height=700, toolbar_location=None, 
        tools="crosshair,pan,reset,save,wheel_zoom",
        title="Fruit Counts")
plot.vbar(x='fruits', top='counts', width=0.9, source=source, legend="fruits",
       line_color='white', fill_color=factor_cmap('fruits', palette=Spectral6, factors=datos.Ciudad))

plot.xgrid.grid_line_color = None
plot.y_range.start = 0
plot.y_range.end = 30
plot.legend.orientation = "horizontal"
plot.legend.location = "top_center"



# Set up widgets
text = TextInput(title="title", value=u'mi gráfica')
v1 = Slider(title="Loja", value=0.0, start=109000.0, end=400000.0, step=10000.0)
v2 = Slider(title="Quito", value=0.0, start= 200000.0, end=400000.0, step=10000.0)
v3 = Slider(title="Guayaquil", value=0.0, start=15000.0, end=400000.0, step=10000.0)
v4 = Slider(title="Cuenca", value=0.0, start=10000.0, end=400000.0, step=10000.0)


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    a = v1.value
    b = v2.value
    w = v3.value
    k = v4.value

    # Generate the new curve
    x = np.linspace(0, 4*np.pi, N)
    y = a*np.sin(k*x + w) + b
    
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    counts = [a, b, w, k, l, m]
    source.data = dict(fruits=datos.Ciudad, counts=datos.Poblacion)

for w in [v1, v2, v3, v4]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(text, v1, v2, v3, v4)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"
