from msvcrt import kbhit
from re import I
import pyaudio
import wave
import numpy as np

chunk = 8000*2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 1
FQ= RATE/1256.0      # Signal Frequency 
wind= 40            # window

p = pyaudio.PyAudio()
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = chunk
)
data = stream.read(chunk)
stream.close()   
p.terminate

q=[];i=[]
for j in range(0,16000-1,2):
      k = data[j+1]-128      
      q.append(k*np.sin(np.pi/FQ*j))
      i.append(k*np.cos(np.pi/FQ*j))
      print(int(sum(q)>0),int(sum(i)>0),sep=",")
      if j>wind:q.pop(0);i.pop(0)
