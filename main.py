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