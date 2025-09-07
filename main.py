import pyedflib as edf
import numpy as np
import matplotlib.pyplot as plt

f = edf.EdfReader("TG7.edf")
sh = f.getSignalLabels()
dur = f.getFileDuration()
f.close()
signals, signal_headers, header = edf.highlevel.read_edf("TG7.edf")
signals = np.array(signals)
sample = len(signals[0])
x = np.linspace(0, dur, sample)
fig, ax = plt.subplots(4, 2)
for i in range(len(sh)):
    signal = signals[i]
    ax[i//2, i%2].plot(x, signal)
    ax[i//2, i%2].set_title(f'Канал {i + 1}: {sh[i]}')
plt.tight_layout()
plt.show()



