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


def dpa(num_nodes, num_new_nodes):
    """
    Create graph where every new node added randomly connects to a set number of existing nodes.
    """
    dpa_graph = ind.make_complete_graph(num_new_nodes)
    graph = alg.DPATrial(num_new_nodes)
    for num in range(num_new_nodes, num_nodes):
        new_node_neighbors = graph.run_trial(num_new_nodes)
        dpa_graph[num] = new_node_neighbors
    return dpa_graph

 
dpa_graph = dpa(27770, 13)
dpa_in_degrees = ind.in_degree_distribution(dpa_graph)

def normalize_in_degrees(num_nodes, dict):
    """
    Normalize in_degrees based off of 27770 nodes
    """
    y = [val / num_nodes for key, val in dict.items()]
    
    return y

y = normalize_in_degrees(27770, dpa_in_degrees)
x = [key for key in dpa_in_degrees.keys()]
