#treinado com imagens azuis e vermelhas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

def ImgToArray(strImg):
    img = np.array(plt.imread(strImg))
    x = [];
    for i in range(1,len(img)): 
        for ii in img[i]:
            for iii in ii:
                x.append(iii)
    return x  

X = []
y = [] #0 para tons de azul e 1 para tons de vermelho

#azuis
