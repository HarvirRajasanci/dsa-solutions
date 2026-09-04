class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(heap)

        reorganized_string = []
        prev = None
        while heap or prev:
            if prev and not heap:
                return ""

            count, char = heapq.heappop(heap)
            reorganized_string.append(char)
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None
                
            if count:
                prev = (count, char)

        return "".join(reorganized_string)