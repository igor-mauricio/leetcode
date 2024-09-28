#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Using hash map
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            num_map[num] = i
        
# @lc code=end

