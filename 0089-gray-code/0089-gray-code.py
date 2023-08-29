class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i // 2) for i in range(pow(2, n))]