class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        q = deque()

        cycles = 0
        while heap or q:
            cycles += 1
            
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count:
                    q.append((cycles + n, count))

            if q and q[0][0] == cycles:
                count = q.popleft()[1]
                heapq.heappush(heap, count)
        return cycles
