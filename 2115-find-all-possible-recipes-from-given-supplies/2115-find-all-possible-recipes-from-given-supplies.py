from collections import defaultdict
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        
        g = defaultdict(list)
        all_ingredients = [item for i in ingredients for item in i]
        indegree = {i:0 for i in all_ingredients+recipes }
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        
        for k,i in enumerate(ingredients):
            for item in i:
                g[item].append(recipes[k])
                indegree[recipes[k]]+=1
        q = [item for item,deg in indegree.items() if deg ==0]
        ans = []
        while q:
            item = q.pop(0)
            if item in recipes_set:
                ans.append(item)
                supplies_set.add(item)
                
            if item not in supplies_set:
                continue
                
            for nei in g[item]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    
        return ans
            
            
        