# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 02:56:02 2019

@author: Rodrigo Tamura

@description: Getting samples from external dataset using Systematic Sample Technique
"""

import pandas as pd
import numpy as np
from math import ceil

#Getting dataset from iris.csv
dataset = pd.read_csv("iris.csv")

population = len(dataset) #getting population of iris.csv
sample = ceil(population * 10 / 100) #Let's get 10% of samples from population

k = ceil(population / sample) # number of steps for getting samples sequence

starting = np.random.randint(low = 1, high = k + 1, size = 1) # getting the starting sample
'''
 starting vector going to receive one number (size = 1) randomly between 1 (low = 1)
and 10 (high = k + 1).

randint(): Returns random integers from low (inclusive) to high (exclusive).
'''

acumulator = starting[0]

samples = [] #Creating the vector for chosen samples

for i in range(sample):
    samples.append(acumulator)
    acumulator += k #getting next sample adding k
    
iris_samples = dataset.loc[samples] #using loc[] in order to locate the individuals from dataset