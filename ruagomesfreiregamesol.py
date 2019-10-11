import math
import pickle
import time

  
class SearchProblem:

  	def __init__(self, goal, model, auxheur = []):
    	self.goal = goal;
    	self.model = model;
    	self.auxheur = auxheur;
    	pass

  	def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
   		openList = initOpenList(self.init, self.model)
   		closedList = initClosedList(init)
   		while len(openList) != 0 :



    	return closedList

    def initOpenList(init, matrix):
    	openList = []
    	for i in range(len(init)):
    		openList += matrix[init[i]]
    	return openList

    def initClosedList(init):
    	closedList = []
    	closedList += [[], init]
    	return closedList

    def selectChild(fater ,listAdj, goal):
    	distance = distance(listAdj[0], goal)   
    	point = listAdj[0]
    	for i in range(len(listAdj)- 1):
    		j = i + 1
    		newDistance = distance(listAdj[j], goal)
    		if distance < newDistance:
    			distance = newDistance
    			point = listAdj[j]



    def distance(point, goal):
    	return Math.sqrt((point[0]-goal[0]).pow(2)+(point[1]-goal[1]).pow(2))

    
  