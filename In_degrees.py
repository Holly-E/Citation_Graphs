#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:21:35 2018

@author: hollyerickson

Includes functions that compute information about the distribution of 
the in-degrees for nodes in graphs.
"""


# 3 Constants representing graphs
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 
             4: set([1]), 5: set([2]), 6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 
             5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    '''
    Parameter #nodes and returns a dictionary corresponding to 
    a complete directed graph with the specified number of nodes.
    It contains all possible edges, self-loops are not allowed. 
    The nodes of the graph should be numbered 0 to num_nodes - 1.
    '''
    
    if num_nodes <= 0:
        return {}
    
    new_dict = {}
    for num in range(num_nodes):
        neighbors = []
        for neighbor in range(num_nodes):
            if neighbor != num:
                neighbors.append(neighbor)
        new_dict[num] = set(neighbors)
    return new_dict
    
def compute_in_degrees(digraph):
    '''
    Takes a directed graph (represented as a dictionary) and 
    computes the in-degrees for the nodes in the graph. 
    It returns a dictionary with the same set of keys (nodes) as digraph 
    whose corresponding values are the number of edges whose head matches a particular node.
    '''
    new_dict = {}
    
    for key in digraph:
        new_dict[key] = 0
        
    for key, val in digraph.items():
        out_nodes = list(val)
        for node in out_nodes:
            new_dict[node] += 1
    
    return new_dict

def in_degree_distribution(digraph):
    '''
    Takes a directed graph and computes the unnormalized distribution 
    of the in-degrees of the graph. The function should return a dictionary 
    whose keys correspond to in-degrees of nodes in the graph. 
    The value associated with each in-degree is the number of nodes with that in-degree. 
    In-degrees with no corresponding nodes are not included.
    '''
    in_dict = compute_in_degrees(digraph)
    
    new_dict = {}
    for _dummy_key, val in in_dict.items():
        if val in new_dict:
            new_dict[val] += 1
        else:
            new_dict[val] = 1
    return new_dict

#a = make_complete_graph(4)
#print (in_degree_distribution(a))