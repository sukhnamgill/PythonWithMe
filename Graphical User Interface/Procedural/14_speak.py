# pip install pyttsx3
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties (optional)
engine.setProperty('rate', 150)      # Speed of speech
engine.setProperty('volume', 0.9)    # Volume (0.0 to 1.0)

# Define the text you want to convert to speech
text = "Hello, Sukhnam! How can I assist you today?"

# Start speaking the text
engine.say(text)
engine.runAndWait()

