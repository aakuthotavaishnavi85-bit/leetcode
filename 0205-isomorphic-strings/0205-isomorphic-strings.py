class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """set1=set(s)
        set2=set(t)
        if len(set1)!=len(set2):
            return False
        else:"""
        d={}
        mapping=set()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in mapping:
                    return False
            d[s[i]]=t[i]
            mapping.add(t[i])
        return True
                    
                

        