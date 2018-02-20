
import config
import codebook64 as CODEBOOK
import math
import numpy as np
import itertools

eta_k = [];
epsilon_j = [];
combination = [];
class _DecoderHelper():

    def buildEta_k(self, factorGraph):
        global eta_k;
        eta_k = [];
        for k in range(factorGraph.shape[0]):
            temp = [];
            for i,vNode in enumerate(factorGraph[k]):
                if vNode == 1:
                    temp.append(i+1);
            eta_k.append(temp);
    def buildEpsilon_j(self, factorGraph):
        global epsilon_j;
        epsilon_j = [];
        for j in range(factorGraph.shape[1]):
            temp = [];
            for i,fNode in enumerate(factorGraph[:,j]):
                if fNode == 1:
                    temp.append(i+1);
            epsilon_j.append(temp);


    def getMessage(self, k, j, codewords):
        sigma_x = 0;
        for i, j_th in enumerate(eta_k[k]):
            #print("codewords",CODEBOOK.getCodeword(i+1, codewords[i])[k]);
            sigma_x += CODEBOOK.getCodeword(j_th, codewords[j_th-1])[k];
        dividend = config.resourceLayer[k]-sigma_x;
        return np.exp(-(dividend*dividend.conjugate())/(config.sigma**2))

    def productSequencev_f(self, k, j, codewords):
        pi_Ev_f = 1;
        for i, j_th in enumerate(eta_k[k]):
            if j_th != j:
                pi_Ev_f *= config.Ev_f[k, j_th-1, codewords[j_th-1].astype(int)];
        return pi_Ev_f;

    def getEf_v(self, k, j, cw):
        if eta_k[k].count(j) < 1:
            print("no j");
            return 0;
        update = 0;
        codewords = np.zeros(shape=(CODEBOOK.userNum(),1),dtype=np.integer);

        # initiate codewords
        codewords[j-1] = cw;
        global combination;
        for i, element in enumerate(combination):
            temp = list(element);
            for inner_i, j_th in enumerate(eta_k[k]):
                #print(j_th,j);
                if j_th != j:
                    codewords[j_th-1] = temp.pop();
            message = self.getMessage(k, j, codewords);
            product = self.productSequencev_f(k,j,codewords);
            update += message*product;

        #difference = np.absolute(codewords[index_A]-encoderConfig.userSymbols[index_A]);
        #difference += np.absolute(codewords[index_B]-encoderConfig.userSymbols[index_B]);
        #difference += np.absolute(codewords[j]-encoderConfig.userSymbols[j]);
        #if difference > 7 or difference < 2:

        #print("codewords-userSymbols",np.absolute(codewords[j]-encoderConfig.userSymbols[j]));
        #print("update",update);
        #print(encoderConfig.userSymbols[j],cw,np.abs(update))
        if update.any():
            return update[0];

    def getCodeword(k,j,codewords):
        eta_k = config.factorGraph[k];
        indexOfCW = 0;
        for i, vNode in enumerate(eta_k):
            if vNode == 1:
                if i == j:
                    return codewords[indexOfCW];
                indexOfCW += 1;
    def productSequencef_v(self,k,j,cw):
        epsilon_j = config.factorGraph[:,j];
        pi_Ef_v = 1;
        for i, fNode in enumerate(epsilon_j):
            if fNode == 1 and i != k:
                pi_Ef_v *= config.Ef_v[i,j,cw];
        return pi_Ef_v;
    def All_productSequencef_v(self,j,cw):
        epsilon_j = config.factorGraph[:,j];
        pi_Ef_v = 1;
        for i, fNode in enumerate(epsilon_j):
            if fNode == 1:
                pi_Ef_v *= config.Ef_v[i,j,cw];
        return pi_Ef_v;
    #Normalization

    def magnitude(self,v):
        return math.sqrt(sum(np.absolute(v[i])**2 for i in range(len(v))))

    def add(u, v):
        return [ u[i]+v[i] for i in range(len(u)) ]

    def sub(u, v):
        return [ u[i]-v[i] for i in range(len(u)) ]

    def dot(u, v):
        return sum(u[i]*v[i] for i in range(len(u)))

    def normalize(self,v):
        vmag = self.magnitude(v);
        return v/vmag;

    def getEv_f(self,k, j):
        if config.factorGraph[:,j][k] != 1:
            return 0;
        normalizedProduct = np.zeros( shape = (CODEBOOK.codeWordSize()),dtype=np.complex);
        cw = 0;
        for indexOfCW in range(CODEBOOK.codeWordSize()):
            normalizedProduct[indexOfCW] = self.productSequencef_v(k,j,cw);
            cw += 1;
        cw = 0;
        normalizedProduct = self.normalize(normalizedProduct);
        #print("********after normalization********")
        #print(k,j,cw,normalizedProduct);
        return normalizedProduct;

DECODERHELPER = _DecoderHelper();
def init():
    DECODERHELPER.buildEta_k(config.factorGraph);
    DECODERHELPER.buildEpsilon_j(config.factorGraph);
    global combination;
    combination = list(itertools.product(range(config.numCodeWords), repeat=len(eta_k[0])-1));


def messagePassing():
    # update message from Function Node to Variable Node
    #print("********Info from vNode to fNode********")

    for k in range(config.factorGraph.shape[0]):
        for j, j_th in enumerate(eta_k[k]):
            for index in range(config.numCodeWords):
                config.Ef_v[k,j_th-1,index] = DECODERHELPER.getEf_v(k,j_th,index);
                #print(k,j_th,index,config.Ef_v[k,j_th-1,index]);
    # update message from V Node to F Node
    #print("********Info from fNode to vNode********")
    for j in range(config.factorGraph.shape[1]):
        for k in range(config.factorGraph.shape[0]):
            config.Ev_f[k,j,:] = DECODERHELPER.getEv_f(k,j);
            #print("userSymbols",encoderConfig.userSymbols[j]);
            #print("final",k,j,config.Ev_f[k,j,:]);

def iterativeMPA(iteration):
    for i in range(iteration):
        messagePassing();
def estimateSymbol():
    for j in range(config.factorGraph.shape[1]):
        probX_j = np.zeros( shape = (CODEBOOK.codeWordSize()),dtype=np.complex);
        for indexOfCW in range(CODEBOOK.codeWordSize()):
            probX_j[indexOfCW] = DECODERHELPER.All_productSequencef_v(j,indexOfCW);
        config.EstimatedSymbols[j] = np.argmax(probX_j);
