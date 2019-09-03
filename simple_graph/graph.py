from bokeh.plotting import figure, show
import math
x_values = range(0, 720)
y_values = [math.sin(math.radians(x)) for x in x_values]
p = figure(title='Sine wave', x_axis_label='x (degrees)', y_axis_label='y = sin(x)')
p.line(x_values, y_values)
show(p)
