Below are examples of **DFS**, **BFS**, **Dijkstra**, and **Prim's Algorithm** in Python, each with code optimized for interview preparation:

---

## **1. Depth-First Search (DFS)**

### **What is it?**

DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It is typically implemented using a stack (either explicitly or via recursion).

### **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

### **Space Complexity**: O(V), due to the recursion stack or the explicit stack.

### **Code Example**:

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')  # Process the node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS from node 'A'
dfs(graph, 'A')  # Output: A B D E F C
```

### **Key Idea**:

- Uses recursion or an explicit stack.
- Useful for problems that require exploring all possible paths (like connected components, cycle detection).

### **In practice**:

https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=problem-list-v2&envId=depth-first-search

```python
from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, graph, start, destination, visited=None):
        if visited is None:
            visited = set()

        if start == destination:
            return True

        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                if self.dfs(graph, neighbor, destination, visited):
                    return True

        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build graph from edges
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use DFS to check if there's a path from source to destination
        return self.dfs(graph, source, destination)

# Test
sol = Solution()
print(sol.validPath(5, [[0,1],[0,2],[0,3],[0,4],[4,2]], 0, 2))  # Expected output: True
```

---

## **2. Breadth-First Search (BFS)**

### **What is it?**

BFS is a graph traversal algorithm that explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level. It is implemented using a queue.

### **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

### **Space Complexity**: O(V), due to the queue storing nodes.

### **Code Example**:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # Process the node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS from node 'A'
bfs(graph, 'A')  # Output: A B C D E F
```

### **Key Idea**:

- Uses a queue to explore nodes level by level.
- Useful for finding the shortest path in an unweighted graph.

---

## **3. Dijkstra's Algorithm**

### **What is it?**

Dijkstra's Algorithm finds the shortest paths from a source vertex to all other vertices in a graph with non-negative edge weights. It uses a priority queue to explore the closest nodes first.

### **Time Complexity**: O((V + E) log V) with a priority queue (using a min-heap).

### **Space Complexity**: O(V), for storing distances and the priority queue.

### **Code Example**:

```python
import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if a longer path is found
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider shorter paths
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Run Dijkstra from node 'A'
distances = dijkstra(graph, 'A')
print(distances)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

### **Key Idea**:

- Uses a priority queue (min-heap) for optimal node selection.
- Suitable for finding the shortest path in graphs with non-negative weights.

---

## **4. Prim’s Algorithm**

### **What is it?**

Prim's Algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges. It expands the MST by adding the shortest edge connected to the already included nodes.

### **Time Complexity**: O((V + E) log V) with a priority queue (using a min-heap).

### **Space Complexity**: O(V + E), for storing the MST and the priority queue.

### **Code Example**:

```python
import heapq

def prim(graph, start):
    mst = []  # Store edges of the MST
    visited = set([start])

    # Priority queue to store (cost, from, to)
    edges = [(cost, start, to) for to, cost in graph[start]]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))

            # Add new edges connected to the MST
            for to_next, cost in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Run Prim's algorithm from node 'A'
mst = prim(graph, 'A')
print(mst)  # Output: [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]
```

### **Key Idea**:

- Uses a priority queue to select the smallest edge connecting a new node to the MST.
- Suitable for building the MST in weighted undirected graphs.

---

### **Summary**

| **Algorithm** | **Purpose**                       | **Data Structure**        | **Best for**                                | **Time Complexity** |
| ------------- | --------------------------------- | ------------------------- | ------------------------------------------- | ------------------- |
| DFS           | Graph traversal                   | Recursion/Stack           | Exploring all possible paths                | O(V + E)            |
| BFS           | Graph traversal (level order)     | Queue                     | Finding shortest paths in unweighted graphs | O(V + E)            |
| Dijkstra      | Shortest paths in weighted graphs | Min-Heap (Priority Queue) | Shortest path with non-negative weights     | O((V + E) log V)    |
| Prim's        | Minimum Spanning Tree             | Min-Heap (Priority Queue) | Constructing MST with weighted edges        | O((V + E) log V)    |

This should provide you with a solid understanding of these essential graph algorithms and prepare you well for interviews!
