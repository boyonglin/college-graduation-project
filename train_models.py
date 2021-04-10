import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")

def train_models():
    #path to training data
    source   = "C:\\Users\\USER\\GUI_SpeakerID\\development_set\\"   

    #path where training speakers will be saved
    dest = "C:\\Users\\USER\\GUI_SpeakerID\\speaker_models\\"

    train_file = "voice_list_enroll.txt"        

    file_paths = open(train_file,'rb')

    count = 1

    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())
    for path in file_paths:    
        path = path.strip()
        print (path)

        # read the audio
        rate,audio = read(source + path.decode('utf-8'))

        # extract 40 dimensional MFCC & delta MFCC features
        vector = extract_features(audio,rate)

        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))
        # when features of 5 files of speaker are concatenated, then do model training
        if count == 5:
            gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 3)
            gmm.fit(features)

            # dumping the trained gaussian model
            picklefile = path.decode().split("_")[0]+".gmm"
            pickle.dump(gmm,open(dest + picklefile,'wb+'))
            print ('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)
            features = np.asarray(())
            count = 0
        else:
            count = count + 1