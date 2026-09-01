class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(city):
            if city in visited:
                return
            visited.add(city)
            for curr_city, is_connected in enumerate(isConnected[city]):
                if is_connected:
                    dfs(curr_city)

        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces