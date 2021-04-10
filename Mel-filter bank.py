import numpy.matlib
import matplotlib.pyplot as plt
import librosa.display

mel = librosa.filters.mel(sr=22050, n_fft=1024, n_mels=26, fmin=0, fmax=22050/2, norm=None)

plt.figure(figsize=(6, 4))
librosa.display.specshow(mel, x_axis='linear')
plt.xlabel('freqency')
plt.ylabel('Mel-filter')
plt.title('Mel-filter bank')
plt.colorbar()
plt.tight_layout()
plt.show()

plt.xlabel('freqency')
plt.ylabel('Mel-filter')
plt.title('Mel-filter bank')
plt.plot(mel.T)
plt.show()
