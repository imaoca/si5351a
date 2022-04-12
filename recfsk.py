from re import I
import pyaudio
import wave
import numpy as np

chunk = 8000*2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 1

FQm= RATE/431     # Mark Frequency 914Hz
FQs= RATE/1434    # Space Frequency 1086Hz
wind= 32           # windows size Integer
 
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

#print(data)
""""
for j in range(0,16000-1,2):
    i = data[j+1]
    print(i)

"""

mq=[];mi=[];sq=[];si=[]
for j in range(0,16000-1,2):
      i = data[j+1]-128
      mq.append((i)*np.sin(np.pi/FQm*j))
      mi.append((i)*np.cos(np.pi/FQm*j))
      sq.append((i)*np.sin(np.pi/FQs*j))
      si.append((i)*np.cos(np.pi/FQs*j))
      mk = np.sqrt(sum(mq)**2 + sum(mi)**2)
      sp = np.sqrt(sum(sq)**2 + sum(si)**2)     
      print(mk,sp,int(mk>sp),sep=",")
      if j>wind:
            mq.pop(0);mi.pop(0);sq.pop(0);si.pop(0)
