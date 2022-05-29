class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)
        
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
        