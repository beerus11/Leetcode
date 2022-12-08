class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = [s[0]]
        i=1
        while i < len(s):
            if len(st)==0:
                st.append(s[i])
            elif s[i]!=st[-1]:
                st.append(s[i])
            else:
                st.pop()
            i+=1
        return "".join(st)
        
        