import numpy as np
from PIL import Image
import pandas as pd
image1=[]
previous_state1=[]
label1=[]
datafile=pd.read_csv('/media/kanish/Data_Softwares/autonomous/'+'syncdata.csv')
datafile = datafile.sample(frac=1).reset_index(drop=True)
for i in range(datafile.shape[0]):
	previous_state=list(datafile.iloc[i][['sonar1','sonar2','sonar3','sonar4','sonar5','sonar6','sonar7','sonar8','sonar9','sonar10','sonar11','sonar12','sonar13','sonar14','sonar15','sonar16','LinvelX','AngvelX']])
	current_label=list(datafile.iloc[i][['LinvelY','AngvelY']])
	previous_state1.append(previous_state)
	label1.append(current_label)
	img = Image.open( '/media/kanish/Data_Softwares/autonomous/images/'+datafile.iloc[i]['image'])
	try:
	    data = np.asarray( img, dtype='uint8' )
	except SystemError:
	    data = np.asarray( img.getdata(), dtype='uint8' )
	image1.append(data)

image=np.asarray(image1)
previous_state=(np.asarray(previous_state1)).astype(float)
label=(np.asarray(label1)).astype(float)
np.save('./data_cooked/image.npy',image)
np.save('./data_cooked/previous_state.npy',previous_state)
np.save('./data_cooked/label.npy',label)