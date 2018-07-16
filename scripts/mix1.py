from __future__ import division
from scipy.io.wavfile import read, write
import numpy as np
import math

def renormalize(n, range_in, range_out):
    delta_in = range_in[1] - range_in[0]
    delta_out = range_out[1] - range_out[0]
    frac1 = ((n - range_in[0])/(delta_in))
    out = (frac1*delta_out) + range_out[0] 
    return (out)

noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/factory1.wav"
noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/babble.wav"
noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/factory1_16.wav"
audio_file = "/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2.wav"
audio_file = "/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2_16.wav"

noise = np.array(read(noise_file)[1], dtype=np.int16)
audio = np.array(read(audio_file)[1], dtype=np.int16)

noise_smpl_rate = read(noise_file)[0]
audio_smpl_rate = read(audio_file)[0]

#Mix wav files with same sample rates
assert noise_smpl_rate == audio_smpl_rate

noise_mid = int(len(noise)/2)
audio_mid = int(len(audio)/2)

audio2 = np.asarray(audio, dtype=np.int16)
#print (len(audio), len(noise))
#write("/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2_16_out1.wav", 16000, audio2)

for i in range(audio_mid-noise_mid, audio_mid+noise_mid):
  audio2[i]=audio[i]+noise[i-(audio_mid-noise_mid)]

audio21 = audio2.astype(np.int32)
audio3 = audio21 - min(audio21)

esp = 1e-5

audio3 = audio3 + esp
audio4 = np.log10(audio3)
audio4_min, audio4_max = [min(audio4), max(audio4)]
a_min, a_max = [-5, 30]
audio5 = renormalize(audio4, [audio4_min, audio4_max], [a_min, a_max])

audio6 = audio5**10
audio6 = audio6 + min(audio21)
audio6 = audio6 - esp
audio6 = audio6.astype(np.int16)

write("/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2_16_out3.wav", 16000, audio6)
