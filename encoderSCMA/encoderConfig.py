import numpy as np
import codebook64 as CODEBOOK


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Input(object):
    @constant
    def inputSize():
        return 8;

INPUT = _Input();

def inputSize():
    return INPUT.inputSize;

userInput = np.zeros( shape = (CODEBOOK.userNum(),INPUT.inputSize))
userCodewords = np.zeros( shape=(CODEBOOK.userNum(),int(INPUT.inputSize/CODEBOOK.codewordBits()),CODEBOOK.codeWordSize() ),dtype=np.complex_)
finalInput = np.zeros( shape = (int(INPUT.inputSize/CODEBOOK.codewordBits()),CODEBOOK.codeWordSize() ),dtype=np.complex_)
