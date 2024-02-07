class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        seen = set()
        last_occur = {v:k for k,v in enumerate(s)}
        for i in range(len(s)):
            if s[i] not in seen:
                while st and st[-1]>s[i] and i<last_occur[st[-1]]:
                    seen.remove(st.pop())
                st.append(s[i])
                seen.add(s[i])
        return "".join(st)
        