class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        x2, y2 = 0, 0

        for point in points:
            x1, y1 = point 
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            heapq.heappush(heap, (distance, point))

        res = []
        for i in range(min(k, len(heap))):
            res.append(heapq.heappop(heap)[1])
            
        return res