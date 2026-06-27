class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        times = []
        for pos, speed in cars:
            times.append((target - pos) / speed)
            
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()
            
        return len(times)
