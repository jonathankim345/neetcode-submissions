class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        N = len(position)
        cars = []
        for i in range(N): 
            cars.append((position[i], speed[i]))
        cars.sort(key = lambda x:x[0], reverse = True)
        times = []
        for i in range(N):
            time = (target - cars[i][0])/cars[i][1]
            if len(times) == 0 or times[-1] < time: 
                times.append(time)
                fleets += 1
        return fleets