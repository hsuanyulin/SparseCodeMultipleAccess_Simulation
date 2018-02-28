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

def randomInputGenerator():
    #print(encoderConfig.userInput);

    binaryM = np.ones(shape=(encoderConfig.symbolSize()), dtype = np.int8);
    for i, ele in enumerate(binaryM):
        binaryM[i] = 2**(encoderConfig.symbolSize()-1-i);
    #print("binaryM", binaryM);

    encoderConfig.userInput = np.random.randint(2, size=encoderConfig.userInput.shape);
    #print("users' input",encoderConfig.userInput);
    encoderConfig.userSymbols = np.dot(encoderConfig.userInput,binaryM);
    #print("users' symbols",encoderConfig.userSymbols);

    for i in range(CODEBOOK.userNum()):
        for j, ele in enumerate(encoderConfig.userSymbols[i]):
            encoderConfig.userCodewords[i,j] = CODEBOOK.getCodeword(i+1, ele);
        #print("users' cw",encoderConfig.userCodewords[i]);
    encoderConfig.finalInput = np.sum(encoderConfig.userCodewords, axis = 0);
    #print(encoderConfig.userSymbols)

#print(bin2dec(1111));
#print(CODEBOOK.getCodewords(1));
#print(CODEBOOK.codeWordSize());
