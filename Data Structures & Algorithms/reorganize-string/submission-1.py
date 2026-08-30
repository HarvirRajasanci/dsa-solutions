class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, num) for num, count in Counter(s).items()]
        heapq.heapify(heap)

        reorganized_string = []
        prev = None
        while heap or prev:
            if prev and not heap:
                return ""
            count, num = heapq.heappop(heap)
            reorganized_string.append(num)
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count != 0:
                prev = (count, num)
        return "".join(reorganized_string)



