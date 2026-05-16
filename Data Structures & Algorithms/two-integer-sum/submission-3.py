from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)
        for i, n in enumerate(nums):
            if n in nums_map:
                return [nums_map[n], i]
            nums_map[target - n] = i
        return [-1, -1]