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
		return self.BFS(init, self.goal, self.model, node_list, tickets)
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

	def BFS(self, init, goal, model, node_list, tickets):
		queue = []
		node_list[init[0]].setVisited() #set first node as visited
		queue.append(node_list[init[0]])
		while queue:
			vertex = queue.pop(0) #node
			for neighbour in self.getInfoSucessors(vertex.index):
				if(neighbour[1] == goal[0]):
					node_list[neighbour[1]].setFather(vertex) #set father index
					node_list[neighbour[1]].setTransport(neighbour[0])
					try_list = self.traceBack(node_list[neighbour[1]], tickets)
					#if(try_list != []):
					#	return try_list

				else:
					if not (node_list[neighbour[1]].visited):
						node_list[neighbour[1]].setFather(vertex) #set father index
						node_list[neighbour[1]].setTransport(neighbour[0])
						node_list[neighbour[1]].setVisited()
						queue.append(node_list[neighbour[1]])
		
	def traceBack(self, node, tickets):
		list = []
		list.insert(0, node)
		tickets_copy = tickets.copy()

		current_father = node.getFather()
		transport = node.getTransport()
		while(current_father != None):
			tickets_copy = self.reduce_tickets(tickets_copy, transport)
			list.insert(0, current_father)
			current_father = current_father.getFather() 
		
		for i in range(0,3):
			if(tickets_copy[i] < 0):
				print(self.createAnswer(list))
				return []
		
		print(self.createAnswer(list))
		return self.createAnswer(list)
		
	def createAnswer(self, list):
		final_list = []
		final_list.append(self.start_node_answer(list))

		for i in range(1, len(list)):
			final_list.append([[list[i].transport], [list[i].index]])

		return final_list
	
	#auxiliary functions
	def start_node_answer(self, list):
		return [[], [list[0].index]]

	def reduce_tickets(self, tickets, transport):	
		if(transport == 0):
			tickets[0] -= 1
		elif(transport == 1):
			tickets[1] -= 1
		else:
			tickets[2] -= 1
		
		return tickets

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
	
	def getTransport(self):
		return self.transport

	def setFather(self, father):
		self.father = father
	
	def setVisited(self):
		self.visited = 1
	
	def setTransport(self, number):
		self.transport = number
	










