import numpy as np
import codebook64 as CODEBOOK64
import config


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Input(object):
    @constant
    def symbolNum():
        return config.numSymbols;
    @constant
    def symbolSize():
        return config.numBits;
class _symHelper(object):
    @constant
    def SYM1():
        return np.array([1,0,0,0]);
    @constant
    def SYM2():
        return np.array([0,1,0,0]);
    @constant
    def SYM3():
        return np.array([0,0,1,0]);
    @constant
    def SYM4():
        return np.array([0,0,0,1]);

    USERS = {0 : SYM1.__get__(object),
             1 : SYM2.__get__(object),
             2 : SYM3.__get__(object),
             3 : SYM4.__get__(object),
             }

INPUT = _Input();

def symbolSize():
    return INPUT.symbolSize;
def symbolNum():
    return INPUT.symbolNum;



userInput = np.zeros( shape = (config.numUsers,INPUT.symbolNum,INPUT.symbolSize))
userSymbols = np.zeros( shape=(config.numUsers,INPUT.symbolNum),dtype = np.int8)
userCodewords = np.zeros( shape=(config.numUsers,INPUT.symbolNum,config.numResources),dtype=np.complex_)

finalInput = np.zeros( shape = (INPUT.symbolNum,config.numResources),dtype=np.complex_)
