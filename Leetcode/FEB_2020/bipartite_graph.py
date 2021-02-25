def is_bipartite(graph):
    if not graph: return False

    groups = [set([0]), set(graph[0])]
    visited = [False for _ in range(len(graph))]
    visited[0] = True

    def check_groups(graph_id, group_idx):
        visited[graph_id] = True

        other_group = 1 - group_idx
        groups[group_idx].add(graph_id)
        groups[other_group].add(graph[graph_id])

        for adj_node in graph[graph_id]:
            if visited[adj_node]:
                continue
            if adj_node in groups[group_idx]:
                return False
            else:
                if not check_groups(graph_id, other_group):
                    return False
        return True

    return check_groups(0, 0)
