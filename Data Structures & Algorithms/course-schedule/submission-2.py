class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0
        while q:
            pre = q.popleft()
            for crs in adj[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs) 
            completed += 1

        return numCourses == completed
