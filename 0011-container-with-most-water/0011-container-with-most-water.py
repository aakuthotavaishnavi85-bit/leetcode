class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        """n=len(height)
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                width=j-i
                ht=min(height[j],height[i])
                area=width*ht
                maxi=max(maxi,area)
        return maxi"""
        n=len(height)
        i=0
        j=n-1
        max_water=0
        while i<j:
            wd=j-i
            ht=min(height[i],height[j])
            area=wd*ht
            max_water=max(max_water,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water



