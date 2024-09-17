# ECE2112 - Experiment 3
## Introduction to Data Analysis with Pandas

### Overview
This repository contains the code for Experiment 3 of the ECE2112 course, focusing on data analysis using the pandas library in Python. The scripts demonstrate how to load data from a CSV file and perform various data extraction and analysis tasks.

#### I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

#### II. Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter
notebook in the dedicated submission bin.

### Problem 1: Load and Display Data
#### Objective: Load a CSV file into a pandas DataFrame and display the first and last five rows.

#### Step-by-step Code Explanation
1. Import the pandas library.
2. Define the file path for the CSV file.
3. Load the CSV file into a DataFrame named cars.
4. Display the first five rows of the DataFrame.
5. Display the last five rows of the DataFrame.

### Problem 2: Data Extraction and Analysis
Objective: Perform data extraction and analysis using subsetting, slicing, and indexing operations on the cars DataFrame.

#### Step-by-step Code Explanation

1. Display the first five rows with odd-numbered columns:
- Select columns with odd indices and display the first five rows.

2. Display the row that contains the ‘Model’ of ‘Mazda RX4’:
- Filter the DataFrame to show the row where the 'Model' is 'Mazda RX4'.

3. Determine the number of cylinders for the car model ‘Camaro Z28’:
- Find the number of cylinders for 'Camaro Z28'.

4. Determine the number of cylinders and gear type for specific car models:
- Extract the number of cylinders and gear type for ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’.

### Note:
Ensure that cars.csv is located in the same directory as the scripts, or update the file_path variable to the correct location.

### Files
cars.csv: CSV file containing car data.

Problem_1.py: Script for loading and displaying data.

Problem_2.py: Script for data extraction and analysis.

### Contact
For any questions or feedback, please contact hopersaez@gmail.com

### Acknowledgements
Special thanks to the instructors and resources of the ECE2112 course for providing the foundational concepts.
