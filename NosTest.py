import networkx as nx
import random
G = nx.fast_gnp_random_graph(100,0.1)
L = list(G.edges())
edges_to_delete = random.sample(L, 5)
G.remove_edges_from(edges_to_delete)

#it's probably better to create a copy of `G` rather than act on `G` directly.
node_list = list(G.nodes())
for counter in range(5):
    candidate_edge = tuple(random.sample(node_list,2))
    if not G.has_edge(*candidate_edge):
        G.add_edge(*candidate_edge)

nx.draw(G)