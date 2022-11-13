class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(" ")[::-1]
        arr = [i for i in arr if len(i)>0]
        return " ".join(arr)
        