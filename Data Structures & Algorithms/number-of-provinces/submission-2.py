class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(city):
            if city in visited:
                return
            visited.add(city)
            for i, connected in enumerate(isConnected[city]):
                if connected:
                    dfs(i)

        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1
        return provinces