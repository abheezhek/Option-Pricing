# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 01:50:26 2019

@author: user
"""

import numpy as np

#Initialize the variables
S = 500
K=520
r=0.05
sigma=0.2
T=1
N=100
dt = T/N

#Cox-Ross-Rubinstein 
u = np.exp(sigma * np.sqrt(dt))
d = np.exp(-sigma * np.sqrt(dt))
p = (np.exp(r*dt) - d)/(u - d)

C = [[0 for i in range(N+1)] for j in range(N+1)]

#Number of nodes in respective time step i = i+1
# for ex Nth time step will have N+1 time steps
for j in range(N+1):
    C[N][j] = max( S*(u**j)*(d**(N-j)) - K, 0)
        
for i in range(N-1, -1, -1):
    for j in range(i+1):
        C[i][j] = np.exp(-r * dt)*( p*C[i+1][j+1] + (1-p)*C[i+1][j] )

print(C[0][0])