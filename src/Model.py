###This file provides generative model of network that we used in our analysis to produce four community structure types: Assortative, Disassotative, Core-Periphery and Source-Basin with two groups

import networkx as nx
import random
import numpy as np
import math
from User import *

def initialization(N,z,p0,p1,a = 1/2,seed = 1): 
    '''
        Initialize a directed random network 
        Parameters: N: the number of nodes
            z: average degree of node(include in and out degree)
            p0: probabilities of games for nodes in first group (P^S,P^A,P^R,alpha,1)
            p1: probabilities of games for nodes in second group (P^S,P^A,P^R,alpha,1)
            a: N_0/N
            seed: random seed
        Return: a directed random network
    '''
    p = z/(N-1)
    g = nx.fast_gnp_random_graph(n=N, p=p, seed=seed, directed=True)
    ps0 = p0[:3]
    alpha0 = p0[3]
    beta0 = p0[4]
    ps1 = p1[:3]
    alpha1 = p1[3]
    beta1 = p1[4]
    for n in g.nodes():
        if n < N*a:
            attribute = 0
        else:
            attribute = 1
        
        if attribute == 0:
            g.nodes[n]['User'] = User(n,attribute,ps0,alpha0,beta0)
        else:
            g.nodes[n]['User'] = User(n,attribute,ps1,alpha1,beta1)
        g.nodes[n]['attribute'] = attribute
    return g;

def dynamics(g,N):
    '''
        Perform the evolution process 
        Parameters: g: the initial network
            N: the number of evolution times 
        Return: the resulting network
    '''
    for i in range(N):
        n = np.random.choice(g.nodes())  
        g= g.nodes[n]['User'].activate(g)
    
    return g;



