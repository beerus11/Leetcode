class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        seen = set()
        
        last_occurrence = {c:i for i,c in enumerate(s)}
        
        for i,c in enumerate(s):
            if c not in seen:
                while st and c<st[-1] and i< last_occurrence[st[-1]]:
                    seen.remove(st.pop())
                seen.add(c)
                st.append(c)
        return ''.join(st)
        