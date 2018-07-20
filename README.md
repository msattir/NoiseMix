# NoiseMix
Mixing Noise and Audio files

Resampling audio and noise files (Requires SoX)  
 ```for i in *;do  sox $i -r 16000 ${i%.wav}_16.wav; rm $i; done```


Recommended Folder structure  
 mix_try1  
  --| audio  
  --| noise  
  --| output  
   
from mix_try run:  
 ```for i in audio/*; do for j in noise/*;do python ../scripts/mix1.py $i $j 20 ./output/;done ; done```
 
 mix1.py   
 ```"Usage: ./mix1.py [audio_file] [noise_file] [num_times] [output_directory]"```
