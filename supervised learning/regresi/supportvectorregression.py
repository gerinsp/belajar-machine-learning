# -*- coding: utf-8 -*-
"""SupportVectorRegression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WH6K3Xu2_y7V8lRWLDLorWLus4iku5bC
"""

import pandas as pd

data = pd.read_csv('Salary_Data.csv')

data.info()

import numpy as np

# memisahkan atribut dan label
X = data['YearsExperience']
y = data['Salary']

# mengubah bentuk atribut
X = np.array(X)
X = X[:,np.newaxis]

from sklearn.svm import SVR

# membangun model dengan parameter C, gamma, dan kernel
model = SVR(C=1000, gamma=0.05, kernel='rbf')

# melatih model dengan fungsi fit
model.fit(X,y)

import matplotlib.pyplot as plt

# memvisualisasikan model
plt.scatter(X, y)
plt.plot(X, model.predict(X))