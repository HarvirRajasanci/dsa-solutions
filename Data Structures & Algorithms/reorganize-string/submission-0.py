class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, num) for num, count in Counter(s).items()]
        heapq.heapify(heap)

        reorganized_string = []
        last_num = None
        while heap:
            count, num = heapq.heappop(heap)
            reorganized_string.append(num)

            if last_num and last_num[0] < 0:
                heapq.heappush(heap, last_num)
            last_num = (count + 1, num)

        if last_num[0] != 0:
            return ""
        return "".join(reorganized_string)



