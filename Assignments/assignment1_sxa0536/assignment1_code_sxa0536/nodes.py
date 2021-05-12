# Shubham Arya 1001650536

class Node:

    # initializes value when the class is first called.
    def __init__(self, key):
        # key - unique key of node, successor - successors of node, weight- cost between 2 nodes
        self.key = key
        self.successors = []
        self.cost_successors = {}

    # return the key of the node
    def getKey(self):
        return self.key

    # return the successors of the node
    def getSuccessors(self):
        return self.successors

    # add a node as a successor with the cost between the two nodes
    def addSuccessor(self, node, cost):
        if node.getKey() not in self.cost_successors:
            self.successors.append(node)
            self.cost_successors[node.getKey()] = cost

    # returns cost of successors
    def getCostSuccessors(self):
        return self.cost_successors
