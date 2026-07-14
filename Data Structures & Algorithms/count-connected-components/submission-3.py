class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u):
            if visited[u]:
                return
            visited[u] = True
            for nei in adj[u]:
                dfs(nei)
                
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components

