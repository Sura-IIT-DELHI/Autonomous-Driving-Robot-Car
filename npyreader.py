import numpy as np
from PIL import Image
import pandas as pd
image=np.load('./data_cooked/image.npy')
previous_state=np.load('./data_cooked/previous_state.npy')
label=np.load('./data_cooked/label.npy')
print image.shape
print previous_state.shape
print label.shape

print previous_state[0]
print label[0]
