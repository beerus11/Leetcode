class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ss = []
        count = defaultdict(int)
        for i in range(minSize,maxSize+1):
            j = 0
            while j < len(s)-i+1:
                x = s[j:j+i]
                if len(set(x))<=maxLetters:
                    ss.append(x)
                    count[x]+=1
                j+=1
        if len(ss)==0:
            return 0
        return max(count.values())