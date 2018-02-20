import sys
sys.path.append('./encoderSCMA')
sys.path.append('./decoderSCMA')
sys.path.append('./encoderSCMA/codebooks')
import encoderSCMA as encoder
import encoderConfig
import decoderSCMA
import config
import numpy as np
import math
import matplotlib.pyplot as plt

codebooks = [1];
numRounds = 10;


def getA_noise(SNR, A_signal):
    return math.sqrt(A_signal/(10.**(SNR/10.)))
def getMagnitude(v):
    return math.sqrt(sum(np.absolute(v[i])**2 for i in range(len(v))))
def plotSER(SER):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1);
    ax.plot(SER[0], SER[1], ms=5, c="b", marker="o")
    plt.ylabel('SER');
    plt.xlabel('SNR(db)');
    plt.show()
def getDB(value):
    return 10*math.log(value,10);

SNRList = np.arange(1, 10, 1);
A_signal = 1.;
A_noise = 1.;

decoderSCMA.init();
for index, codebookIndex in enumerate(codebooks):
    print("********* CODEBOOK ",codebookIndex," ********");
    global SNR, A_signal, A_noise;
    SER = np.zeros(shape = (2,SNRList.shape[0]))
    for iSNR,SNR in enumerate(SNRList):
        difference = 0;
        SER[0][iSNR] = SNR;

        for i in range(numRounds):
            timeE = 0;
            encoder.setCodebook(codebookIndex);
            encoder.randomInputGenerator();
            encoder.bin2codewords(encoderConfig.userInput);
            #error
            awgn = (np.random.normal(0., config.sigma, config.resourceLayer.shape)+1j*np.random.normal(0., config.sigma, config.resourceLayer.shape));

            A_signal = getMagnitude(encoderConfig.finalInput[0]);
            A_noise = getA_noise(SNR, A_signal);
            awgn = awgn/getMagnitude(awgn)*A_noise;
            config.resourceLayer = awgn + encoderConfig.finalInput[0];


            decoderSCMA.iterativeMPA(10);
            decoderSCMA.estimateSymbol();
                #print(np.transpose(config.EstimatedSymbols));
                #print(np.transpose(encoderConfig.userSymbols));
            for ele in np.absolute(config.EstimatedSymbols-encoderConfig.userSymbols):
                if ele != 0:
                    timeE += 1;
            #if timeE != 0:
                #print("AWGN", getMagnitude(awgn));
                #print("Round",i,"Symbol_error",timeE);
            difference += timeE;

        SER[1][iSNR] = difference*1./numRounds/6.;
        print("Symbol_error",SER[1][iSNR]);
    plotSER(SER);
