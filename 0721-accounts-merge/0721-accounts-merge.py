class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
            
        g = defaultdict(list)
        for account in accounts:
            for email in account[1:]:
                g[email].append(account[1])
                g[account[1]].append(email)
        visit = set()
        ans = []
        res = []
        
        def dfs(node):
            visit.add(node)
            for nei in g[node]:
                if nei not in visit:
                    dfs(nei)
            res.append(node)
            
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in visit:
                    res = []
                    dfs(email)
                    ans.append([name]+sorted(res))
        return ans