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
		node_list = self.createNodes()
		self.BFS(init, self.goal, self.model, node_list)
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
	
	def getInfoSucessors(self, index): #[[transport, sucesssors]*]
		return self.model[index]

	def getSucessors(self, index):
		list = []
		for i in range(len(self.model[index])):
			list.append(self.model[index][i][1])
		
		return list

	def BFS(self, init, goal, model, node_list):
		queue = []
		node_list[init[0]].setVisited() #set first node as visited
		queue.append(node_list[init[0]])

		while queue:
			vertex = queue.pop(0) #node
			for neighbour in self.getSucessors(vertex.index):			
				if(neighbour == goal[0]):
					node_list[neighbour].setFather(vertex) #set father index
					return self.traceBack(node_list[neighbour])

				else:
					if not (node_list[neighbour].visited):
						node_list[neighbour].setFather(vertex) #set father index
						node_list[neighbour].setVisited()
						queue.append(node_list[neighbour])
		
	def traceBack(self, node):
		list = []
		list.insert(0, node)

		current_father = node.getFather()
		while(current_father != None):
			list.insert(0, current_father)
			current_father = current_father.getFather() 
		
		self.printList(list)
		

	def printList(self, list):
		for i in range(len(list)):
			print("My number is " + str(list[i].index))
		

class Node:
	def __init__(self, index, father, visited):
		self.index = index
		self.father = father
		self.visited = visited
	
	def getFather(self):
		return self.father

	def getIndex(self):
		return self.index

	def setFather(self, father):
		self.father = father
	
	def setVisited(self):
		self.visited = 1
	
	










