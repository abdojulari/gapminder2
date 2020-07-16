# Assignment using Seaborn Heatmap
import numpy as np
import seaborn as sb

import pandas as pd
import matplotlib.pyplot as plt

# reading the dataset
dataset =  pd.read_csv('dataset.csv')

# setting the year along the x axis and continent along y axis 

dataset_df =  dataset.pivot_table(values='lifeExp', index='continent', columns='year', aggfunc=np.average)

sb.heatmap(dataset_df, annot=True)

# using annot to add values to the cells over the heatmap
   
plt.savefig('image_seaborn.png', dpi=400)