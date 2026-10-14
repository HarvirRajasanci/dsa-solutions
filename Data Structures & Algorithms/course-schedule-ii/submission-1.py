class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        courses = []
        completed = 0
        while q:
            course = q.popleft()
            for dst in adj[course]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)
            courses.append(course)
            completed += 1

        return courses if completed == numCourses else []