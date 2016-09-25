import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import linear_model


url = 'https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt'


data = pd.read_csv(url,
	names=['charge', 'use'])

# plt.scatter(data['charge'], data['use'])
# plt.xlabel('charge')
# plt.ylabel('use')
# plt.show()

subdata = data.loc[data['charge'] < 4]

x = np.array(subdata['charge']).reshape(-1, 1)
y = np.array(subdata['use'])

regr = linear_model.LinearRegression()

regr.fit(x, y)

xnew = float(raw_input())

if xnew < 4:
	predict = regr.predict(xnew)
else: 
	predict = 8.0

print "{:.2f}".format(predict[0])