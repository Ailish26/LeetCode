class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
      counts = Counter(nums)
      return sum(num for num,count in counts.items() if count==1)  