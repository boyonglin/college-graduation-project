import numpy as np
from sklearn import preprocessing
import python_speech_features as mfcc

def calculate_delta(array):
    """Calculate and returns the delta of given feature vector matrix"""

    rows,cols = array.shape
    deltas = np.zeros((rows,20))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i-j < 0:
                first = 0
            else:
                first = i-j
            if i+j > rows -1:
                second = rows -1
            else:
                second = i+j
            index.append((second,first))
            j+=1
        deltas[i] = ( array[index[0][0]]-array[index[0][1]] + (2 * (array[index[1][0]]-array[index[1][1]])) ) / 10
    return deltas

def extract_features(audio,rate):
    """extract 20 dim mfcc features from an audio, performs CMS and combines 
    delta to make it 40 dim feature vector"""    
    
    # audio is audio signal from which to compute features -> should be n*1 array
    # rate is samplerate of the signal we are working with
    # 0.025 is the length of the analysis window in seconds (default is 25ms)
    # 0.01 is the step between successive windows in seconds (default is 10ms)
    # 20 is number of cepstrum to return (default is 13)
    # append energy is true if zeroth cepstral coefficient is replaced with log of total frame energy
    # mfcc() returns a numpy array of size (NUMFRAMES by numcep) containing features, each row holds 1 feature vector 
    # further possible parameters & their defaults can be found at python-speech-features.readthedocs.io/en/latest/
    mfcc_feat = mfcc.mfcc(audio,rate, 0.025, 0.01,20,appendEnergy = True)
    
    # Scale all data onto one scale, eliminating sparsity & following same concept of Normalization & Standardization
    mfcc_feat = preprocessing.scale(mfcc_feat)
    delta = calculate_delta(mfcc_feat)
    combined = np.hstack((mfcc_feat,delta)) 
    return combined
#    
if __name__ == "__main__":
     print ("In main, Call extract_features(audio,signal_rate) as parameters")

