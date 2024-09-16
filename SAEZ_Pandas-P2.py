{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e3ab751f-05de-4b86-8037-0629195d7d91",
   "metadata": {},
   "source": [
    "#### SAEZ, Eljenzal Hoper U. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36b0fca0-4837-461f-b086-852499ab9942",
   "metadata": {},
   "source": [
    "#### 2ECE - C"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "263213ac-c107-4ff7-901c-9eea75f10b66",
   "metadata": {},
   "source": [
    "### Problem 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b882f09b-84be-4f73-a0db-ef0c7cba7d8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First five rows with odd-numbered columns:\n",
      "    mpg   disp  drat   qsec  am  carb\n",
      "0  21.0  160.0  3.90  16.46   1     4\n",
      "1  21.0  160.0  3.90  17.02   1     4\n",
      "2  22.8  108.0  3.85  18.61   1     1\n",
      "3  21.4  258.0  3.08  19.44   0     1\n",
      "4  18.7  360.0  3.15  17.02   0     2\n",
      "\n",
      "Row with the model 'Mazda RX4':\n",
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n",
      "\n",
      "Number of cylinders for 'Camaro Z28': 8\n",
      "\n",
      "Cylinders and gear types for selected models:\n",
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# load the CSV file into a DataFrame \n",
    "file_path = 'cars.csv'  # Replace with your actual file path\n",
    "cars = pd.read_csv(file_path)\n",
    "\n",
    "# a. display the first five rows with odd-numbered columns\n",
    "odd_columns = cars.iloc[:, 1::2]\n",
    "print(\"First five rows with odd-numbered columns:\")\n",
    "print(odd_columns.head())\n",
    "\n",
    "# b. display the row that contains the ‘Model’ of ‘Mazda RX4’\n",
    "mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']\n",
    "print(\"\\nRow with the model 'Mazda RX4':\")\n",
    "print(mazda_rx4_row)\n",
    "\n",
    "# c. how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?\n",
    "camaro_z28_cylinders = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]\n",
    "print(f\"\\nNumber of cylinders for 'Camaro Z28': {camaro_z28_cylinders}\")\n",
    "\n",
    "# d. determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’ have\n",
    "models_of_interest = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']\n",
    "info_models = cars[cars['Model'].isin(models_of_interest)][['Model', 'cyl', 'gear']]\n",
    "print(\"\\nCylinders and gear types for selected models:\")\n",
    "print(info_models)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b4b71d7-d57f-488d-bdf6-45919147aac4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
