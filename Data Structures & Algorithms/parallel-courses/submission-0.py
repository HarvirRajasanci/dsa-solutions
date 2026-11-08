class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegrees = [0] * (n + 1)
        adj = defaultdict(list)
        for pre, crs in relations:
            adj[pre].append(crs)
            indegrees[crs] += 1

        q = deque([pre for pre in range(1, n + 1) if indegrees[pre] == 0])
        courses_taken = 0
        semesters = 0
        while q:
            size = len(q)
            for _ in range(size):
                pre = q.popleft()
                courses_taken += 1

                for crs in adj[pre]:
                    indegrees[crs] -= 1
                    if indegrees[crs] == 0:
                        q.append(crs)
            semesters += 1

        return semesters if courses_taken == n else -1
