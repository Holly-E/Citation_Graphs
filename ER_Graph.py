#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:18:27 2018

@author: hollyerickson

Graph where for every ordered pair of distinct nodes (i,j), the modified algorithm adds the directed edge from i to j with probability p
"""
import random
import In_degrees as ind

def er(num_nodes, prob):
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
    
er_graph = er(5000, 0.05)
er_in_degrees = ind.in_degree_distribution(er_graph)

def normalize_in_degrees(num_nodes, dict):
    """
    Normalize in_degrees based off of 27770 nodes
    """
    y = [val / num_nodes for key, val in dict.items()]
    
    return y

y = normalize_in_degrees(5000, er_in_degrees)
x = [key for key in er_in_degrees.keys()]
