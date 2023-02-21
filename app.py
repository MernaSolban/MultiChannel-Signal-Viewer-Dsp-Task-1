import streamlit as st   #for web development
import pandas as pd  #read csv( CSV (comma-separated values) file is a text file that has a specific format which allows data to be saved in a table structured format) , data manipulation
import numpy as np  #numerical computations
import time #simulating real time data,loops
import plotly.express as px  #interactive charts

## Page Layout
st.set_page_config(layout="wide",page_title="Signal viewer and manipulator" , page_icon=":radio:")  #title imp for Search engine optimization



#############
#Title  
st.title("Signal Viewer Task 1 Demo") 

#  Choose which signal to manipulate or control
control_mode = st.selectbox(
'Current signal',
('Signal 1', 'Signal 2', 'Link'))

placeholder=st.empty()

#viewports
with st.container():
    
   viewport_1, viewport_2=st.columns(2)

with viewport_1:
#insert viewport1
 st.subheader("First Signal")
 chart_data=pd.DataFrame(

    columns=['a', 'b', 'c'])
 
 st.area_chart(chart_data)
    
with viewport_2:
#insert viewport2
 st.subheader("Second Signal")


#controls
with st.container():
    controls_col_1, controls_col_2 = st.columns(2)
#upload signal
with controls_col_1:
   add_signal_button1 = st.button("Add First Signal" , key="add_button1")
   
with controls_col_2:  
   add_signal_button2= st.button("Add second signal" , key="add_button2")



#zoom

#pause

#