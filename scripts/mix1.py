from scipy.io.wavfile import read, write
import numpy as np

noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/factory1.wav"
noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/babble.wav"
noise_file = "/home/carla/msattir/noise_mix/audio_samples/noise/factory1_16.wav"
audio_file = "/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2.wav"
audio_file = "/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2_16.wav"

noise = np.array(read(noise_file)[1], dtype=float)
audio = np.array(read(audio_file)[1], dtype=float)

noise_smpl_rate = read(noise_file)[0]
audio_smpl_rate = read(audio_file)[0]

#Mix wav files with same sample rates
assert noise_smpl_rate == audio_smpl_rate

noise_mid = int(len(noise)/2)
audio_mid = int(len(audio)/2)

audio2 = np.asarray(audio, dtype=np.int16)
print (len(audio), len(noise))
write("/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2_16_out1.wav", 16000, audio2)

for i in range(audio_mid-noise_mid, audio_mid+noise_mid):
  audio2[i]=audio[i]+noise[i-(audio_mid-noise_mid)]


write("/home/carla/msattir/noise_mix/audio_samples/audio/sw04023-2_16_out2.wav", 16000, audio2)
