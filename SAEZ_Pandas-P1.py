#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import the necessary library
import pandas as pd

# define the file path 
file = 'cars.csv' 

# load the CSV file into a DataFrame 
cars = pd.read_csv(file)

# display the first five rows of the DataFrame
print("First five rows of the DataFrame:")
print(cars.head())

# display the last five rows of the DataFrame
print("\nLast five rows of the DataFrame:")
print(cars.tail())

