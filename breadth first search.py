from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize queue with starting node
    visited.add(start)  # Mark the starting node as visited

    while queue:
        node = queue.popleft()  # Get the next node from the queue
        print(node)  # Process the current node

        # Explore all neighboring nodes of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Add the neighbor to the queue for further exploration

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for BFS traversal
start_node = 'A'
print("BFS traversal starting from node", start_node)
bfs(graph, start_node)