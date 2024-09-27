###This file provides some simplied functions to analyze two groups network
import networkx as nx
import random
import numpy as np
import math
from collections import Counter
from summary_stats import pairwise_interaction_type,three_ineraction_type

def get_density(g,community):
    '''
        Compute the exact density matrix
        Parameters: g: network
            community: dict with node as keys and corresponding community as values
        Return: 2x2 density matrix
    '''
    
    B = 2 #two communities
    m = np.zeros((B,B))
    count_par = Counter([v for v in community.values()])
    
    for e in g.edges():
        s,t = e
        par_s = community[s]
        par_t = community[t]
        if par_s != par_t:
            m[int(par_s)][int(par_t)] += 1/count_par[par_s]/count_par[par_t]
        else:
            m[int(par_s)][int(par_t)] += 1/count_par[par_s]/(count_par[par_t]-1)
        
    return m;

def get_structure(den):
    '''
        Classify community structure type given a density matrix
        Parameters: den: 2x2 density matrix
        Return: Community structure type
    '''
    typ = pairwise_interaction_type(den[0][0],den[1][1],den[0][1],den[1][0],directed = True)
    ttyp = three_ineraction_type(typ)
    if ttyp == 'Assortative':
        return 'A';
    elif ttyp == 'Disassortative':
        return 'D';
    elif ttyp == 'Core-Periphery':
        return 'CP';
    else:
        return 'SB';
    
#def get_degree_sep(g,community):
#    '''
#        Compute the average number of in and out edges for four cases:
#            1. from group 0 to group 0
#            2. from group 1 to group 0
#            3. from group 0 to group 1
#            4. from group 1 to group 1
#        Parameters: network
#            community: dict with node as keys and corresponding community as values
#        Return: 2 dict
#    '''
#    B = 2 #two communities
#    in_degree,out_degree={"0-0":[],"0-1":[],"1-0":[],"1-1":[]},{"0-0":[],"0-1":[],"1-0":[],"1-1":[]}
#    
#    N0 = [v for v in community.values()].count('0')
#    N1 = [v for v in community.values()].count('1')
#    
#    for n in g.nodes():
#        pre = [community[m] for m in g.predecessors(n)] #(m,n)
#        suc = [community[m] for m in g.successors(n)] #(n,m)
#        
#        
#        in_degree['0-'+community[n]].append(pre.count('0'))
#        in_degree['1-'+community[n]].append(pre.count('1'))
#        out_degree[community[n]+'-0'].append(suc.count('0'))
#        out_degree[community[n]+'-1'].append(suc.count('1'))
#    
#    in_degree['0-0'] = np.sum(in_degree['0-0'])/N0
#    in_degree['1-0'] = np.sum(in_degree['1-0'])/N0
#    in_degree['0-1'] = np.sum(in_degree['0-1'])/N1
#    in_degree['1-1'] = np.sum(in_degree['1-1'])/N1
#    
#    out_degree['0-0'] = np.sum(out_degree['0-0'])/N0
#    out_degree['1-0'] = np.sum(out_degree['1-0'])/N1
#    out_degree['0-1'] = np.sum(out_degree['0-1'])/N0
#    out_degree['1-1'] = np.sum(out_degree['1-1'])/N1
#    
#        
#    return in_degree,out_degree;

#def get_density_sep(g,community):
#    '''
#        Compute the exact density matrix
#        Parameters: g: network
#            community: dict with node as keys and corresponding community as values
#        Return: 2x2 density matrix
#    '''
#    B = 2 #two communities
#    
#    in_degree={"0-0":[],"0-1":[],"1-0":[],"1-1":[]}
#    
#    for n in g.nodes():
#        pre = [community[m] for m in g.predecessors(n)] #(m,n)
#       
#        in_degree['0-'+community[n]].append(pre.count('0'))
#        in_degree['1-'+community[n]].append(pre.count('1'))
#    
#    den = np.zeros((B,B))
#    N0 = [v for v in community.values()].count('0')
#    N1 = [v for v in community.values()].count('1')
#    den[0][0] = sum(in_degree["0-0"])/N0/(N0-1)
#    den[0][1] = sum(in_degree["0-1"])/N0/N1
#    den[1][0] = sum(in_degree["1-0"])/N0/N1
#    den[1][1] = sum(in_degree["1-1"])/N1/(N1-1)
#    
#    return den;
