Simple Emoji Translator 💬➡️😎

This is a simple web app built with Python, Streamlit, and GitHub, designed for a simple coding activity. It "translates" specific words from a user's sentence into corresponding emojis.

All emojis used in this project are from Get Emoji: https://getemoji.com/.


(Remember to replace the URL above with your own app's live URL after you deploy it!)

🚀 How it Works

This project consists of two key files:

app.py: The main Streamlit web app script.

It uses st.title and st.expander to build the user interface.

It contains a Python dictionary (EMOJI_DICT) that maps words (keys) to emojis (values).

It takes user input, splits it into a list of words, and replaces any word found in the dictionary.

requirements.txt: This file tells Streamlit's servers that this project needs the streamlit library to run.

🏃 How to Run This Project

You can run this app on your own computer or deploy it for free on Streamlit Community Cloud.

To Deploy on Streamlit:

Upload to GitHub: Create a new repository on your GitHub account and upload app.py and requirements.txt.

Go to Streamlit Community Cloud: https://share.streamlit.io/

Deploy a New App:

Point it to your new GitHub repository.

Set the Main file path to app.py.

Deploy!
