


import math
import config
import numpy as np

def printBasic():
    print("User Layer");
    print(config.userLayer);
    print("Factor Graph");
    print(config.factorGraph);
    print("Resource Layer");
    print(config.resourceLayer);


def init(Ev_f,probabilityX):
    Ev_f = Ev_f/config.numCodeWords;
    config.probabilityX = Ev_f;

def updateEf_v(k,j):
    eta_k = config.factorGraph[k];
    update = 0;
    for i,vNode in enumerate(eta_k):
        if i != j and vNode == 1:
            epsilon_i = config.factorGraph[:,i];
            for k_conditional, fNode in enumerate(epsilon_i):
                if fNode == 1 and k_conditional != k:
                    update += getMessage(config.factorGraph, k)*productSequencev_f(config.factorGraph, k_conditional,i);
    return update;

def updateEv_f(k,j):
    update = 0;
    update = config.probabilityX[j]*productSequencef_v(config.factorGraph,k,j);
    return update;

def productSequencev_f(factorGraph,k,j):
    eta_k = factorGraph[k];
    pi_Ev_f = 1;

    for i, vNode in enumerate(eta_k):
        if vNode == 1 and i != j:
            pi_Ev_f *= config.Ev_f[k,i];
    return pi_Ev_f;

def productSequencef_v(factorGraph,k,j):

    #print("Turn: "+str(k)+","+str(j));
    epsilon_j = factorGraph[:,j];
    #print(epsilon_j);

    pi_Ef_v = 1;
    for i, fNode in enumerate(epsilon_j):
        if fNode == 1 and i != k:
            #print("Ef_v["+str(i)+","+str(j)+"]="+str(config.Ef_v[i,j]));
            pi_Ef_v *= config.Ef_v[i,j];

    #print("Ef_v["+str(i)+","+str(j)+"]="+str(pi_Ef_v));
    return pi_Ef_v;

# Define function names()
def getMessage(factorGraph,k):
    eta_k = factorGraph[k];
    sigma_x = 0

    for i, variable_node in enumerate(eta_k):
        if variable_node == 1:
            sigma_x += variable_node

    return math.exp(-1/(config.sigma**2)*(config.resourceLayer[k]-sigma_x))

#Normalization
def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))
def add(u, v):
    return [ u[i]+v[i] for i in range(len(u)) ]
def sub(u, v):
    return [ u[i]-v[i] for i in range(len(u)) ]
def dot(u, v):
    return sum(u[i]*v[i] for i in range(len(u)))
def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]







xMax = 0;
#print(config.Ev_f);
#print(config.Ef_v);
#print(probabilityX);

for index in range(config.numCodeWords):
    for k in range(config.factorGraph.shape[0]):
        for j in range(0,config.factorGraph.shape[1]):
            config.Ef_v[k,j] = updateEf_v(k,j);

    #print(config.Ef_v);
    for j in range(config.factorGraph.shape[1]):
        for k in range(0,config.factorGraph.shape[0]):
            config.Ev_f[k,j] = productSequencef_v(config.factorGraph,k,j);
        config.Ev_f[:,j] = normalize(config.Ev_f[:,j]);
        config.Ev_f[:,j] *= config.probabilityX[j];
    #print(config.Ev_f);

temp_Ev_f = np.zeros(config.factorGraph.shape[1]);
for j in range(config.factorGraph.shape[1]):
    epsilon_j = config.factorGraph[:,j];
    pi_Ef_v = 1;
    for i, fNode in enumerate(epsilon_j):
        if fNode == 1:
            pi_Ef_v *= config.Ef_v[i,j];
    temp_Ev_f[j] = pi_Ef_v;
temp_Ev_f = 1 - temp_Ev_f;
xMax = np.argmax(temp_Ev_f);
#print(temp_Ev_f);
print("Input on Layer: "+ str(np.argmax(config.userLayer)));
print("argmax on Layer: "+ str(xMax));
