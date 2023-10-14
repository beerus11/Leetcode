
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome = Counter(ransomNote)
        for m in magazine:
            if m in ransome:
                ransome[m]-=1
            if ransome[m]==0:
                del ransome[m]
        return len(ransome)==0
        