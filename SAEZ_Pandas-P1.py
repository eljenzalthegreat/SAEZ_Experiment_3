#!/usr/bin/env python
# coding: utf-8

# ### Experiment 3 - Problem 1

# In[7]:


#PROBLEM 1: Save your file as Surname_Pandas-P1.py
#Using knowledge obtained from the experiment and demonstrations:

#a. Load the corresponding .csv file into a data frame named cars using pandas
#b. Display the first five and last five rows of the resulting cars.
import pandas as pd #import pandas library

cars = pd.read_csv("cars.csv") #load the .csv file into a data frame named cars using pandas
p1 = pd.concat([cars.head(), cars.tail()]) #display the first 5 rows and last 5 rows of cars.csv
p1

