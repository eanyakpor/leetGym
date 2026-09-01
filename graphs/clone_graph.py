'''
RAMPER
R - restate the problem
    given a connected node from a undirected graph
    return the a depp copy of that graph 
    a deep copy is 
    not only is the references the same and paired as the original
    but completly new objects are made with their own references copying what the oroginal had done
A - ask any questions 
    given an adjancey list how do i convert it to graph?
    
M - make an example 
    input to large for that one chief
    understood froom image example on leetcode.com though
P - pick a pattern
    hashmap dfs traversal 
E - explain the plan
    convert adj list to graph 
    create a hashmpap
    hashmap will contain old node as key and new noes as value 
    iterate through old graph
    each time we see an old node and its reference have the new node
    point to the another new nodes reference formulating a deep copy

    convert adjlist to graph through connected undirected conncetion
    create a hashmap of all the old nodes in the graph and have the values be created new nodes with its own new refernces
        idk how to this part or underitstand it full ngl -> iterate through the hashmap and connect new nodes with its references similar to old nodes 
'''
def cloneGraph(node):
    cloneMap = {}

    def dfs(node):

        # already cloned?
        if node in cloneMap or node is None:
            return cloneMap[node]

        # otherwise create new Node
        copy = Node(node.val, [])

        # save old -> new
        cloneMap[node] = copy

        # we'll handle neighbors afterward
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    dfs(node)



