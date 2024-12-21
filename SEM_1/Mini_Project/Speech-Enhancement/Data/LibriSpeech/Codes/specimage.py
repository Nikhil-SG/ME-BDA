import numpy as np
img_array = np.load('"E:\MAHE\1st Sem\Mini Project - 1\Speech-Enhancement\Data\Train\spectrogram\noise_amp_db.npy"')
from matplotlib import pyplot as plt
plt.imshow(img_array, cmap='gray')
plt.show()