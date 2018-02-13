import numpy as np
import codebook64 as CODEBOOK1
import codebook3 as CODEBOOK3
import codebook2 as CODEBOOK2
import encoderConfig


CODEBOOK = CODEBOOK1;

def setCodebook(num):
    global CODEBOOK
    if num == 1:
        CODEBOOK = CODEBOOK1;
    elif num == 2:
        CODEBOOK = CODEBOOK2;
    elif num == 3:
        CODEBOOK = CODEBOOK3;


def bin2dec(binary):
    binString = str(binary);
    return int(binString, 2);

def randomInputGenerator():
    #print(encoderConfig.userInput);
    for i in range(CODEBOOK.userNum()):
        encoderConfig.userInput[i] = np.random.randint(2, size=encoderConfig.inputSize());
    #print("users' input",encoderConfig.userInput);

def array2int(array):
    final = 0;
    for i in range(len(array)):
        final +=  array[i]*(10**(len(array)-1-i))
    return final;

def bin2codewords(userBinaries):
    encoderConfig.finalInput = np.zeros( shape= encoderConfig.finalInput.shape, dtype = np.complex_);
    for i in range(userBinaries.shape[0]):
        userBin = userBinaries[i];
        seq = 0;
        while int(len(userBin)/CODEBOOK.codewordBits()) > 0:
            subbin = userBin[:CODEBOOK.codewordBits()];
            subint = bin2dec(int(array2int(subbin)));

            encoderConfig.userSymbols[i][seq] = subint;
            encoderConfig.userCodewords[i][seq] = CODEBOOK.getCodeword(i+1,subint);
            encoderConfig.finalInput[seq] += encoderConfig.userCodewords[i][seq];
            #print(encoderConfig.userCodewords[i][seq]);
            #trim the used one
            userBin = userBin[CODEBOOK.codewordBits():];
            seq += 1;
    #print("users' symbol",encoderConfig.userSymbols);
    #print("users' final input",encoderConfig.finalInput);



#print(bin2dec(1111));
#print(CODEBOOK.getCodewords(1));
#print(CODEBOOK.codeWordSize());
