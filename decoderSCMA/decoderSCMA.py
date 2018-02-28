
import config
import codebook64 as CODEBOOK
import math
import numpy as np
import itertools
import copy

eta = [];
epsilon = [];

class _DecoderHelper():

    def getCombination(self, k, j):
        listUsers = []
        for i, user in enumerate(eta[k]):
            if user != j:
                listUsers.append(CODEBOOK.getCodewords(user)[k]);
        return list(itertools.product(*listUsers));

    def buildEta(self, factorGraph):
        global eta;
        eta = [];
        for k in range(factorGraph.shape[0]):
            temp = [];
            for i,vNode in enumerate(factorGraph[k]):
                if vNode == 1:
                    temp.append(i+1);
            eta.append(temp);
    def buildEpsilon(self, factorGraph):
        global epsilon;
        epsilon = [];
        for j in range(factorGraph.shape[1]):
            temp = [];
            for i,fNode in enumerate(factorGraph[:,j]):
                if fNode == 1:
                    temp.append(i+1);
            epsilon.append(temp);

    def getMessage(self, k, j, cw):

        combination = np.sum(self.getCombination(k,j),axis=1)+CODEBOOK.getCodeword(j, cw)[k];
        resourceK = np.reshape(config.resourceLayer[:,k], (config.resourceLayer[:,k].shape[0],1))
        resourceK = np.repeat(resourceK, 16, axis=1);

        dividend = resourceK-combination;

        return np.exp(-(dividend*dividend.conjugate())/(config.sigma**2))

    def productSequencev_f(self, k, j, cw):
        usersProb = [];
        for i, user in enumerate(eta[k]):
            if user != j:
                usersProb.append(config.Ev_f[:,k, user-1].transpose());
        usersProb = np.asarray(usersProb);
        #print("itertools userProb", usersProb.shape)
        #usersProb = usersProb.transpose();
        #print("itertools userProb", usersProb.shape)
        #print(np.asarray(list(itertools.product(*usersProb))).shape)
        return np.prod(list(itertools.product(*usersProb)),axis=1).transpose()

    def getEf_v(self, k, j, cw):
        return np.sum(self.getMessage(k, j, cw)*self.productSequencev_f(k,j,cw),axis=1);


    def productSequencef_v(self,k,j):
        resourcesProb = np.ones(shape=(config.numSymbols,config.numCodeWords),dtype = np.float)
        for i, resource in enumerate(epsilon[j]):
            if resource != k:
                resourcesProb = resourcesProb*config.Ef_v[:,resource-1,j]
        return resourcesProb

    def All_productSequencef_v(self,j):
        resourcesProb = np.ones(shape=(config.numSymbols,config.numCodeWords))
        for i, resource in enumerate(epsilon[j]):
                resourcesProb = resourcesProb*config.Ef_v[:,resource-1,j]
        return resourcesProb

    def magnitude(self,v):
        return np.sqrt(np.sum(np.square(np.absolute(v)),axis=1));

    def add(u, v):
        return [ u[i]+v[i] for i in range(len(u)) ]

    def sub(u, v):
        return [ u[i]-v[i] for i in range(len(u)) ]

    def dot(u, v):
        return sum(u[i]*v[i] for i in range(len(u)))

    def normalize(self,v):
        vmag = np.sum(np.absolute(v),axis=1);
        v = v / vmag[:,None];
        return v;

    def getEv_f(self,k, j):
        normalizedProduct = self.normalize(self.productSequencef_v(k,j));
        #print("********after normalization********")
        #print(normalizedProduct,k,j)
        return normalizedProduct;

DECODERHELPER = _DecoderHelper();
def init():
    DECODERHELPER.buildEta(config.factorGraph);
    DECODERHELPER.buildEpsilon(config.factorGraph);

def messagePassing():
    # update message from Function Node to Variable Node
    for k in range(config.factorGraph.shape[0]):
        for j, j_th in enumerate(eta[k]):
            for index in range(config.numCodeWords):
                config.Ef_v[:,k,j_th-1,index] = DECODERHELPER.getEf_v(k,j_th,index);

    # update message from V Node to F Node
    for j in range(config.factorGraph.shape[1]):
        for k, k_th in enumerate(epsilon[j]):
            config.Ev_f[:,k_th-1,j,:] = DECODERHELPER.getEv_f(k_th,j);


def iterativeMPA(iteration):
    iterationThreshold = 0;
    temp = [];
    iterationEnd = 0;
    for i in range(iteration):
        temp = copy.copy( config.EstimatedSymbols);
        iterationEnd = copy.copy(i)
        #print("estimateSymbol",config.EstimatedSymbols)
        if iterationThreshold > 2:
            break;
        messagePassing();
        estimateSymbol();
        if np.allclose(temp, config.EstimatedSymbols):
            iterationThreshold += 1;
    #print("iteration end", iterationEnd)
    return iterationEnd;

def estimateSymbol():
    for j in range(config.factorGraph.shape[1]):
        config.EstimatedSymbols[j] = np.argmax(DECODERHELPER.All_productSequencef_v(j),axis=1);
