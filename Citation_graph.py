#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:30:15 2018

@author: hollyerickson

Code for loading the loglog citation graph.
"""
import matplotlib.pyplot as plt

from Citation_data import x
from Citation_data import y

plt.style.use('seaborn-whitegrid')
plt.figure(figsize = (9, 5))
plt.loglog(x, y, ls='None', marker='.', ms = 8, mec='black', mew=.5, c='blue')
plt.show()


