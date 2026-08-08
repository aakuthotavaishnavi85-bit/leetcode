class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m=len(g)
        n=len(s)
        g.sort()
        s.sort()
        i=j=0
        count=0
        while i<m and j<n:
            if g[i]<=s[j]:
                count+=1
                i+=1
            j+=1
        return count