import math
import pickle
import time

  
class SearchProblem:

	def __init__(self, goal, model, auxheur = []):
		self.goal = goal
		self.model = model 
		self.auxheur = auxheur 
		pass

	def getCoords(self, index):
		return self.auxheur[index]

	def getAdjs(self, index):
		return self.model[index]


	def search(self, init, limitexp = 2000):
		g_cost = 0 
		self.a_star(init)

	def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
		self.a_star(init)
		return []

	def a_star(self, init):
		openList = self.openListInit(init)
		closeList = self.closeList()
		#goalList = self.goalListInit()

	def openListInit(self, init):
		openList = []
		for i in range(len(init)):
			openList += [Node(init[i], None, 0, 0)]
		return openList

	def closedListInit(self, init):
		closedList = [[[],init]]
		return closedList

	def goalListInit(self):
		goalList = []
		for i in range(len(self.goal)):
			goalList += [Node(goal[i], None, 0, 0)]
		return goalList


class Node:
	def __init__(self, index, father, g, h):
		self.father = father;
		self.g = g
		self.h = h
		self.f = g + h 
		self.index = index
	
	def getFather(self):
		return self.father

	def getIndex(self):
		return self.index
