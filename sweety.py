import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text.lower()  # Convert to lowercase for easier matching
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the Google Speech Recognition service.")
            return None

# Function to perform actions based on user input
def perform_action(text):
    if "what's your name" in text or "what is your name" in text:
        engine.say("My name is Sweety , your personal assistant.")
        engine.runAndWait()
    elif "what's time now" in text or "what is time now" in text:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        engine.say("The time is " + time)
        engine.runAndWait()
    elif "search for google" in text:
        query = text.replace("search for", "").strip()
        engine.say(f"Searching for {query} ")
        engine.runAndWait()
        pywhatkit.search(query)
    elif "who is the" in text:
        query = text.replace("who is the", "").strip()
        engine.say(f"Let me check who {query} is the.")
    elif "what is" in text:
        query = text.replace("what is", "").strip()
        engine.say(f"Let me check what {query} is.")
        try:
            result = wikipedia.summary(query, sentences=1)
            engine.say(result)
        except wikipedia.exceptions.DisambiguationError as e:
            engine.say("There are multiple entries for this topic. Please be more specific.")
        except wikipedia.exceptions.PageError:
            engine.say("Sorry, I couldn't find any information on that.")
        engine.runAndWait()
    elif "good night sweety" in text or "quit" in text:
        engine.say("Good night Friend Have a Nice Day!")
        engine.runAndWait()
        return False
    else:
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()
    return True

# Main loop
while True:
    text = speech_to_text()
    if text:
        if not perform_action(text):
            break
