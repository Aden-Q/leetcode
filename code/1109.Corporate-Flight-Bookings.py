class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for booking in bookings:
            first, last, seat = booking
            diff[first - 1] += seat
            if last < n:
                diff[last] -= seat
        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i-1] + diff[i]
            
        return res