import streamlit as st

from utils.utils import upload_file
from visualization import Visualization

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")

col1, maincol, col2 = st.columns([1, 4, 1])
with maincol:
    st.title('Messenger Wrapped')

    data = upload_file()

    if data:
        st.header("Visualizations")
        
        st.divider()
        Visualization.bar_plot_message_count(data)
        
        st.divider()
        Visualization.bar_plot_number_messages_per_units_of_time(data)
        
        st.divider()
        Visualization.line_plot_number_messages_evolution(data)
        
        st.divider()
        Visualization.line_plot_number_messages_evolution_per_user(data)

        st.divider()
        Visualization.dot_plot_all_messages(data)

        st.divider()
        Visualization.heatmap_messages_count(data)