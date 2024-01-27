import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def greet():
    engine.say("Hello! How can I help you today?")
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    engine.say(f"The current time is {current_time}")
    engine.runAndWait()

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    engine.say(f"Searching the web for {query}")
    engine.runAndWait()


greet()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "hello" in command:
            greet()
        elif "time" in command:
            get_time()
        elif "search" in command:
            query = command.split("search")[-1].strip()
            search_web(query)
        elif "exit" in command:
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        else:
            engine.say("I'm sorry, I didn't understand that.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    #except Exception as e:
        #print(f"An error occurred: {e}")
