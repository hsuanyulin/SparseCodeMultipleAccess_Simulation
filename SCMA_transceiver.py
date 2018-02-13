import sys
sys.path.append('./encoderSCMA')
sys.path.append('./decoderSCMA')
import encoderSCMA as encoder
import encoderConfig
import decoderSCMA
import config
import numpy as np





for codebookIndex in range(1,3):
    difference = 0;
    print("********* CODEBOOK ",codebookIndex," ********");
    for i in range(5):
        encoder.setCodebook(codebookIndex);
        encoder.randomInputGenerator();
        encoder.bin2codewords(encoderConfig.userInput);

        config.resourceLayer = (np.random.normal(0., config.sigma, config.resourceLayer.shape)+1j*np.random.normal(0., config.sigma, config.resourceLayer.shape))/2.**0.5 + encoderConfig.finalInput[0];
        #print("AWGN", config.resourceLayer-encoderConfig.finalInput);

        decoderSCMA.iterativeMPA(10);
        decoderSCMA.estimateSymbol();
            #print(np.transpose(config.EstimatedSymbols));
            #print(np.transpose(encoderConfig.userSymbols));
        for ele in np.absolute(config.EstimatedSymbols-encoderConfig.userSymbols):
            if ele != 0:
                difference += 1;
    print("Symbol_error",difference);
