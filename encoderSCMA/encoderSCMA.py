import numpy as np
import codebook64 as CODEBOOK
import encoderConfig





def bin2dec(binary):
    binString = str(binary);
    return int(binString, 2);

def randomInputGenerator():
    #print(encoderConfig.userInput);
    for i in range(CODEBOOK.userNum()):
        encoderConfig.userInput[i] = np.random.randint(2, size=encoderConfig.inputSize());
    #print(encoderConfig.userInput);

def array2int(array):
    final = 0;
    for i in range(len(array)):
        final +=  array[i]*(10**(len(array)-1-i))
    return final;

def bin2codewords(userBinaries):
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
        #print(encoderConfig.userSymbols[i]);
    #print(encoderConfig.finalInput);



#print(bin2dec(1111));
#print(CODEBOOK.getCodewords(1));
#print(CODEBOOK.codeWordSize());
