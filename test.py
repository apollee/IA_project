def createAnswer(self, list):
		final_list = []
		final_list.append(self.start_node_answer(list)) #first node

		for i in range(1, len(list)):
			list_node_transport, list_node_index, list_path = ([] for i in range(3))
			transport = list[i].transport
			list_node_transport.append(list[i].transport)
			list_node_index.append(list[i].index)
			list_path.append(list_node_transport)
			list_path.append(list_node_index)
			final_list.append(list_path)
		
		return final_list
	
	#auxiliary function
	def start_node_answer(self, list):
		list_node_transport, list_node_index, list_path = ([] for i in range(3))
		list_node_index.append(list[0].index)
		list_path.append(list_node_transport)
		list_path.append(list_node_index)
		return list_path

#######################################################

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
		return self.BFS(init, self.goal, self.model, node_list)
		#return []

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
			for neighbour in self.getInfoSucessors(vertex.index):			
				if(neighbour[1] == goal[0]):
					node_list[neighbour[1]].setFather(vertex) #set father index
					node_list[neighbour[1]].setTransport(neighbour[0])
					return self.traceBack(node_list[neighbour[1]])

				else:
					if not (node_list[neighbour[1]].visited):
						node_list[neighbour[1]].setFather(vertex) #set father index
						node_list[neighbour[1]].setTransport(neighbour[0])
						node_list[neighbour[1]].setVisited()
						queue.append(node_list[neighbour[1]])
		
	def traceBack(self, node):
		list = []
		list.insert(0, node)

		current_father = node.getFather()
		while(current_father != None):
			list.insert(0, current_father)
			current_father = current_father.getFather() 
		
		return self.createAnswer(list)
	
	def createAnswer(self, list):
		final_list = []
		#for the first one
		list_node_transport = []
		list_node_index = []
		list_node_index.append(list[0].index)
		list_path = []
		list_path.append(list_node_transport)
		list_path.append(list_node_index)

		final_list.append(list_path)

		for i in range(1, len(list)):
			list_node_transport = []
			transport = list[i].transport
			list_node_transport.append(list[i].transport)
			list_node_index = []
			list_node_index.append(list[i].index)

			list_path = []
			list_path.append(list_node_transport)
			list_path.append(list_node_index)

			final_list.append(list_path)
		
		return final_list

class Node:
	def __init__(self, index, father, visited):
		self.index = index
		self.father = father
		self.visited = visited
		self.transport = None
	
	def getFather(self):
		return self.father

	def getIndex(self):
		return self.index

	def setFather(self, father):
		self.father = father
	
	def setVisited(self):
		self.visited = 1
	
	def setTransport(self, number):
		self.transport = number
	










