class Solution:
    def trap(self, height: List[int]) -> int:
        """prefix=[0]*len(height)
        prefix[0]=height[0]
        for i in range(1,len(height)):
            prefix[i]= max(prefix[i-1],height[i])
        suffix=[0]*len(height)
        suffix[len(height)-1]=height[len(height)-1]
        for i in  range (len(height)-2,-1,-1):
            suffix[i]=max(suffix[i+1],height[i])        
        total=0
        for i in range(len(height)):
            if height[i]<prefix[i] and height[i]<suffix[i]:
                total+=min(suffix[i],prefix[i])-height[i]
        return total"""
        leftmax=0
        rightmax=0
        left=0
        right=len(height)-1
        water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    water+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    water+=rightmax-height[right]
                right-=1
        return water
            




                
        