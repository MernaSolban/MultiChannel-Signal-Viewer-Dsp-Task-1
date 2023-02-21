import streamlit as st 
import pandas as pd
import numpy as np

## Page Layout
st.set_page_config(layout="wide",page_title="Signal Manipulator" , page_icon=":radio:")



#############
#Title  
st.title("Signal Viewer Task 1 Demo") 

#viewports
with st.container():
    
   viewport_1, viewport_2=st.columns(2)

with viewport_1:
#insert viewport1
 st.subheader("Viewport1")
 chart_data=pd.DataFrame(

    columns=['a', 'b', 'c'])
 
 st.area_chart(chart_data)
    
with viewport_2:
#insert viewport2
 st.subheader("Viewport2")


#controls
with st.container():
    controls_col_1, controls_col_2 = st.columns(2)
#upload signal
add_signal_button1 = st.button("Add First Signal" , key="add_button1")
add_signal_button2= st.button("Add second signal" , key="add_button2")

#radio buttons
control_mode = st.selectbox(
'Current signal',
('Viewport 1', 'Viewport 2', 'Both'))
#zoom

#pause

#