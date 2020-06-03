N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        print("current_node는", current_node, "search_node는", search_node, "foot_print는", foot_prints)
        # print("row:",row[current_node][search_node],"sear : ",search_node, "foot:", foot_prints)
        if row[current_node][search_node] and search_node not in foot_prints:
            print("재진입, search_node는", search_node)
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        print("current_node는", current_node, "foot_print는", foot_prints)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


# print(*dfs(V, matrix, []))
print(*bfs(V))
