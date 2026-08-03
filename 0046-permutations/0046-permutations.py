class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = [[nums[0]]]
        for num in nums[1:]:
            result = [ res[0:i] + [num] + res[i:] for res in result for i in range(len(res)+1) ]
        return result