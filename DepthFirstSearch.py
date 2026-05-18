matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
    ]

def dfs(adj_matrix, start_node):
    stack = [start_node]
    visited = [start_node]
    while stack:
        node = stack.pop()
        for i in range(len(adj_matrix)-1,-1,-1):
            if adj_matrix[node][i] == 1 and i not in visited:
                stack.append(i)
                visited.append(i)
    return visited


print(dfs(matrix, 1))