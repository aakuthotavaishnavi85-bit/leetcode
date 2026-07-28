class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        lenght=0
        k=len(s)
        while k>0:
            for i in range(len(s)-k+1):
                sub=s[i:i+k]
                if sub==sub[::-1]:
                    return sub
            k-=1
                


        

        