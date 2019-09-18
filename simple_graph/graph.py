from bokeh.plotting import figure, show
import math
x_values = range(0, 720)
y_values = [math.sin(math.radians(x)) for x in x_values]
p = figure(title='10 Sine waves', x_axis_label='x (degrees)', y_axis_label='y = sin(x)', plot_width=850, plot_height=350)
for i in range(10):
    factor = 1 - i/10
    p.line(x_values, [y * factor for y in y_values])
show(p)
