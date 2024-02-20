import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.visualization_utils import (
    get_participant_message_counts,
    get_participant_full_df,
    )


def bar_plot_message_count(data):
    st.subheader("Number of Messages per Person")
    
    df = get_participant_message_counts(data)
    df_sorted = df.sort_values(by='messages_count', ascending=False)
    
    plt.figure(figsize=(20,10))
    sns.barplot(x='messages_count', y='index', data=df_sorted, color='#67c0fc')
    plt.xlabel('Messages Count', fontsize=18)
    plt.ylabel('', fontsize=18)
    st.pyplot()


def line_plot_number_messages_evolution(data):
    st.subheader("Number of Messages Evolution Over Time")
    grannularity = st.selectbox('Select grannularity', ('Monthly', 'Daily'))
    
    df = get_participant_full_df(data)

    if grannularity == "Monthly":
        df_messages_year_month = df.groupby(by=["year", "month"]).count()[['index']].reset_index()
        df_messages_year_month['date'] = pd.to_datetime(df_messages_year_month[['year', 'month']].assign(day=1))
    else:
        df_messages_year_month = df.groupby(by=["year", "month", "day"]).count()[['index']].reset_index()
        df_messages_year_month['date'] = pd.to_datetime(df_messages_year_month[["year", "month", "day"]])

    plt.figure(figsize=(20,10))
    sns.lineplot(x='date', y='index', data=df_messages_year_month, palette='viridis')
    plt.xlabel('Date')
    plt.ylabel('Number of Messages')
    st.pyplot()


def line_plot_number_messages_evolution_per_user(data):
    st.subheader("Number of Messages Evolution Over Time")
    df = get_participant_full_df(data)

    users = st.multiselect(
        'Select Users',
        df.sender_name.unique(),
        df.sender_name.unique())

    df_messages_year_month_sender = df.groupby(by=["sender_name", "year", "month"]).count()[['index']].reset_index()
    df_messages_year_month_sender['date'] = pd.to_datetime(df_messages_year_month_sender[['year', 'month']].assign(day=1))

    plt.figure(figsize=(20,10))
    for n in users:
        sns.lineplot(x='date', y='index', data=df_messages_year_month_sender[df_messages_year_month_sender["sender_name"] == n], label=n)
    plt.title('Number of messages Evolution Over Time')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Number of Messages', fontsize=18)
    plt.legend(fontsize=15)
    st.pyplot()


