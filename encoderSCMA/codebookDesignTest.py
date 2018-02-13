import numpy as np
#plot
import matplotlib.pyplot as plt
from math import e,pi
import itertools

def printY_k():
        fig = plt.figure()


        user1 = np.array([-1,1,0]);
        #ax = fig.add_subplot(2,2,1);
        #ax.scatter(user1.real[:], user1.imag[:], s=1, c="y", marker="s")
        #user2 = np.array([0.5+0.5j,0,-0.5-0.5j]);
        #user3 = np.array([1j,-1j,0]);
        #user4 = np.array([-0.5j,0.5j,1.5j]);

        #user4 = np.array([-1,1]);
        #create all combination
        #combination = list(itertools.product(user1,user2,user3,user4))
        user2 = user1*(2/3*(2**0.5)*(e**(45j/180*pi)))
        #ax = fig.add_subplot(2,2,2);
        #ax.scatter(user2.real[:], user2.imag[:], s=1, c="r", marker="s")
        user3 = user1*(e**(90j/180*pi))
        #ax = fig.add_subplot(2,2,3);
        #ax.scatter(user3.real[:], user3.imag[:], s=1, c="g", marker="s")
        user4 = user1*(1/3*(2**0.5)*(e**(135j/180*pi)))
        user5 = user2*(1/3*(2**0.5)*(e**(135j/180*pi)))
        user6 = user4*(1/3*(2**0.5)*(e**(135j/180*pi)))
        print(user1, user2, user3)
        combination = list(itertools.product(user1, user2, user3))
        #print(np.array(combination).shape)
        y_k = np.array(np.sum(combination,axis=1).tolist());
        ax = fig.add_subplot(1,1,1);
        ax.scatter(y_k.real[:], y_k.imag[:], s=1, c="b", marker="s")
        plt.ylabel('Resource k');
        y_k = np.round(y_k,4)
        y_kList = y_k.tolist();
        my_dict = {i:y_kList.count(i) for i in y_kList}
        print(np.array(my_dict));
        plt.show()

printY_k();
