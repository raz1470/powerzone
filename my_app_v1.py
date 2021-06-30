import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('ticks',{'axes.grid' : True})
from PIL import Image

# Set Title
st.title('Power Zone Rides')
st.write('The following app tracks my Power Zone ride and FTD test performance')
image = Image.open('bike.jpg')
st.image(image)

# Import Ride History
df1 = pd.read_csv('.' + '/raz1470_workouts.csv')
df1 = df1.rename(columns={'Length (minutes)': 'Length'})

# Power Zone Rides
st.subheader('Power Zone Rides')

selection_1 = st.button('View Power Zone Rides')
if selection_1:

    df2 = df1[(df1['Type']=='Power Zone') & (df1['Length']>=30) &(df1['Total Output']>10) & (~df1['Title'].str.contains('Endurance'))]
    df2['Ride ID'] = np.arange(len(df2)) + 1
    
    st.write('Personal Bests:')
    
    df2_tot_max = '- Total Output: ' + str(df2['Total Output'].max()) + ' watts'
    st.write(df2_tot_max)

    df2_avg_max = '- Avg Output: ' + str(df2['Avg. Watts'].max()) + ' watts'
    st.write(df2_avg_max)

    df2_dis_max = '- Distance: ' + str(df2['Distance (mi)'].max()) + ' miles'
    st.write(df2_dis_max)

    fig1, ax1 = plt.subplots()    
    sns.regplot(data=df2, x='Ride ID', y='Avg. Watts', x_estimator=np.mean, logx=True, ci=None)
    ax1.set_title('Power Zone Rides')
    ax1.set_ylabel('Avg Output')
    ax1.set_xlabel('Ride ID')
    st.pyplot(fig1)

# Power Zone Endurence Rides
#st.subheader('Power Zone Endurance Rides')

#selection_2 = st.button('View Power Zone Endurance Rides')
#if selection_2:

#    df3 = df1[(df1['Type']=='Power Zone') & (df1['Length']>=30) &(df1['Total Output']>10) & (df1['Title'].str.contains('Endurance'))]
#    df3['Ride ID'] = np.arange(len(df3)) + 1

#    df3_tot_max = 'PB: Total Output ' + str(df3['Total Output'].max()) + ' watts'
#    st.write(df3_tot_max)

#    df3_avg_max = 'PB: Avg Output ' + str(df3['Avg. Watts'].max()) + ' watts'
#    st.write(df3_avg_max)

#    df3_dis_max = 'PB: Distance ' + str(df3['Distance (mi)'].max()) + ' miles'
#    st.write(df3_dis_max)

#    fig2, ax2 = plt.subplots()    
#    sns.lineplot(data=df3, x='Ride ID', y='Avg. Watts', ax=ax2, marker='o')
#    ax2.set_title('Power Zone Endurance Rides')
#    ax2.set_ylabel('Avg Output')
#    ax2.set_xlabel('Ride ID')
#    st.pyplot(fig2)

# FTP Tests
st.subheader('FTP Tests')

selection_3 = st.button('View FTP Tests')
if selection_3:

    df4 = df1[(df1['Type']=='Power Zone') & (df1['Title']=='20 min FTP Test Ride') &(df1['Total Output']>10)]
    df4['Ride ID'] = np.arange(len(df4)) + 1
    
    st.write('Personal Bests:')

    df4_tot_max = '- Total Output: ' + str(df4['Total Output'].max()) + ' watts'
    st.write(df4_tot_max)

    df4_avg_max = '- Avg Output: ' + str(df4['Avg. Watts'].max()) + ' watts'
    st.write(df4_avg_max)

    df4_dis_max = '- Distance: ' + str(df4['Distance (mi)'].max()) + ' miles'
    st.write(df4_dis_max)

    fig3, ax3 = plt.subplots()
#    sns.lineplot(data=df4, x='Ride ID', y='Avg. Watts', ax=ax3, marker='o')
    sns.regplot(data=df4, x='Ride ID', y='Avg. Watts', x_estimator=np.mean, logx=True, ci=None)
    ax3.set_title('FTP Tests')
    ax3.set_ylabel('Avg Output')
    ax3.set_xlabel('Ride ID')
    st.pyplot(fig3)


