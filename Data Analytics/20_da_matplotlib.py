

#pip install matplotlib
import matplotlib
matplotlib.__version__

"""###Simple Plot - Line"""

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]
plt.plot(x,y)
plt.show()

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]
plt.plot(x,y)
plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.show()

"""### Double Plot - Line"""

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]
x2 = [1,2,3,4,5,6,7,8,9]
y2 = [2,4,7,9,5,3,8,10,2]

plt.plot(x,y,'r')
plt.plot(x2,y2,'g')

plt.plot(x,y,'ro')
plt.plot(x2,y2,'go')

plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.show()

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]
x2 = [1,2,3,4,5,6,7,8,9]
y2 = [2,4,7,9,5,3,8,10,2]

plt.plot(x,y,'r',label='Profit',linewidth=5)
plt.plot(x2,y2,'g',label='Tax')

plt.legend()
plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.show()

"""###Bar Graph"""

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]
x2 = [1,2,3,4,5,6,7,8,9]
y2 = [2,4,7,9,5,3,8,10,2]

plt.bar(x,y,color='b',label='Profit')
#plt.bar(x2,y2,color='g',label='Tax')

plt.legend()
plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.show()

"""###Histogram - Bar Graph"""

from matplotlib import pyplot as plt
age = [24,22,56,76,89,21,9,15,12,18,19,21,46,67,61,7,37,79,14]
range = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(age, range)
plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.grid()
plt.show()

"""###Scatter Plot

"""

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]

plt.scatter(x,y,color='r')

plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.show()

"""### Pie Chart"""

from matplotlib import pyplot as plt
x = [80,20,40,50,90,5]
y = ["Math","Physics","Programming","Communication","History","Sports"]
c = ['r','g','c','b','m','y','w','k']

plt.pie(x,labels=y,colors=c,autopct='%1.1f%%')

plt.title("Graph")
plt.show()

"""### Subplot"""

from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [10,2,3,6,4,9,7,4,2]
x2 = [1,2,3,4,5,6,7,8,9]
y2 = [2,4,7,9,5,3,8,10,2]

plt.subplot(2, 1, 1)
plt.title("Subplot 1")
plt.plot(x,y,'r')

plt.subplot(2, 1, 2)
plt.plot(x2,y2,'g')
plt.show()

"""# Project-1"""

import pandas as pd

dataset = pd.read_csv('dataset.csv')

X = dataset.iloc[:, :-1].values
X

Y = dataset.iloc[:, -1].values
Y

import matplotlib.pyplot as plt
plt.scatter(X,Y, color="red")
plt.title("Data Visualization")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

from sklearn.linear_model import LinearRegression
modelLR = LinearRegression()
modelLR.fit(X,Y)

import matplotlib.pyplot as plt
plt.scatter(X,Y, color="red")
plt.plot(X, modelLR.predict(X))
plt.title("Linear Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()
