import numpy as np
#plot
import matplotlib.pyplot as plt
from math import e,pi
import itertools

def printY_k():
        fig = plt.figure()

        ax = fig.add_subplot(1,1,1);
        user1 = np.array([-1+1j,0,1-1j]);
        user2 = np.array([-1j,0,1j]);
        user3 = np.array([1+1j,0,-1-1j]);
        user4 = np.array([-1,0,1]);
        #create all combination
        #combination = list(itertools.product(user1,user2,user3,user4))
        user2 = user4*(e**(60j/180*pi))
        user3 = user4*(e**(120j/180*pi))
        #user1 = np.round(user4*(e**(135j/180*pi)))
        print(user2,user3,user4)
        combination = list(itertools.product(user2, user3, user4))
        print(np.array(combination).shape)
        y_k = np.array(np.sum(combination,axis=1).tolist());

        ax.scatter(y_k.real[:], y_k.imag[:], s=1, c="b", marker="s")
        plt.ylabel('Resource k');
        y_k = np.round(y_k)
        y_kList = y_k.tolist();
        my_dict = {i:y_kList.count(i) for i in y_kList}
        print(np.array(my_dict));
        plt.show()

printY_k();
