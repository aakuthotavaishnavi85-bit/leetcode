class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums"""
        i=0
        n=len(nums)
        ans=[0]*n
        j=n-1
        ind=-1
        while i<=j:
            
            if abs(nums[i])<abs(nums[j]):
                ans[ind]=nums[j]**2
                j-=1
            else:
                ans[ind]=nums[i]**2
                i+=1
            ind-=1
        return ans



            
