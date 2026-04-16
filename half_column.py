import networkx as nx

def HalfColumn(G: nx.Graph, w: int) -> set:
    S = set()
    for vertex in G:
        x, y = vertex
        if x % 2 == 0:
            S |= {vertex}
        elif w % 2 == 0 and x == w - 1 and y % 2 == 1:
            S |= {vertex}
    return S

m = 6
n = 6
G = nx.grid_2d_graph(m, n)
gammax2set = HalfColumn(G, m)

print("Minimum double dominating set: ", gammax2set)