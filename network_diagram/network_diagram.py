# Original data from http://www.sociopatterns.org/datasets/high-school-contact-and-friendship-networks/

import matplotlib.pyplot as plt
from networkx import nx

G = nx.read_edgelist('Facebook-known-pairs_data_2013_cleaned.csv', delimiter=',')
options = {'node_color': 'blue', 'node_size': 10, 'line_color': 'grey', 'linewidths': 0, 'width': 0.1}
plt.figure(figsize=(8.8, 3.5))
nx.draw_spring(G, **options)
plt.show()
