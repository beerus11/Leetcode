class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        ans = []
        for i in range(len(people)):
            ans.insert(people[i][1],people[i])
        return ans