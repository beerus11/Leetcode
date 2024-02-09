class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        st = set()
        for i in nums:
            if i in st:
                st.remove(i)
            else:
                st.add(i)
        return list(st)[0]
        