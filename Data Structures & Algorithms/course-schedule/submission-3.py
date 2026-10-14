class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for dst, crs in prerequisites:
            adj[crs].append(dst)
            indegree[dst] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        completed = 0
        while q:
            crs = q.popleft()
            for dst in adj[crs]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)
            completed += 1

        return completed == numCourses
