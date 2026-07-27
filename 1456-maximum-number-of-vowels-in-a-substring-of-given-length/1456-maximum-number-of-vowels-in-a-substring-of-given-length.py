class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        vowels=['a','i','e','o','u']
        for i in range(k):
            if s[i] in vowels:
                count+=1
        max_count=count
        for j in range(k,len(s)):
            if s[j-k] in vowels:
                count-=1
            if s[j] in vowels:
                count+=1
            max_count=max(count,max_count)
        return max_count

