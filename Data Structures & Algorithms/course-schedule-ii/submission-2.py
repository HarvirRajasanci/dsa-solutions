class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque([pre for pre in range(numCourses) if indegree[pre] == 0])
        courses = []
        courses_taken = 0
        while q:
            pre = q.popleft()
            courses_taken += 1
            courses.append(pre)

            for crs in adj[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)

        return courses if courses_taken == numCourses else []
