#!/usr/bin/env python
# coding: utf-8

# #### SAEZ, Eljenzal Hoper U. 

# #### 2ECE - C

# ### Problem 2

# In[15]:


import pandas as pd

# load the CSV file into a DataFrame 
file_path = 'cars.csv'  # Replace with your actual file path
cars = pd.read_csv(file_path)

# a. display the first five rows with odd-numbered columns
odd_columns = cars.iloc[:, 1::2]
print("First five rows with odd-numbered columns:")
print(odd_columns.head())

# b. display the row that contains the ‘Model’ of ‘Mazda RX4’
mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']
print("\nRow with the model 'Mazda RX4':")
print(mazda_rx4_row)

# c. how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
camaro_z28_cylinders = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"\nNumber of cylinders for 'Camaro Z28': {camaro_z28_cylinders}")

# d. determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’ have
models_of_interest = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
info_models = cars[cars['Model'].isin(models_of_interest)][['Model', 'cyl', 'gear']]
print("\nCylinders and gear types for selected models:")
print(info_models)


# In[ ]:




