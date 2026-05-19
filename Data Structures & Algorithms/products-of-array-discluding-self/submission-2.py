class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_product = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            final_product[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            final_product[i] *= postfix
            postfix *= nums[i]
        
        return final_product