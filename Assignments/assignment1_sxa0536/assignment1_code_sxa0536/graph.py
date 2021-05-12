# Shubham Arya 1001650536

from nodes import *

class Graph:

	def __init__(self):
		self.nodes = {}

	# adds a node in the graph passing a node key. Checks if the node already exists. If it does not, then it
	# creates an instance of the node and stores the node
	def addNode(self, node_key):
		if node_key not in self.nodes:
			node = Node(node_key)
			self.nodes[node_key] = node

	# connect the nodes in the graph if the keys do not already exist in the graph
	def connect(self, start, destination, cost):
		self.nodes[start].addSuccessor(self.nodes[destination], cost)

	# returns the edge cost between 2 nodes if the keys exists and are different.
	def getEdgeCost(self, current, successor):
		cost_successors = self.nodes[current].getCostSuccessors()
		if successor in cost_successors:
			return cost_successors[successor]

	# returns all successors of a node (i.e. adjacent nodes)
	def getSuccessors(self, cnode):
		nodes = self.nodes[cnode].getSuccessors()
		return [node.getKey() for node in nodes]

	# returns all nodes in the graph.
	def getNodes(self):
		return self.nodes
