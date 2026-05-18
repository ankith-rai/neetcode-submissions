from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper_num = Counter(nums)
        result = sorted(mapper_num.keys(), key=lambda x: mapper_num[x], reverse=True)
        return result[:k]