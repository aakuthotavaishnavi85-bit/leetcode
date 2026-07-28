class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        else:
            for i in range(n,0,-1):
                prefix=s[:i]
                if prefix==prefix[::-1]:
                    break
            remaining=s[i:]
            return remaining[::-1]+s
        

        