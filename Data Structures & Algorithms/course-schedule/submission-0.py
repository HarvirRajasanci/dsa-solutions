class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        q = deque([pre for pre in range(numCourses) if indegree[pre] == 0])

        courses_taken = 0
        while q:
            pre = q.popleft()
            courses_taken += 1
            
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return courses_taken == numCourses
        
