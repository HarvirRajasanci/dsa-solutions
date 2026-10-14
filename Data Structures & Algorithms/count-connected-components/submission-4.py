class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        return components