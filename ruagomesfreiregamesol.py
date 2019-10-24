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
		pass

	def neighbors(self, index):
		return self.model[index] 

	def search(self, init, limitexp = 2000):
		g_cost = 0 

	def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
		
		if(len(init) == 1):
			print("not doing it rn")
			#return self.a_star_3_4(init, self.model, self.goal, tickets, self.matrix, limitdepth)
		elif(len(init) == 3):
			return self.a_star_3_4(init, self.model, self.goal, tickets, self.matrix, limitdepth)
		else:
			return []

	def a_star_3_4(self, init, model, goal, tickets, matrix, max_depth):
		depth_to_explore = max(matrix[init[i]][goal[i]] for i in range(len(init))) #allow more than one cop

		while depth_to_explore < max_depth:
			cops_path = []
			for i in range(len(init)):
				cops_path.append((self.calculatePath(depth_to_explore-1, init[i], goal[i], tickets)))
			
			#check if there is a valid solution with current_node depth
			if [] not in cops_path:
				solution_path = self.detectCollisions(cops_path, tickets)
				if len(solution_path) > 0: #found valid solution
					return self.createAnswer(solution_path)
			
			#increase depth if no solution found
			depth_to_explore += 1
		
		return []
	
	def calculatePath(self, maxDistance, init, goal, tickets):
		current_node = Node([[], init], None, tickets)
		openset = list() #set of nodes to explore
		openset.append([current_node])
		
		while maxDistance != -1:
			n_nodes_to_explore = len(openset)
			while n_nodes_to_explore:
				for child in self.neighbors(openset[0][-1].getIndex()):
					if(self.matrix[child[1]][goal] <= maxDistance or child[1] == goal):
						newNode = Node([child[0], child[1]], openset[0][-1], tickets)
						new_node_list = openset[0].copy()	
						new_node_list.append(newNode)
						openset.append(new_node_list)
				n_nodes_to_explore -= 1
				openset.remove(openset[0])
			maxDistance -= 1
		return openset

	def detectCollisions(self, copspathList, tickets):
		prod = product(copspathList[i] for i in range(len(copspathList)))
		prod2 = product(copspathList[0], copspathList[1], copspathList[2])	
		print(prod)
		print(prod2)

		for lst in product(copspathList[0], copspathList[1], copspathList[2]):
			flag_collisions = 1
			newTickets = tickets.copy()
			for j in range(len(lst[0])):
				if lst[0][j].getIndex() == lst[1][j].getIndex():
					flag_collisions = 0
					break
				if lst[0][j].getIndex() == lst[2][j].getIndex():
					flag_collisions = 0
					break 
				if lst[1][j].getIndex() == lst[2][j].getIndex():
					flag_collisions = 0
					break
				if(lst[0][j].getTransport() != []):
					newTickets = self.reduceTickets(lst[0][j].getTransport(), newTickets)
					newTickets = self.reduceTickets(lst[1][j].getTransport(), newTickets)
					newTickets = self.reduceTickets(lst[2][j].getTransport(), newTickets)
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

	def createAnswer(self, list_nodes):
		final_list = []
		for i in range(len(list_nodes[0])):
			list_for_onepath = []
			list_indexes = []
			list_transports = []
			for j in range(len(list_nodes)):
				if(i != 0):
					list_transports.append(list_nodes[j][i].getTransport())
				list_indexes.append(list_nodes[j][i].getIndex())
			list_for_onepath.append(list_transports)
			list_for_onepath.append(list_indexes)
			final_list.append(list_for_onepath)

		return final_list
	
	def reduceTickets(self, transport, tickets):
		tickets[transport] -= 1
		return tickets

class Node:

	def __init__(self, transport_index, father, tickets):
		self.transport_index = transport_index
		self.father = father
	
	def __repr__(self):
		return str(self.transport_index[1])

	def getFather(self):
		return self.father

	def setFather(self, father):
		self.father = father

	def getIndex(self):
		return self.transport_index[1]
	
	def getTransport(self):
		return self.transport_index[0]



def floydWarshall(model):
	path_deep = []

	#initialize matrix
	for i in range(len(model)):
		path_deep.append([])
		for j in range(len(model)):
			path_deep[i].append(math.inf) 
	
	#insert depth of all connections in matrix
	for i in range(len(model)):
		for j in range(len(model[i])):
			path_deep[i][model[i][j][1]] = 1
	
	for k in range(len(model)):
		for i in range(len(model)):
			for j in range(len(model)):
				if path_deep[i][k] + path_deep[k][j] < path_deep[i][j]:  
					path_deep[i][j] = path_deep[i][k] + path_deep[k][j] 

	return path_deep