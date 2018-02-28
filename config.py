import numpy as np
import math


sigma = 0.25;
numCodeWords = 4;
numUsers = 6;
numResources = 4;
numSymbols = 1000000;
numBits = int(math.log(numCodeWords,2));

userLayer = np.array([0,0,0,0,0,1]);
factorGraph = np.array([[1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0]]);
resourceLayer = np.dot(factorGraph, userLayer);

symbolShape = np.array([numUsers,numSymbols]);
codewordsShape = np.array([numUsers,numSymbols,numResources]);
EstimatedSymbols = np.empty(shape=symbolShape,dtype = np.integer)
EstimatedCodewords = np.empty(shape=codewordsShape,dtype=np.complex_)


shapeE = np.append(factorGraph.shape, numCodeWords);
shapeE = np.append(numSymbols, shapeE);
Ev_f = np.ones(shapeE,dtype=np.integer)/numCodeWords;
Ef_v = np.zeros(shapeE,dtype=np.complex);

combinations = None;
