import streamlit as st

from utils.utils import upload_file
from visualization import (
    bar_plot_message_count, 
    line_plot_number_messages_evolution,
    )

st.set_option('deprecation.showPyplotGlobalUse', False)


st.title('Messenger Wrapped')

data = upload_file()

if data:
    st.header("Visualizations")
    
    st.divider()
    bar_plot_message_count(data)
    
    st.divider()
    line_plot_number_messages_evolution(data)
