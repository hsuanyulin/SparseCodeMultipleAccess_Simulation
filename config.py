import numpy as np

sigma = 1;
numCodeWords = 2;

userLayer = np.array([0,0,0,0,0,1]);
factorGraph = np.array([[1, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 1]]);
resourceLayer = np.dot(factorGraph, userLayer);

Ev_f = np.ones(factorGraph.shape)/numCodeWords;
Ef_v = np.zeros(factorGraph.shape);
probabilityX = np.ones(factorGraph.shape[1])/numCodeWords;
