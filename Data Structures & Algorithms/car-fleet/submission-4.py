class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        fleets = []
        for car in cars: 
            time = (target - car[0])/car[1]
            if not fleets or fleets[-1] < time: 
                fleets.append(time)
            else:
                continue
        return len(fleets)