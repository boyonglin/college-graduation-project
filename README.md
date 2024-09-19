# System Design of Speaker Recognition Applied to Biometric Authentication and Computer Voice Control

---

Introduction: Speech is a rich source of information and a natural form of human interaction. Technologies like Speech-to-Text (STT) and Speaker Identification enhance security and control systems. Given the increasing prevalence of voice recognition systems, this study aims to assist specific disabled users in performing secure and user-friendly computer operations.

Research Methods:
Signal Preprocessing: Speech signals are non-stationary, challenging their mathematical modeling. This issue is addressed by framing the signal into 25ms frames to treat it as stationary and convolving these frames with a Hamming window to prevent spectral leakage.
Feature Extraction: The Mel-Frequency Cepstrum (MFC) is used to extract a 40-dimensional feature vector, simulating the human auditory system. This process involves transforming time-domain signals into the frequency domain, followed by using a mel-scale filter bank to capture auditory-relevant features.
Model Training: A Gaussian Mixture Model (GMM) is employed for voice recognition, with initial clustering achieved through K-means classification. The model parameters are refined using the Expectation Maximization (EM) algorithm to enhance the recognition accuracy.

Results and Discussion: The system's effectiveness increases with the number of audio files used for training, with five files found to be optimal. Utilizing more files may lead to parameter expansion and require additional data. Integration of Deep Neural Networks (DNN) could potentially improve recognition but would increase computational demand.

Usage flow:
1. Use `Login.py` to activate the Python GUI.
2. By characteristically capturing MFCCs for audio as input to the GMM, users create user profiles in real-time recording.
3. Access to the computer's voice control interface after voice matching of acoustic fingerprints.
4. Provides computer-specific operation for physically challenged people through speech-to-text conversion and instant recognition of the speaker.

![Flow](https://user-images.githubusercontent.com/56038738/226797803-65372cf7-f749-41cc-87fd-e48a7d8df247.jpg)

Credits:

	Clancy (Leader):
		GUI building  
		main code writing & testing  
		debugging & optimisation  
		posters & slides & demo video

	Yunwei:
		collecting & sorting data  
		partial code testing  
		assisting with posters & slides
