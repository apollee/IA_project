
import math
import pickle
import time
import heapq

  
class SearchProblem:

	def __init__(self, goal, model, auxheur = []):
		self.goal = goal
		self.model = model 
		self.auxheur = auxheur 
		#self.createNodes()
		pass

	def getCoords(self, index):
		return self.auxheur[index]

	def getAdjs(self, index):
		return self.model[index]

	def search(self, init, limitexp = 2000):
		g_cost = 0 

	def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
		return self.a_star(init, self.model, self.goal, tickets)
		return []

	def createAnswer(self, list):
		final_list = []
		final_list.append(self.start_node_answer(list))

		for i in range(1, len(list)):
			final_list.append([[list[i].transport], [list[i].index]])

		return final_list
	
	def createNodes(self):
		node_list = []
		for i in range(0, 114):
			node_list.append(Node(i, None, 0, 0))
		
		return node_list
	
	#auxiliary functions
	def start_node_answer(self, list):
		return [[], [list[0].index]]

	def a_star(self, init, model, goal, tickets):
		goal = goal[0]
		init = init[0]
		
		openset = set()
		closedset = set()
		current = Node([[], init], None, tickets)
		openset.add(current)

		while openset:

			min = 1000
			for node in openset: 
				value = node.g + self.heuristic(goal, node)
				if(value < min):
					min = value
					current = node

			if current.transport_index[1] == goal:
				path = []
				while current.father:
					path.append(current.transport_index)
					current = current.father
				path.append(current.transport_index)
				return path[::-1]
		
			openset.remove(current)
			#closedset.add(current)
			for node in self.neighbors(current.transport_index[1]):
				node = Node(node, current, current.tickets)
				node.reduceTickets(node.transport_index[0])
				if(node.tickets[node.transport_index[0]] < 0):
					continue
				#if node in closedset:
				#	continue
				if node in openset:
					new_g = current.g + 1
					if node.g > new_g:
						node.g = new_g
						node.father = current
				else:
					node.g = current.g + 1
					node.h = self.heuristic(goal, node)
					node.father = current
					openset.add(node)

	def heuristic(self, goal, node):

		h2 = self.calculateH2(node.transport_index[0])
		h3 = self.calculateH3(goal, node.transport_index[1])

		return h2 + h3

	def calculateH2(self, node):
		if(node == 0): 
			return 3
		elif(node == 1):
			return 2
		else:
			return 1
	
	def calculateH3(self, goal, node):
		x1 = self.auxheur[node - 1][0]
		x2 = self.auxheur[goal - 1][0]
		y1 = self.auxheur[node - 1][1]
		y2 = self.auxheur[goal - 1][1]
		return math.sqrt((x2 - x1)**2 + (y2-y1)**2) / 120
	
	def neighbors(self, index):
		return self.model[index] 

class Node:
	def __init__(self, transport_index, father, tickets):
		self.transport_index = transport_index
		self.father = father
		self.tickets = tickets.copy()
		
		self.g = 0
		self.h = 0
		self.f = 0
		
	def getFather(self):
		return self.father

	def getIndex(self):
		return self.index
		
	def getG(self):
		return self.g
		
	def getH(self):
		return self.h 
	
	def getF(self):
		return self.f
	
	def reduceTickets(self, transport):
		self.tickets[transport] -= 1
