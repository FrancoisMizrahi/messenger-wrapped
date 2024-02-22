import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import label_font_size, figsize

from utils.visualization_utils import (
    get_participant_message_counts,
    get_participant_full_df,
    )


class Visualization():
    
    @staticmethod
    def bar_plot_message_count(data):
        st.subheader("Number of Messages per Person")
        
        df = get_participant_message_counts(data)
        df_sorted = df.sort_values(by='messages_count', ascending=False)
        
        plt.figure(figsize=figsize)
        sns.barplot(x='messages_count', y='index', data=df_sorted, color='#67c0fc')
        plt.xlabel('Messages Count', fontsize=label_font_size)
        plt.ylabel('', fontsize=label_font_size)
        st.pyplot()


    @staticmethod
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

        plt.figure(figsize=figsize)
        sns.lineplot(x='date', y='index', data=df_messages_year_month, palette='viridis')
        plt.xlabel('Date', fontsize=label_font_size)
        plt.ylabel('Number of Messages', fontsize=label_font_size)
        st.pyplot()


    @staticmethod
    def line_plot_number_messages_evolution_per_user(data):
        st.subheader("Number of Messages Evolution Over Time")
        df = get_participant_full_df(data)

        users = st.multiselect(
            'Select Users',
            df.sender_name.unique(),
            df.sender_name.unique())

        df_messages_year_month_sender = df.groupby(by=["sender_name", "year", "month"]).count()[['index']].reset_index()
        df_messages_year_month_sender['date'] = pd.to_datetime(df_messages_year_month_sender[['year', 'month']].assign(day=1))

        plt.figure(figsize=figsize)
        for n in users:
            sns.lineplot(x='date', y='index', data=df_messages_year_month_sender[df_messages_year_month_sender["sender_name"] == n], label=n)
        plt.title('Number of messages Evolution Over Time')
        plt.xlabel('Date', fontsize=label_font_size)
        plt.ylabel('Number of Messages', fontsize=label_font_size)
        plt.legend(fontsize=15)
        st.pyplot()


    @staticmethod
    def bar_plot_number_messages_per_units_of_time(data):
        st.subheader("Number of Messages")
        df = get_participant_full_df(data)

        grannularity = st.selectbox(
            'Select Time Grannularity',
            ["Month", "Day of Month", "Day of Week"])
        
        if grannularity == "Month":
            df_messages_avg_month = df.groupby(by=["year", "month"]).count()[['index']].reset_index()
            df_messages_avg_month = df_messages_avg_month.groupby(by=["month"]).mean()[['index']].reset_index()
            plt.figure(figsize=figsize)
            sns.barplot(x='month', y='index', data=df_messages_avg_month, color='#67c0fc')
            plt.title('Average Number of Messages per Month')
            plt.xlabel('Month', fontsize=label_font_size)
            plt.ylabel('Number of Messages', fontsize=label_font_size)
            st.pyplot()

        elif grannularity == "Day of Month":
            df_messages_avg_month_day = df.groupby(by=["year", "month", 'day']).count()[['index']].reset_index()
            df_messages_avg_month_day = df_messages_avg_month_day.groupby(by=["day"]).mean()[['index']].reset_index()
            plt.figure(figsize=figsize)
            sns.barplot(x='day', y='index', data=df_messages_avg_month_day, color='#67c0fc')
            plt.title('Average Number of Messages per Day of the Month')
            plt.xlabel('Day of the Month', fontsize=label_font_size)
            plt.ylabel('Number of Messages', fontsize=label_font_size)
            st.pyplot()

        else:
            df_messages_day_week = df.groupby(by=['day_week']).count()[['index']].reset_index()
            plt.figure(figsize=figsize)
            sns.barplot(x='day_week', y='index', data=df_messages_day_week, color='#67c0fc')
            plt.title('Number of Messages per Day of the Week')
            plt.xlabel('Day of the Week', fontsize=label_font_size)
            plt.ylabel('Number of Messages', fontsize=label_font_size)
            st.pyplot()


    @staticmethod
    def dot_plot_all_messages(data):
        st.subheader("All of Messages")
        df = get_participant_full_df(data) 

        # Extract date and time information
        df['date'] = df['timestamp'].dt.date
        df['time'] = df['timestamp'].dt.time

        # Convert time to seconds past midnight
        df['seconds'] = df['time'].apply(lambda time: time.hour*3600 + time.minute*60 + time.second)

        # Sorting dataframe by 'date' and 'seconds' 
        df = df.sort_values(['date', 'seconds'])

        # Plotting
        plt.figure(figsize=figsize)
        sns.scatterplot(x='date', y='seconds', data=df, s=20, alpha=0.5, edgecolor = None)

        plt.xlabel('Date', fontsize=label_font_size)
        plt.ylabel('Time of the day', fontsize=label_font_size)
        plt.title('Messages')
        plt.xticks(rotation=45)

        # Setting the y-axis labels as time strings
        y_ticks = [f'{h}:00' for h in range(24)]
        plt.yticks(ticks=range(0, 24*3600, 3600), labels=y_ticks)

        plt.tight_layout()
        st.pyplot()


    @staticmethod
    def heatmap_messages_count(data):
        st.subheader("Number of Messages")
        df = get_participant_full_df(data)

        df['Day_of_Week'] = df['timestamp'].dt.day_name()
        df['Hour_of_Day'] = df['timestamp'].dt.hour

        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Create a pivot table for the heatmap
        heatmap_data = df.pivot_table(index='Hour_of_Day', columns='Day_of_Week', values='content', aggfunc='count')

        # Reorder columns based on the specified order
        heatmap_data = heatmap_data[day_order]

        # Create the heatmap using seaborn
        plt.figure(figsize=figsize)
        sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False, linewidths=0.5)
        plt.title('Message Heatmap')
        plt.xlabel('Day of the Week', fontsize=label_font_size)
        plt.ylabel('Hour of the Day', fontsize=label_font_size)
        st.pyplot()