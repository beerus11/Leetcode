class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for a in strs:
            x = "".join(sorted(a))
            hm[x].append(a)
        return hm.values()
        