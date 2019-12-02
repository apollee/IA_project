import random
from math import inf 

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):

                # define this function
                self.nS = nS
                self.nA = nA
                self.gamma =  0.75
                self.alpha = 0.5
                self.tableQ = [[0 for i in range(nA)] for i in range(nS)]
                self.tableF = [[-inf for i in range(nA)] for i in range(nS)]
                
                # define this function
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                min_value = inf
                counter = 0
                for i in aa:
                    if(min_value > self.tableF[st][i]):
                        min_value = self.tableF[st][i]
                        a = [i, counter]
                    counter += 1

                self.tableF[st][a[0]] += 1
                return a[1]

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                max_value = -inf
                counter = 0

                for i in aa:
                        if(max_value < self.tableQ[st][i]):
                                max_value = self.tableQ[st][i]
                                index = counter
                                a = [i, counter]
                        counter += 1

                return a[1]
                


        # this function is called after every action
        # st - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,st,nst,a,r):
                # define this function
                self.tableQ[st][a] = self.tableQ[st][a] + self.alpha * (r + self.gamma * max(self.tableQ[nst]) - self.tableQ[st][a])
                return 
