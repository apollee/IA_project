
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
		path = []
		while currents[0].father:
			transports = []
			indexs = []
			joint = []
			for i in range(len(currents)):
				transports.append(currents[i].transport_index[0])
				indexs.append(currents[i].transport_index[1])
				joint.append(transports)
				joint.append(indexs)
				currents[i] = currents[i].father
				path.append(joint)
			transports = []
			indexs = []
			joint = []
			transports.append(currents[i].transport_index[0])
			indexs.append(currents[i].transport_index[1])
			joint.append(transports)
			joint.append(indexs)
			path.append(joint)

		return path
	
	def createNodes(self):
		node_list = []
		for i in range(0, 114):
			node_list.append(Node(i, None, 0, 0))
		
		return node_list
	
	#auxiliary functions
	def start_node_answer(self, list):
		return [[], [list[0].index]]

	def a_star(self, init, model, goal, tickets):
		
		openset = []
		currents = []
		for i in range(len(init)):
			currents.append(Node([[], init[i]], None, tickets))
		
		openset.append(currents)

		while openset:
			min = 1000
			for node in openset:  #[[no, no, no],*]
				for i in range(len(node)):	
					value_f = node[i].g + self.heuristic(goal[i], node[i])
					if(value_f < min):
						min = value_f
						currents[i] = node[i]

			
			flag_all_goal = 1
			for i in range(len(currents)):
				if currents[i].transport_index[1] != goal[i]:
					flag_all_goal = 0
					break
			
			if(flag_all_goal):
				self.createAnswer(currents)
				return path[::-1]
		
			openset.remove(currents)
			for i in range(len(currents)):
				for node in self.neighbors(currents[i].transport_index[1]):
					node = Node(node, currents[i], currents[i].tickets)
					node.reduceTickets(node.transport_index[0])
					if(node.tickets[node.transport_index[0]] < 0):
						continue
					flag = 0
					print(openset)
					for j in range(len(openset)):
						if openset[j][i].transport_index[1] == node.transport_index[1]:
							flag = 1
							break
					
					if flag:
						new_g = currents[i].g + 1
						if node.g > new_g:
							node.g = new_g
							node.father = currents[i]
					else:
						node.g = currents[i].g + 1
						node.h = self.heuristic(goal[i], node)
						node.father = currents[i]
						node_list = [node]
						openset.append(node_list)

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

	def __repr__(self):
		return str(self.transport_index[1])

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
