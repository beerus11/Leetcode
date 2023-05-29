class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        mh = 0
        for i in gain:
            h+=i
            mh = max(mh,h)
        return mh
        