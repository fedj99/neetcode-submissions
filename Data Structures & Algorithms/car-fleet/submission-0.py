class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort by position decreasing
        cars = sorted([(x, v) for x, v in zip(position, speed)], key=lambda car: car[0], reverse=True)

        # Go through cars, compute TTA, build fleets
        fleets = []
        for x, v in cars:
            tta = (target - x) / v
            if len(fleets) == 0 or tta > fleets[-1]:
                # New fleet, otherwise tta <= fleets[-1] and this car will catch up with the next fleet,
                # merging and not creating a new fleet. In this case, we'll never catch up the next fleet
                # and so we create a new fleet.
                fleets.append(tta)

        return len(fleets)
