class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """for i in range(len(nums)):
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
                return nums[i]"""
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==nums[mid^1]:
                left=mid+1
            else:
                right=mid
        return nums[left]
            

            
            
            