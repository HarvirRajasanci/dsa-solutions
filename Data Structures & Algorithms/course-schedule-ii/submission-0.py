class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for src, dst in prerequisites:
            adj[dst].append(src)
            indegree[src] += 1

        q = deque([pre for pre in range(numCourses) if indegree[pre] == 0])

        courses = []
        courses_taken = 0
        while q:
            pre = q.popleft()
            courses.append(pre)
            courses_taken += 1
            
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return courses if courses_taken == numCourses else []
        
