import networkx as nx

def RecursiveDomination(G: nx.Graph, ddset: set, current_vertex_index: int) -> set:
    if current_vertex_index >= len(G.nodes()):
        return ddset

    vertex = list(G)[current_vertex_index]

    tempset = ddset.difference({vertex})

    is_valid_ddset = True

    for node in set(G.neighbors(vertex)) | {vertex}:
        neighbors = set(G.neighbors(node)) | {node}
        dominated_by = neighbors.intersection(tempset)
        if len(dominated_by) < 2:
            is_valid_ddset = False
            break
    
    current_vertex_index += 1
    solution1 = RecursiveDomination(G, tempset, current_vertex_index) if is_valid_ddset else ddset
    solution2 = RecursiveDomination(G, ddset, current_vertex_index)

    if len(solution1) <= len(solution2):
        return solution1
    else:
        return solution2

m = 6
n = 6
G = nx.grid_2d_graph(m, n)
gammax2set = RecursiveDomination(G, set(G.nodes()), 0)

print("Minimum double dominating set: ", gammax2set)