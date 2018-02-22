import numpy as np


sigma = 0.25;
numCodeWords = 4;

userLayer = np.array([0,0,0,0,0,1]);
factorGraph = np.array([[1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0]]);
resourceLayer = np.dot(factorGraph, userLayer);
symbolShape = np.array([6,1]);
codewordsShape = np.array([6,1,4]);
EstimatedSymbols = np.empty(shape=symbolShape,dtype = np.integer)
EstimatedCodewords = np.empty(shape=codewordsShape,dtype=np.complex_)

shapeE = factorGraph.shape;
shapeE = np.append(shapeE, numCodeWords);
Ev_f = np.ones(shapeE,dtype=np.integer)/numCodeWords;
Ef_v = np.zeros(shapeE,dtype=np.complex);
shapeProb = np.array([factorGraph.shape[1],numCodeWords]);
probabilityX = np.ones(shapeProb)/numCodeWords;
