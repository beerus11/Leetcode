class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)/2
        vs = set(['a','e','i','o','u'])
        a,b=s[:l],s[l:]
        def count_vowel(string):
            count = 0
            for i in string:
                if i.lower() in vs :
                    count+=1
            return count
        return count_vowel(a)==count_vowel(b)
                