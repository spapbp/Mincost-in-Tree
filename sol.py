class Node:
    def __init__(self, edge_list, letter):
        self.edge_list = edge_list
        self.letter = letter

class Edge:
    def __init__(self, target, cost):
        self.target = target
        self.cost = cost
        
K = Node([], "K")
J = Node([], "J")        
I = Node([Edge(J, 1),
        Edge(K, 2)], "I")
H = Node([], "H")
G = Node([], "G")
F = Node([], "F")
E = Node([], "E")
D = Node([Edge(H, 1),
        (Edge(I, 1))], "D")
C = Node([Edge(G, 3)], "C")        
B = Node([Edge(E, 4),
        Edge(F, 5)], "B")

A = Node([Edge(B, 7),
        Edge(C, 3),
        Edge(D, 8)], "A")
        
        
def sol(root):
    # return node and min val
    def dfs(root, cost, minCost):
        
        # if leaf node return the cost and node letter
        if not root.edge_list:
            return [cost, root.letter]
        
        # dfs the child 
        for child in root.edge_list:
            curCost = cost + child.cost
            
            # dfs returns [cost, letter]
            leafCost = dfs(child.target, curCost, minCost)
            # if the cost of leaf is less the current minCost then update value
            if leafCost[0] < minCost[0]:
                minCost = leafCost
            
        return minCost
        
    return dfs(root, 0, [999, "A"])
        
print(sol(A))
        
        
        
        
        

