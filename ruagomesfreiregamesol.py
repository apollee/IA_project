import math
import pickle
import time

  
class SearchProblem:

	def __init__(self, goal, model, auxheur = []):
		self.goal = goal
		self.model = model 
		self.auxheur = auxheur 
		self.createNodes()
		pass

	def getCoords(self, index):
		return self.auxheur[index]

	def getAdjs(self, index):
		return self.model[index]

	def search(self, init, limitexp = 2000):
		g_cost = 0 

	def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
		return []

	def createNodes(self):
		node_list = []
		for i in range(0, 114):
			node_list.append(Node(i, None, 0))
		
		return node_list
	
	def getNode(self, index):
		return node_list[index]
	
	def getTransport(self, index):
		pass
	
	def getSucessors(self, index): #[[transport, sucesssors]*]
		return self.model[index]

	def BFS(init, goal, model, node_list):
		queue = []
		node_list[init[0]].setVisited() #set first node as visited
		queue.append(node_list[init[0]])

		while queue:
			vertex = queue.pop(0) #node
			for neighbour in self.getSucessors(vertex.getIndex())
				if not (node_list[neighbour[1]].isVisited()):
					node_list[neighbour[1]].setVisited()
					queue.append(node_list[neighbour[1]])
		

class Node:
	def __init__(self, index, father, visited):
		self.index = index
		self.father = father
		self.visited = visited
	
	def getFather(self):
		return self.father

	def getIndex(self):
		return self.index

	def isVisited(self):
		return self.visited

	def setFather(self, father):
		self.father = father
	
	def setVisited(self):
		self.visited = 1
	
	










