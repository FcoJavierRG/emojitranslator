import streamlit as st

# 1. The Title
st.title("My Emoji Translator 💬➡️😎")

# --- NEW: Instructions Section ---
with st.expander("👉 How to use this app"):
    st.write("""
        1.  Type a sentence in the **"Enter your text"** box.
        2.  If your sentence includes any of the "Magic Words" listed below, they will be translated into emojis!
        3.  Try it! Type: `I love coding with python and my cat`
    """)
# --- End of new section ---


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

# --- NEW: Show the "magic words" to the user ---
st.subheader("Magic Words We Know:")
# We'll join all the keys (the words) into a single string
st.write(", ".join(EMOJI_DICT.keys()))
st.markdown("---") # Adds a horizontal line
# --- End of new section ---


# 3. Get input from the user
user_input = st.text_input("Enter your text to translate:")

# 4. "Translate" the text
# We'll split the sentence into a list of words
# .lower() makes sure "Love" and "love" are both found
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
# (Only show the header if there is text to show)
if output_sentence:
    st.header("Your Emoji Sentence:")
    st.write(output_sentence)
