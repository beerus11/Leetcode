from collections import defaultdict
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        d = defaultdict(int)
        for w in word1:
            d[str(w)]+=1
        d1 = defaultdict(int)
        for w in word2:
            d1[str(w)]+=1
        if set(d.keys())!=set(d1.keys()):
            return 
        a = sorted(d.values())
        b = sorted(d1.values())
        return a==b
        
        