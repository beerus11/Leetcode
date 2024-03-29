'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
from collections import defaultdict
class Solution:
    def ladoos(self, root, home, k):
        # Your code goes here
        g = defaultdict(list)
        def dfs(parent,node):
            if not node:
                return
            if parent.data!=-1:
                g[parent.data].append(node.data)
                g[node.data].append(parent.data)
            dfs(node,node.left)
            dfs(node,node.right)
        dfs(Node(-1),root)
        q = [(home,0)]
        ans = 0
        visited = set()
        while q:
            n,d = q.pop(0)
            visited.add(n)
            if d<=k:
                #print(n)
                ans += n
            for nei in g[n]:
                if nei not in visited and d+1<=k:
                    q.append((nei,d+1))
        return ans
        
        
                



#{ 
 # Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        home=int(line[0])
        k=int(line[1])
        obj = Solution();
        print(obj.ladoos(root,home,k))


# } Driver Code Ends