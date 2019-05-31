import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

#array misturando os vetores x e y
X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])
             
#labels                 
#y = [0,1,0,1,0,1]          


 
#plotting 
plt.scatter(x,y)
plt.show()

x = [1,2,3,6,9]
y = [1,4,9,36,81]
plt.scatter(x,y)
plt.show()