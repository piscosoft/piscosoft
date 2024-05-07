def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes

    visited.add(start)  # Mark the current node as visited

    if start == goal:
        print("Goal reached:", goal)
        return True  # Goal found, return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True  # If goal found in neighbor, return True

    return False  # Goal not found in current branch

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for DFS traversal
start_node = 'A'
goal_node = 'F'
print("DFS search from", start_node, "to", goal_node)
if not dfs(graph, start_node, goal_node):
    print("Goal", goal_node, "not reachable from node", start_node)