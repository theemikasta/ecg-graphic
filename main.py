import pyedflib as edf
import numpy as np
import matplotlib.pyplot as plt

#длительность и количество каналов файла
f = edf.EdfReader("TG7.edf")
sh = f.getSignalLabels()
dur = f.getFileDuration()
f.close()

#количество и значения сигналов ЭКГ (через highlevel т.к. создает массив со всеми каналами)
signals, signal_headers, header = edf.highlevel.read_edf("TG7.edf")
signals = np.array(signals)
sample = len(signals[0])
x = np.linspace(0, dur, sample) #равномерное распределение сигналов по длительности измерения
fig, ax = plt.subplots(4, 2) #сетка графиков
for i in range(len(sh)):
    signal = signals[i]
    ax[i//2, i%2].plot(x, signal)
    ax[i//2, i%2].set_title(f'Канал {i + 1}: {sh[i]}')
plt.tight_layout()
plt.show()



