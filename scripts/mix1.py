from scipy.io.wavfile import read
import numpy as np

noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/factory1.wav"
audio_file = "/home/carla/msattir/noise_mix/audio_samples/audio/sw2263A-ms98-a-trans-108.670875-110.07625.wav"

noise = np.array(read(noise_file)[1], dtype=float)
audio = np.array(read(audio_file)[1], dtype=float)

noise_smpl_rate = read(noise_file)[0]
audio_smpl_rate = read(audio_file)[0]



