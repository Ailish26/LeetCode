class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         if len(nums)==1:
            return nums[-1]

         max_sum=float("-inf")

         curr_sum=0

         for i in range(0,len(nums)):

             curr_sum=max(curr_sum+nums[i],nums[i])

             if max_sum<curr_sum:
                 max_sum=curr_sum
                
         return max_sum



        
        