import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('/Users/yiyingwang/desktop/UdacityMLNanoDegree/data/trainingdata.txt',
	names=['charge', 'use'])

plt.scatter(data['charge'], data['use'])
plt.show()
