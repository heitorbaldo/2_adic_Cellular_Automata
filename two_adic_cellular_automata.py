'''
2-adic Cellular Automata.
Be aware that since this first implementation only takes powers of -9 to 9 into account, 
it will only work properly for small numbers.
'''

import numpy as np
import matplotlib.pyplot as plt
from pyadic import PAdic, ModP

from functions import *

__all__ = [
    "run_addictive_2_adic_cellular_automata",
    "run_multiplicative_2_adic_cellular_automata",
]


def run_addictive_2_adic_cellular_automata(q, timesteps):
    '''Plots the 2-adic cellular automaton.
    Parameters
    ---------
    q: (rational number) a rational number.
    timesteps: (integer) number of time steps in the evolution.
    '''
    if isinstance(timesteps, int) == False:
        raise TypeError("n must be an integer.")
        
    CA = []
    for i in range(1, timesteps):
        two_adic = PAdic(q, 2, 7) #absolute precision: n=7.
        
        #update rule: add the 2-adic number to itself:
        b = power_series_to_binary(two_adic*i) 
        CA.append(b)
    
    plt.rcParams['image.cmap'] = 'binary'
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.matshow(CA)
    ax.axis(True);
    
    
def run_multiplicative_2_adic_cellular_automata(q, timesteps):
    '''Plots the 2-adic cellular automaton.
    Parameters
    ---------
    q: (rational number) a rational number.
    timesteps: (integer) number of time steps in the evolution.
    '''
    CA = []
    for i in range(1, timesteps):
        two_adic = PAdic(q, 2, 7) #absolute precision: n=7.
        
        #update rule: multiply the 2-adic number to itself:
        b = power_series_to_binary(two_adic**i)
        CA.append(b)
     
    plt.rcParams['image.cmap'] = 'binary'
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.matshow(CA)
    ax.axis(True);
    
    