"""
[문제]
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.
--
[입력]
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.
--
[출력]
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.
"""
from collections import defaultdict, deque

node, edge, start = map(int, input().split())
graphs = defaultdict(set)
for _ in range(edge):
    n1, n2 = map(int, input().split())
    graphs[n1].add(n2)
    graphs[n2].add(n1)

def dfs(graphs, start_node, visited, dfs_result):
    visited.add(start_node)
    dfs_result.append(start_node)
    for neighbor in sorted(graphs[start_node]):
        if neighbor not in visited:
            dfs(graphs, neighbor, visited, dfs_result)

    return dfs_result

def bfs(graphs, start_node, visited, bfs_result):
    queue = deque([start_node])
    while queue:
        start_node = queue.popleft()
        if start_node not in visited:
            visited.add(start_node)
            bfs_result.append(start_node)
            queue.extend(sorted(list(graphs[start_node] - visited)))

    return bfs_result

dfs_visited, bfs_visited = set(), set()
dfs_result = dfs(graphs, start, dfs_visited, [])
bfs_result = bfs(graphs, start, bfs_visited, [])
print(*dfs_result)
print(*bfs_result)
