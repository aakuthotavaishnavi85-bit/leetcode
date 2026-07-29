class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]"""
        two_sum={}
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in two_sum:
                return [i,two_sum[remaining]]
            else:
                two_sum[nums[i]]=i
                