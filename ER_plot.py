#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:30:15 2018

@author: hollyerickson

Code for loading the loglog citation graph.
"""
import matplotlib.pyplot as plt

from ER_Graph import x
from ER_Graph import y

plt.style.use('seaborn-whitegrid')
fig = plt.figure(figsize = (9, 5))
ax1 = fig.add_subplot(1, 1, 1)

ax1.loglog(x, y, ls='None', marker='.', ms = 8, mec='black', mew=.5, c='red')

ax1.set_title('LogLog In-Degree Distribution for Citation Graph', weight=600)
ax1.set_xlabel('Number of Citations')
ax1.set_ylabel('Normalized Fraction of Nodes')

#plt.savefig('Images/In-Degree Distribution ER Graph', orientation='landscape')
plt.show()


