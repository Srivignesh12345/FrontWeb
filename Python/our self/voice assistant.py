import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen for and recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition request error: {e}")
        return ""

# Main loop
while True:
    # Listen for speech
    text = recognize_speech()

    # If the user said "hello", respond with a greeting
    if "hello" in text.lower():
        speak("Hello, how can I help you?")

    # If the user said "goodbye", respond with a farewell
    elif "goodbye" in text.lower():
        speak("Goodbye!")

    # If the user didn't say anything, continue listening
    elif text == "":
        continue

    # If the user said something we don't recognize, apologize and ask again
    else:
        speak("I'm sorry, I don't understand. Can you please repeat?")
