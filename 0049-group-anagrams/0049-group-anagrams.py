class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        group={}
        for i in strs:
            k="".join(sorted(i))
            if k not in group:
                group[k]=[]
            group[k].append(i)
        return list(group.values())

