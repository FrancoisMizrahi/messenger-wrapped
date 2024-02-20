import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.visualization_utils import (
    get_participant_message_counts,
    get_participant_full_df,
    )


def bar_plot_message_count(data):
    df = get_participant_message_counts(data)
    st.subheader("Number of Messages per Person")
    plt.figure(figsize=(20,10))
    df_sorted = df.sort_values(by='messages_count', ascending=False)
    sns.barplot(x='messages_count', y='index', data=df_sorted, color='#67c0fc')
    plt.xlabel('Messages Count', fontsize=18)
    plt.ylabel('', fontsize=18)
    st.pyplot()


def line_plot_number_messages_evolution(data):
    df = get_participant_full_df(data)
    st.subheader("Number of messages Evolution Over Time")
    df_messages_year_month = df.groupby(by=["year", "month"]).count()[['index']].reset_index()
    df_messages_year_month['date'] = pd.to_datetime(df_messages_year_month[['year', 'month']].assign(day=1))

    plt.figure(figsize=(20,10))
    sns.lineplot(x='date', y='index', data=df_messages_year_month, palette='viridis')
    plt.xlabel('Date')
    plt.ylabel('Number of Messages')
    st.pyplot()