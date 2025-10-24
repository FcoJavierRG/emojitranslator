import streamlit as st

# 1. The Title
st.title("My Emoji Translator 💬➡️😎")

# 2. Our "translation dictionary"
# This is a simple Python dictionary.
# Key = the word to find, Value = the emoji to replace it with
EMOJI_DICT = {
    "love": "❤️",
    "happy": "😊",
    "sad": "😢",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "coding": "💻",
    "win": "🏆",
    "python": "🐍",
    "fire": "🔥"
    # Students can add more!
}

# 3. Get input from the user
user_input = st.text_input("Enter your text to translate:")

# 4. "Translate" the text
# We'll split the sentence into a list of words
words = user_input.lower().split()

# 5. Create a new list for our translated words
translated_words = []

# 6. Loop through all the words
for word in words:
    # Use .get() to find the word in our dictionary.
    # If it's not found, it just returns the original word.
    translated_word = EMOJI_DICT.get(word, word)
    translated_words.append(translated_word)

# 7. Join the translated words back into a sentence
output_sentence = " ".join(translated_words)

# 8. Display the final result!
st.header("Your Emoji Sentence:")
st.write(output_sentence)
