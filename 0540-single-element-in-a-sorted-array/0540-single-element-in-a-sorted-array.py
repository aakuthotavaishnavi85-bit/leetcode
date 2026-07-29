class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(nums)==1:
                return nums[i]
            if i==0:
                if nums[i]==nums[i+1]:
                    continue
                return nums[i]
            elif i==len(nums)-1:
                if nums[i]==nums[i-1]:
                    continue
                return nums[i]
            else:
                if nums[i]==nums[i+1] or nums[i]==nums[i-1]:
                    continue
                return nums[i]