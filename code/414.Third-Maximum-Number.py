import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        
        min_heap = [nums.pop() for _ in range(3)]
        heapq.heapify(min_heap)
        for num in nums:
            if num < min_heap[0]:
                continue
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
            
        return min_heap[0]