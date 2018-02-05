import numpy as np
import codebook64 as CODEBOOK64


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Input(object):
    @constant
    def inputSize():
        return 2;

INPUT = _Input();

def inputSize():
    return INPUT.inputSize;

userInput = np.zeros( shape = (CODEBOOK64.userNum(),INPUT.inputSize))
userSymbols = np.zeros( shape=(CODEBOOK64.userNum(),int(INPUT.inputSize/CODEBOOK64.codewordBits())),dtype = np.integer)
userCodewords = np.zeros( shape=(CODEBOOK64.userNum(),int(INPUT.inputSize/CODEBOOK64.codewordBits()),CODEBOOK64.codeWordSize() ),dtype=np.complex_)

finalInput = np.zeros( shape = (int(INPUT.inputSize/CODEBOOK64.codewordBits()),CODEBOOK64.codeWordSize() ),dtype=np.complex_)
