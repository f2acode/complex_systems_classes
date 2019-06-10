# pi1
import networkx as nx
import matplotlib.pyplot as plt
import math

r = 1
N = 60480
G = nx.Graph()
pos_dict = {}
r_custom = range(-N, N)

for i in r_custom:
    x = i/N
    y = math.sqrt(r ** 2 - x ** 2)
    
    G.add_node(x)
    G.add_node(x + 60480)
    
    pos_dict[x] = [x, y]
    pos_dict[x + 60480] = [x, -y]
    
nx.draw(G, node_size=50, alpha=1.0, node_color='black', with_labels=False, pos=pos_dict)

for i in r_custom[N-int(N*0.9):int((N * 2)*0.95)]:
    G.add_node(x)
    
    x = (i/N)
    y = math.sqrt(r ** 2 - x ** 2)-0.3

    pos_dict[x] = [x, -y]
        
nx.draw(G, node_size=50, alpha=1.0, node_color='black', pos=pos_dict)

x = 0.5
y = math.sqrt(r ** 2 - x ** 2)-1.2
G.add_node(x)
pos_dict[x] = [x, -y]

x = -0.5
y = math.sqrt(r ** 2 - x ** 2)-1.2
G.add_node(x)
pos_dict[x] = [x, -y]

nx.draw(G, node_size=50, alpha=1.0, node_color='black', pos=pos_dict)

plt.show()
