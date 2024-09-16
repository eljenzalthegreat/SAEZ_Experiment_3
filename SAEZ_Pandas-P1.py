{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ddebe247-8e97-4cff-9a18-8ece64ffda4e",
   "metadata": {},
   "source": [
    "#### SAEZ, Eljenzal Hoper U. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3caaceac-c666-4cfd-93b8-6fe786ef8199",
   "metadata": {},
   "source": [
    "#### 2ECE - C"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6107b550-e18e-4020-8cd9-dd15fd9144ea",
   "metadata": {},
   "source": [
    "### Problem 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a6b40d5a-7c60-478f-a863-4f0599c2e722",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First five rows of the DataFrame:\n",
      "               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
      "0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
      "1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
      "2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
      "3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
      "4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   \n",
      "\n",
      "   carb  \n",
      "0     4  \n",
      "1     4  \n",
      "2     1  \n",
      "3     1  \n",
      "4     2  \n",
      "\n",
      "Last five rows of the DataFrame:\n",
      "             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
      "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
      "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
      "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
      "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
      "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
      "\n",
      "    carb  \n",
      "27     2  \n",
      "28     4  \n",
      "29     6  \n",
      "30     8  \n",
      "31     2  \n"
     ]
    }
   ],
   "source": [
    "# import the necessary library\n",
    "import pandas as pd\n",
    "\n",
    "# define the file path \n",
    "file = 'cars.csv'  # Replace with your file path\n",
    "\n",
    "# load the CSV file into a DataFrame \n",
    "cars = pd.read_csv(file_path)\n",
    "\n",
    "# display the first five rows of the DataFrame\n",
    "print(\"First five rows of the DataFrame:\")\n",
    "print(cars.head())\n",
    "\n",
    "# display the last five rows of the DataFrame\n",
    "print(\"\\nLast five rows of the DataFrame:\")\n",
    "print(cars.tail())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0cf622bc-ffb7-4ddf-95c2-1d2b91b8d268",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2b127a6-b73e-4cd6-9fed-5682945d1ec6",
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
