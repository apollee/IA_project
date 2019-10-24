import math
import pickle
import time
from itertools import product



class SearchProblem:

	def __init__(self, goal, model, auxheur = []):
		self.goal = goal
		self.model = model 
		self.auxheur = auxheur 
		self.matrix = floydWarshall(self.model)
		self.expansion = 0
		#self.createNodes()
		pass

	def getCoords(self, index):
		return self.auxheur[index]

	def getAdjs(self, index):
		return self.model[index]

	def search(self, init, limitexp = 2000):
		g_cost = 0 

	def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
		
		if(len(init) == 1):
			return self.a_star_1_2(init, self.model, self.goal, tickets)
		elif(len(init) == 3):
			return self.a_star_3_4(init, self.model, self.goal, tickets, self.matrix)
		return []

	def createAnswer(self, list_nodes):
		final_list = []
		for i in range(len(list_nodes[0])):
			list_for_onepath = []
			list_indexes = []
			list_transports = []
			for j in range(len(list_nodes)):
				if(i != 0):
					list_transports.append(list_nodes[j][i].transport_index[0])
				list_indexes.append(list_nodes[j][i].transport_index[1])
			list_for_onepath.append(list_transports)
			list_for_onepath.append(list_indexes)
			final_list.append(list_for_onepath)

		
		#print(final_list)
		print(self.expansion)

		return final_list
	
	def createNodes(self):
		node_list = []
		for i in range(0, 114):
			node_list.append(Node(i, None, 0, 0))
		
		return node_list
	
	#auxiliary functions
	def start_node_answer(self, list):
		return [[], [list[0].index]]

	def a_star_1_2(self, init, model, goal, tickets):
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
				print(path[::-1])
				return path[::-1]
		
			openset.remove(current)
			for node in self.neighbors(current.transport_index[1]):
				node = Node(node, current, current.tickets)
				node.reduceTickets(node.transport_index[0])
				if(node.tickets[node.transport_index[0]] < 0):
					continue
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

	def a_star_3_4(self, init, model, goal, tickets, matrix):
		maxDistance = max(matrix[init[0]][goal[0]], matrix[init[1]][goal[1]], matrix[init[2]][goal[2]])
		#for em volta disto!!!


		while maxDistance < 10:
			copspathList = []
			for i in range(len(init)):
				copspathList.append((self.calculatePath(maxDistance-1, init[i], goal[i], tickets)))
			flag = 1
			for cop in copspathList:
				if(cop == []):
					flag = 0
					maxDistance += 1
					break
			if flag:
				lst = self.detectCollisions(copspathList, tickets)
				if lst != []:
					List = self.createAnswer(lst)
					return List
				else:
					maxDistance += 1
		return []
	
	def calculatePath(self, maxDistance, init, goal, tickets):
		current = Node([[], init], None, tickets)
		openset = list()
		openset.append([current])
		while maxDistance != -1:
			length = len(openset)
			while length:
				for child in self.neighbors(openset[0][-1].transport_index[1]):
					self.expansion += 1
					if(self.matrix[child[1]][goal] <= maxDistance or child[1] == goal):
						newNode = Node([child[0], child[1]], openset[0][-1], tickets)
						newList = openset[0].copy()	
						newList.append(newNode)
						openset.append(newList)
				length-= 1
				openset.remove(openset[0])
			maxDistance -= 1
		return openset

	def detectCollisions(self, copspathList, tickets):

		for lst in product(copspathList[0], copspathList[1], copspathList[2]):
			flag_collisions = 1
			newTickets = tickets.copy()
			for j in range(len(lst[0])):
				if lst[0][j].transport_index[1] == lst[1][j].transport_index[1]:
					flag_collisions = 0
					break
				if lst[0][j].transport_index[1] == lst[2][j].transport_index[1]:
					flag_collisions = 0
					break 
				if lst[1][j].transport_index[1] == lst[2][j].transport_index[1]:
					flag_collisions = 0
					break
				#print(lst[0][j].transport_index[0])
				if(lst[0][j].transport_index[0] != []):
					newTickets = self.reduceTickets(lst[0][j].transport_index[0], newTickets)
					newTickets = self.reduceTickets(lst[1][j].transport_index[0], newTickets)
					newTickets = self.reduceTickets(lst[2][j].transport_index[0], newTickets)
				if(not self.checkTickets(newTickets)):
					flag_collisions = 0	
					break
			if(flag_collisions and self.checkTickets(newTickets)):
				return lst
		return []

	def checkTickets(self, tickets):
		for i in range(len(tickets)):
			if tickets[i] < 0 :
				return False
		return True

	def heuristic3(self, goal, node):
		return self.matrix[node.transport_index[1]][goal]

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

	def reduceTickets(self, transport, tickets):
		tickets[transport] -= 1
		return tickets
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



def floydWarshall(model):
	path_deep = []
	for i in range(len(model)):
		path_deep.append([])
		for j in range(len(model)):
			path_deep[i].append(math.inf)
	
	for i in range(len(model)):
		for j in range(len(model[i])):
			path_deep[i][model[i][j][1]] = 1
	
	for k in range(len(model)):
		for i in range(len(model)):
			for j in range(len(model)):
				if path_deep[i][k] + path_deep[k][j] < path_deep[i][j]:  
					path_deep[i][j] = path_deep[i][k] + path_deep[k][j] 

	return path_deep

def printFloyd(lst):
	for i in range(len(lst)):
		print(str(i) + " " +str(lst[i]))