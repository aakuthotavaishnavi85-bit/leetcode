class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        half=s[:n//2]
        half ="".join(sorted(half))
        if n%2==0:
            return half+half[::-1]
        else:
            middle=s[n//2]
            return half + middle + half[::-1]


        