# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mgd0JZd8HcF6Vhveo3QbuqPGjElh84hg
"""

!pip install textblob

from textblob import TextBlob

def detect_emotion(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Happy"
    elif analysis.sentiment.polarity < 0:
        return "Sad"
    else:
        return "Neutral"

def chatbot():
    print("Welcome to the Emotion Detection Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        emotion = detect_emotion(user_input)
        print(f"Chatbot: I sense you're feeling {emotion}.")

if __name__ == "__main__":
    chatbot()

import unittest
from textblob import TextBlob

def detect_emotion(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Happy"
    elif analysis.sentiment.polarity < 0:
        return "Sad"
    else:
        return "Neutral"

def chatbot():
    print("Welcome to the Emotion Detection Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        emotion = detect_emotion(user_input)
        print(f"Chatbot: I sense you're feeling {emotion}.")

# ... (rest of your code) ...

if __name__ == "__main__":
    #chatbot()
    # Call unittest.main() with exit=False
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # Now you can call chatbot() or other functions after the tests
    #chatbot()