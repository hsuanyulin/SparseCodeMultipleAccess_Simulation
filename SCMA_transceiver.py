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
#numRounds = np.zeros(9,dtype = np.integer);
#numRounds += 1000;
#for i, ele in enumerate(numRounds):
#    numRounds[i] = 100*10**(2**(i//3))


def getA_noise(SNR, A_signal):
    mag = np.zeros(shape=(A_signal.shape[0]));
    for i,ele in enumerate(A_signal):
        mag[i] = math.sqrt(ele/(10.**(SNR/10.)))
    return mag;
def getMagnitude(v):
    return np.sqrt(np.sum(np.square(np.absolute(v)),axis=1));
def plotSER(SER):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1);
    ax.plot(SER[0], SER[1], ms=5, c="b", marker="o")
    plt.ylabel('SER');
    plt.xlabel('SNR(db)');
    plt.show()
def getDB(value):
    return 10*math.log(value,10);

SNRList = np.arange(5, 10, 1);
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
        iterations = 0;


        timeE = 0;
        encoder.setCodebook(codebookIndex);
        encoder.randomInputGenerator();
        #print("finalInput shape", encoderConfig.finalInput.shape)

        #error
        awgn = (np.random.normal(0., config.sigma, encoderConfig.finalInput.shape)
                +1j*np.random.normal(0., config.sigma, encoderConfig.finalInput.shape));

        A_signal = getMagnitude(encoderConfig.finalInput);
        noiseAdjust = getA_noise(SNR, A_signal)/getMagnitude(awgn);

        awgn = awgn* noiseAdjust[:,None];


        config.resourceLayer = awgn + encoderConfig.finalInput;
        #print("resource layer")
        #print(config.resourceLayer)


        iterations += decoderSCMA.iterativeMPA(10);
        decoderSCMA.estimateSymbol();

        timeE = np.count_nonzero(config.EstimatedSymbols-encoderConfig.userSymbols);
        difference += timeE;

        SER[1][iSNR] = difference*1./config.numSymbols/6.;
        print("SNR",SER[0][iSNR]);
        print("Total_rounds",config.numSymbols);
        print("Symbol_error",SER[1][iSNR]);
        print("iterations",iterations);
    plotSER(SER);
