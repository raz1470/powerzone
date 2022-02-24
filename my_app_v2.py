import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('ticks',{'axes.grid' : True})
from PIL import Image

# Set Title
st.title('Wordle Warriors League')
st.write('The following app tracks the current standings of the Wordle Warriors AKA Josh, Raz, Rob, Poppy and Parky')
#image = Image.open('wordle.jpg')
#st.image(image)

# Daily Results dataframe
data = {'Josh': [3,4,3,4,6,4,6,3,4,5,4,6],
        'Raz':  [3,4,3,6,4,4,6,4,4,3,7,4],
        'Rob':  [4,6,5,5,4,4,5,5,5,6,6,3],
        'Poppy':[5,4,5,3,5,3,5,4,5,2,3,4],
        'Parky':[3,5,4,4,4,6,5,4,4,3,7,4]       
}

df1 = pd.DataFrame(data)

names = ['Josh','Raz','Rob','Poppy','Parky']

# Daily Results
st.subheader('Daily Results')

selection_1 = st.button('View Daily Results')
if selection_1:

    st.table(df1)

# Calculate league table
df2 = pd.DataFrame()
df2['Score'] = df1.sum()
df2 = df2.sort_values(by='Score')
    
# League Table
st.subheader('League Table')

selection_1 = st.button('View League Table')
if selection_1:

    st.table(df2)

    
