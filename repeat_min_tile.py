import networkx as nx

def MinimumRepeatTile(G: nx.Graph, w: int, h: int) -> set:
    S = set()
    for v in G:
        x, y = v
        if x % 5 == 0:
            if y % 5 == 0 or y % 5 == 1:
                S |= {v}
        if x % 5 == 1:
            if y % 5 == 2 or y % 5 == 3:
                S |= {v}
        if x % 5 == 2:
            if y % 5 == 0 or y % 5 == 4:
                S |= {v}
        if x % 5 == 3:
            if y % 5 == 1 or y % 5 == 2:
                S |= {v}
        if x % 5 == 4:
            if y % 5 == 3 or y % 5 == 4:
                S |= {v}
        if x == 0 and y % 5 == 3:
            S |= {v}
        if x == w - 1 and y % 5 == 1:
            S |= {v}
        if x % 5 == 3 and y == 0:
            S |= {v}
        if x % 5 == 1 and y == h - 1:
            S |= {v}
    return S

m = 15
n = 10
G = nx.grid_2d_graph(m, n)
gammax2set = MinimumRepeatTile(G, m, n)

print(f"Minimum double dominating set: {gammax2set}")