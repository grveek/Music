#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


half_steps_sharps = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
half_steps_flats = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"]
half_steps = np.arange(0,12,1)


# In[4]:


key_major_half_steps = np.array([0,2,4,5,7,9,11])
key_minor_half_steps = np.array([0,2,3,5,7,8,10])
key_dorian_half_steps = np.array([0,2,3,5,7,9,10])
key_phrygian_half_steps = np.array([0,1,3,5,7,8,10])
key_lydian_half_steps = np.array([0,2,4,6,7,9,11])
key_mixolydian_half_steps = np.array([0,2,4,5,7,9,10])
key_locrian_half_steps = np.array([0,1,3,5,6,8,10])
key_byzantine_half_steps = np.array([0,1,4,5,6,8,10])
key_enigmatic_half_steps = np.array([0,2,3,5,7,9,10])
key_neopolitan_maj_half_steps = np.array([0,1,3,5,7,9,11])
key_neopolitan_min_half_steps = np.array([0,1,3,5,7,8,11])
key_hungarian_maj_half_steps = np.array([0,3,4,6,7,9,10])
key_hungarian_min_half_steps = np.array([0,2,3,6,7,8,11])
key_mixolydianb6_half_steps = np.array([0,2,4,5,7,8,10])
key_harmonic_min_half_steps = np.array([0,2,3,5,7,8,11])
key_lydian_dom_half_steps = np.array([0,2,4,6,7,9,10])
key_diminished_half_steps = np.array([0,2,3,5,6,8,9])
key_half_diminished_half_steps = np.array([0,1,3,4,6,7,9])
key_dorian_sharp4_half_steps = np.array([0,2,3,6,7,9,10])
notes = ["A", "B", "C", "D", "E", "F", "G"]
chord_symbols = ["m", "dim", "+", "add9", "sus2", "sus4", "sus2/4", "b5", "m7b5", "7", "Maj7", "m7" ]
sharp_flat = ["#", "b"]
position = ["I", "II", "III", "IV", "V", "VI", "VII"]
scales_modes = ["Major", "Minor", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Locrian", "Byzantine", "Enigmatic","Neopolitan Major","Neopolitan Minor","Hungarian Major","Hungarian Minor","Mixolydian b6","Harmonic Minor","Lydian Dominant","Diminished","Half-Diminished", "Dorian Sharp 4"]
compiled_scales = [key_major_half_steps,key_minor_half_steps,key_dorian_half_steps,key_phrygian_half_steps,key_lydian_half_steps,key_mixolydian_half_steps,key_locrian_half_steps,key_byzantine_half_steps,key_enigmatic_half_steps,key_neopolitan_maj_half_steps,key_neopolitan_min_half_steps,key_hungarian_maj_half_steps,key_hungarian_min_half_steps,key_mixolydianb6_half_steps,key_harmonic_min_half_steps,key_lydian_dom_half_steps,key_diminished_half_steps,key_half_diminished_half_steps,key_dorian_sharp4_half_steps]
          


# In[5]:


scales_modes_hs_df_chart = pd.DataFrame()
for i in scales_modes:
    for j in compiled_scales:
        scales_modes_hs_df_chart[i] = j

scales_modes_hs_df_chart


# In[6]:


df = scales_modes_hs_df_chart
df.iloc[2:5,4:8]


# In[ ]:





# In[ ]:





# In[ ]:





# In[73]:


# hs notes dictionary
hs_notes = dict((keys,values) for keys,values in zip(half_steps,half_steps_sharps))
z = hs_notes


# In[66]:


#test to see if one can create a key list of notes
key = []
for i in key_major_half_steps:
    for x in z.keys():
        if x == i:
            key.append(z[i])
            
print("A major key:", key)


# In[71]:


#test #2 to see if one can create a key list of notes
key = []
for i in key_minor_half_steps:
    for x in z.keys():
        if x == i:
            key.append(z[i])
            
print("A minor key:", key)


# In[70]:


#test #3 to see if one can create a key list of notes
key = []
for i in key_dorian_half_steps:
    for x in z.keys():
        if x == i:
            key.append(z[i])
            
print("A minor Dorian key:", key)


# In[69]:


key = []
zq = [x for i in key_minor_half_steps for x in z.keys() if x == i]
zq
# list comprehension grabs the matching keys but need values printed (right now - does not function)


# In[1]:


# define a function to obtain the notes to a called key/mode/scale

def get_scale():
    scale_req = input(str("Input required key >>> "))
    # code in user-selected HS list
    # consider using dataframe object above?
    # temp is hard wired to test function - user will select
    temp = key_major_half_steps
    hs_notes = dict((keys,values) for keys,values in zip(half_steps,half_steps_sharps))
    temp_z = hs_notes
    temp_z1 = temp + (half_steps_sharps.index(scale_req) - half_steps_sharps.index("A"))
    for i in range(len(temp_z1)):
        if temp_z1[i] > 12:
            temp_z1[i] = temp_z1[i] - 12
        else:
            i
    key = []
    for i in temp_z1:
        for x in temp_z.keys():
            if x == i:
                key.append(temp_z1[i])
    del temp
    del hs_notes
    del temp_z
    del temp_z1
    print("The", scale_req, "scale is:", key)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




