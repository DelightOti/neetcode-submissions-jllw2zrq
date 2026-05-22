class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {}

        if len(edges) != n-1:
            return False
        
        for i in range(n):
            graph[i] = []
            
        for a, b in edges:            
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):

            if node in visited:
                return
            
            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
        
        dfs(0)

        return True if len(visited) == n else False
