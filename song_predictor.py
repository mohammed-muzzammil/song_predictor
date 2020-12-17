import streamlit as st
import pickle
import os
import urllib
import urllib.request

import os.path
from os import path

#os.chdir(r'C:\Users\MOHAMMED MUZZAMMIL\Desktop\job1')
Pkl_Filename = "Pickle_RL_Model.pkl"



    
    
st.markdown("<h1 style='text-align: center; color: Light gray;'>How likely is your song to be a popular?</h1>", unsafe_allow_html=True)


st.info('This is a prediction model based on the database of 2,00,000 songs move the sliders on the left to understand whether your song has what it takes to be popular ')

valence = st.sidebar.slider('how positive was the track?', 0.00, 1.00, 0.00)

acousticness = st.sidebar.slider('how acoustic were the instruments?', 0.00, 1.00, 0.00)

danceability = st.sidebar.slider('how suitable is it for dancing?', 0.00, 1.00, 0.00)

energy = st.sidebar.slider('how energetic is the track?', 0.00, 1.00, 0.00)

explicit = st.sidebar.slider('how explicit are the lyrics?',0.00,1.00,0.00)

liveness = st.sidebar.slider('how loud is the recorded crowd/audience?', 0.00, 1.00, 0.00)

loudness = st.sidebar.slider('how loud does it feel compared to other tracks?', -60.00, 0.00, -60.00)

speechiness = st.sidebar.slider('was there a lot of talking in the track? poetry etc?', 0.00, 1.00, 0.00)

rd=("YES","NO")
release_date_str = st.sidebar.radio('was this released in the last 5 years?',rd)



if release_date_str == 'YES':
    release_date=1
elif release_date_str == 'NO':
    release_date=0


if st.sidebar.button('Predict'):
    
    if path.exists('Pickle_RL_Model.pkl'):
        
        with open(Pkl_Filename, 'rb') as file:  
            
            Pickled_LR_Model = pickle.load(file)


    else:
        
        urllib.request.urlretrieve("https://drive.google.com/u/0/uc?id=18wuXoOrUgVebzuL6NIQXZJJnf7mY4NGN&export=download", "Pickle_RL_Model.pkl")
        
        with open(Pkl_Filename, 'rb') as file: 
            
            Pickled_LR_Model = pickle.load(file)
   
    
    
    
    input_s=Pickled_LR_Model.predict([1,valence,acousticness,danceability,energy,explicit,liveness,loudness,release_date,speechiness]) 
    
 
    
    if input_s>0.2:
        
        st.info('this song could definitely be popular!')
        
    else:
        
        st.info('sorry, this song may not be popular!')
        

