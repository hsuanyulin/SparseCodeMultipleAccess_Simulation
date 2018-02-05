import sys
sys.path.append('./encoderSCMA')
sys.path.append('./decoderSCMA')
import encoderSCMA as encoder
import encoderConfig
import decoderSCMA
import config
import numpy as np


encoder.randomInputGenerator();
encoder.bin2codewords(encoderConfig.userInput);

config.resourceLayer = encoderConfig.finalInput[0];
for i in range(5):
    decoderSCMA.iterativeMPA(1);
    decoderSCMA.estimateSymbol();
    difference = 0;
    for ele in np.absolute(config.EstimatedSymbols-encoderConfig.userSymbols):
        difference += ele;
    print(i,difference);
