from collections import deque

def breadth_first_traversal(graph, start):
    visited = {}

    for k in graph:
        visited[k] = False

    node_queue = deque(start)
    print(start)
    visited[start] = True

    while len(node_queue) != 0:
        current_node = node_queue.popleft()
        neighbors = graph[current_node]

        for n in neighbors:
            if not visited[n]:
                print n
                visited[n] = True
                node_queue.append(n)


graph = {
    "A": ["C", "D", "E"],
    "B": ["A", "C", "E"],
    "C": ["A", "B"],
    "D": ["A", "E"],
    "E": ["A", "B"]
}

breadth_first_traversal(graph, "A")