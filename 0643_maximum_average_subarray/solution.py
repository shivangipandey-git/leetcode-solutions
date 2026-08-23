from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first_sum = sum(nums[0:k])
        left = 0
        right = k
        max_sum = first_sum
        max_left = len(nums)-k
        for left in range (max_left):
            new_sum = first_sum - nums[left] + nums[right]
            first_sum = new_sum
            right +=1
            if new_sum> max_sum:
                max_sum = new_sum
        return max_sum/k