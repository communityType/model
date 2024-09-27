import networkx as nx
import random
import numpy as np
import math

class User(): 
    def __init__(self,index,attribute,ps,alpha,beta):
        self.index = index
        self.attribute = attribute
        self.pswap = ps[0]
        self.pA = ps[1]
        self.pAdd = 1-ps[2]
        self.alpha = alpha
        self.beta = beta

        
    def activate(self,g):
        current = self.search_current(g)
        candidate = self.search_candidate(g)
        
#         print("====================================")       
        if random.uniform(0, 1) <= self.pswap: #Swapping
            if current != 'NOT FOUND' and candidate != 'NOT FOUND':
                if random.uniform(0, 1) <= self.pA:
                    g = self.moveA(g,current,candidate)
                else:
                    g = self.moveD(g,current,candidate)
        else: #Changing
            if random.uniform(0, 1) <= self.pAdd:
                if candidate == 'NOT FOUND':
                    nodes = [n for n in g.nodes()]
                    nodes.remove(self.index)
                    candidate = random.choices(nodes)[0]
                g = self.moveAdd(g,candidate)    
#               print("Add")
            else:
                if current != 'NOT FOUND':
                    g = self.moveRemove(g,current)
#               print("Remove")
                
        return g;
        
    
    def search_candidate(self,g):
        found = False
        origin = self.index
        following = [n for n in g.predecessors(self.index)]
        if len(following) == g.number_of_nodes() -1:
            return "NOT FOUND";
        available = [n for n in g.nodes() if n != origin and n not in following]
        
        return random.choices(available)[0]
    
    def search_current(self,g):
        following = [n for n in g.predecessors(self.index)]
        
        if len(following) != 0:
            return random.choices(following)[0]
        else:
            return "NOT FOUND";
        
    def moveA(self,g,current,candidate):
        #check if new following user is the same attribute
        if g.nodes[candidate]['User'].attribute == self.attribute:
            if g.nodes[current]['User'].attribute == self.attribute and random.uniform(0, 1) <0.5:
                return g;
            else:
                g.remove_edge(current,self.index)
                g.add_edge(candidate,self.index)
        else:
            if g.nodes[current]['User'].attribute != self.attribute and random.uniform(0, 1) <0.5:
                g.remove_edge(current,self.index)
                g.add_edge(candidate,self.index)
            else:
                return g;
        return g
    
    def moveD(self,g,current,candidate):
        #check if new following user is the different attribute
        if g.nodes[candidate]['User'].attribute != self.attribute:
            if g.nodes[current]['User'].attribute != self.attribute and random.uniform(0, 1) <0.5:
                return g;
            else:
                g.remove_edge(current,self.index)
                g.add_edge(candidate,self.index)
        else:
            if g.nodes[current]['User'].attribute == self.attribute and random.uniform(0, 1) <0.5:
                g.remove_edge(current,self.index)
                g.add_edge(candidate,self.index)
            else:
                return g;
        return g
    
    def moveAdd(self,g,candidate):
        #Add beta in-edge
        if self.beta > 0:
            g.add_edge(candidate,self.index)
#             print("Add: ",candidate,self.index)
            add = 1
        else:
            add = 0
        while add < self.beta:
            candidate = self.search_candidate(g)
            if candidate != 'NOT FOUND':
                g.add_edge(self.index,candidate)
                
            add += 1;
        return g
    
    def moveRemove(self,g,current):
        #remove a proportion of in-edge
        followers = [n for n in g.predecessors(self.index)]
        for n in followers:
            if random.uniform(0, 1) <= self.alpha:
                g.remove_edge(n,self.index)
            
        return g;
    