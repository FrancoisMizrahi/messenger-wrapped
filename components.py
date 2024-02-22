import streamlit as st


def info_find_messenger_data():
    with st.expander("Help finding/ uploding the Date"):
        st.subheader("How to find my Messenger Data")
        st.write("""
                To Download you facebook Data follow these instructions:
                Request a download of your Facebook information from Accounts Centre
                - Click on your profile picture in the top right, then click Settings and privacy.
                - Click Settings.
                - Click Accounts Centre, then click Your information and permissions.
                - Click Download your information.
                - Click Request a download.
                - Select the profiles that you'd like to download information from.
                - Click Next.
                - Select the information that you want to download.
                
                Once you've selected the information that you want to download, choose your file options:
                - The date range
                - The notification email
                - The format of your download request.
                - The quality of photos, videos and other media.
                - Click Submit request.
            """)
        st.subheader("Locate the right file to Upload")
        st.write("""
                Once you have downloaded you Facebook Data, you should hace a ZIP file.
                 - First, Unzip the file
                 - Second, navigate to your_activity_across_facebook > messages > inbox
                 - Thrid, open the folder of the conversation you are intrested in
                 - Last, Upload the JSON file called message_1.json
            """)
