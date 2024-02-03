class Solution:
    def countLetters(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            st = s[i]
            count+=1
            for j in range(i+1,len(s)):
                if st!=s[j]:
                    break
                count+=1
        return count
        