"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id:e for e in employees}
        def dfs(eid):
            emp = emap[eid]
            imp = emp.importance
            for nei in emp.subordinates:
                imp+=dfs(nei)
            return imp
        return dfs(id)
        
        