import sys 


# Read Input
F, N = map(int, raw_input().split(" "))
training = []
for i in xrange(N):
    training.append(map(float, raw_input().split(" ")))

T = int(raw_input())
test = []
for i in xrange(T):
    test.append(map(float, raw_input().split(" ")))


# fit a polynomial regression which has an order less than 4

from sklearn.preprocessing import PolynomialFeatures
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline 

# Data 
training_data = np.array(training)
X_training = training_data[:, :-1]
y_training = training_data[:,-1]

model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                    ('linear', LinearRegression(fit_intercept=False))])

# fit to an order-3 polynomial data
model = model.fit(X_training, y_training)

result = model.predict(np.array(test))

for p in result:
    print p

