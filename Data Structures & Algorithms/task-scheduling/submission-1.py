class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)

        cycles = 0
        q = deque()
        while heap or q:
            cycles += 1

            if not heap:
                cycles = q[0][1]
            else:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count, cycles + n])

            if q and q[0][1] == cycles:
                heapq.heappush(heap, q.popleft()[0])

        return cycles