import numpy as np;
import matplotlib.pyplot as plt
import config
import itertools
import math


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Codebook2(object):

    @constant
    def USER1():
        return np.array([[1, 0, 0, -1], [0, 0, 0, 0], [0, -0.6351-0.4615j, 0.6351+0.4615j, 0], [0, 0, 0, 0]]);
    @constant
    def USER2():
        return np.array([[0, 0, 0, 0], [0, -0.6351-0.4615j, 0.6351+0.4615j, 0], [0, 0, 0, 0], [1, 0, 0, -1]]);
    @constant
    def USER3():
        return np.array([[-0.6351+0.4615j, 0, 0, 0.6351-0.4615j], [0, 0.4873-0.6156j, -0.4873-0.6156j, 0], [0, 0, 0, 0], [0, 0, 0, 0]]);
    @constant
    def USER4():
        return np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, -1], [0, -1j, 1j, 0]]);
    @constant
    def USER5():
        return np.array([[0, -1j, +1j, 0], [0, 0, 0, 0], [0, 0, 0, 0], [-0.6351+0.4615j, 0, 0, 0.6351-0.4615j]]);
    @constant
    def USER6():
        return np.array([[0, 0, 0, 0], [0.7851, 0, 0, -0.7851], [0, 0.4873-0.6156j, -0.4873+0.6156j, 0], [0, 0, 0, 0]]);

    def printConstellation(self):
        RGB = np.array([[0.1451, 0.0314, 0.3490],[0.0000, 0.2353, 1.0000],[0.0000, 0.6588, 0.8000],[0.2196, 1.0000, 0.7765],[0.4353, 0.9529, 0.7529],[0.6549, 0.9059, 0.7294]]);
        fig = plt.figure()

        for iResource in range(config.factorGraph.shape[0]):
            ax = fig.add_subplot(2,2,(iResource+1));
            eta = config.factorGraph[iResource];
            for i,vNode in enumerate(eta):
                if vNode == 1:
                    ax.scatter(_Codebook2.USERS[i+1].real[iResource], _Codebook2.USERS[i+1].imag[iResource], s=10, c=RGB[i], marker="s", label=('User '+str(i+1)))
            plt.legend(loc='upper left');
            plt.ylabel('Resource '+str(iResource+1));
        plt.show()
    def printY_k(self):
        fig = plt.figure()
        for iResource in range(config.factorGraph.shape[0]):
            ax = fig.add_subplot(2,2,(iResource+1));

            #create array of active users
            eta = config.factorGraph[iResource];
            activeUsers = [];
            for i,vNode in enumerate(eta):
                if vNode == 1:
                    activeUsers.append(i);
            activeUsersArr = np.array(activeUsers);
            activeUsersArr = activeUsersArr +1;
            print(activeUsers);
            #create all combination
            combination = list(itertools.product(_codebook2.USERS[activeUsersArr[0]],
                _codebook2.USERS[activeUsersArr[1]][iResource],
                _codebook2.USERS[activeUsersArr[2]][iResource]))
            print(np.array(combination).shape)
            y_k = np.array(np.sum(combination,axis=1).tolist());

            print(y_k.shape);
            ax.scatter(y_k.real[:,iResource], y_k.imag[:,iResource], s=1, c="b", marker="s")
            plt.ylabel('Resource '+str(iResource+1));
        plt.show()

    USERS = {1 : USER1.__get__(object),
               2 : USER2.__get__(object),
               3 : USER3.__get__(object),
               4 : USER4.__get__(object),
               5 : USER5.__get__(object),
               6 : USER6.__get__(object),
           }


_codebook2 = _Codebook2();
def printCodebooks():
    _Codebook2.printConstellation();

def getCodeword(userNum,symbol):
    codewords = _Codebook2.USERS[userNum];
    codeword = codewords[:,symbol]
    return codeword;

def codeWordSize():
    return _Codebook2.USERS[1].shape[1];

def codewordBits():
    return int(math.log(codeWordSize(), 2));

def userNum():
    return 6;
