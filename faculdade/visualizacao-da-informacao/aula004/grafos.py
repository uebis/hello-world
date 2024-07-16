import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph() # cria grapho não-orientado
G.add_nodes_from([1,2,3,4]) # define nós
G.add_edges_from([(1,2), (1,3), (2,4), (3,4), (2,3)]) # define arestas
nx.draw_random(G) # posição aleatória
plt.show()