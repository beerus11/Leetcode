class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1,n+1)]

        def backtrack(path,index):
            if len(path) == n: self.res.append(path)
            for i in range(len(nums)):
                x = ((i+1) not in self.visited)
                y = ((index+1)%nums[i] == 0 or nums[i]%(index+1) == 0)
                if x and y:
                    self.visited.add(i+1)
                    backtrack(path+[nums[i]],index+1)
                    self.visited.remove(i+1)

        self.res = []
        self.visited = set()
        backtrack([],0)

        return len(self.res)
        