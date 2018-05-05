#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:18:27 2018

@author: hollyerickson

Create the DPA graph, calculate the in-degrees for each node and the x and y values.
"""
#import random
import In_degrees as ind
import alg_dpa_trial as alg

def dpa(num_nodes, num_edges):
    """
    Create graph where every new node added randomly connects to a set number of existing nodes.
    """
    """
    g = {}
    nodes = [num for num in range(num_nodes)]
    num_edges = prob *  num_nodes
    
    for num in range(num_nodes):
        #random.shuffle(nodes)
        edges = 0
        edge_list = []
        while edges < num_edges:
            edge = random.choice(nodes)
            if edge != num:
                edge_list.append(edge)
            edges += 1
        g[num] = set(edge_list)
        
    return g
    """
    
dpa_graph = dpa(27770, 12)
dpa_in_degrees = ind.in_degree_distribution(dpa_graph)

def normalize_in_degrees(num_nodes, dict):
    """
    Normalize in_degrees based off of 27770 nodes
    """
    y = [val / num_nodes for key, val in dict.items()]
    
    return y

y = normalize_in_degrees(27770, dpa_in_degrees)
x = [key for key in dpa_in_degrees.keys()]
