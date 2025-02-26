import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import cohere

newsapi = "<ADD YOUR API KEY>"
pygame.mixer.init()
import pygame
import os
from gtts import gTTS

def speak(text):
    try:
        if not text.strip():  # Ensure text is not empty
            return
        
        pygame.mixer.init()
        tts = gTTS(text)  
        temp_file = "temp.mp3"
        tts.save(temp_file)  # Save the speech file
        
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)  # Small delay to prevent CPU overload

        pygame.mixer.music.unload()
        os.remove(temp_file)  # Delete temp file after playing

    except Exception as e:
        print(f"Error in speak function: {e}")

        
def aicommnad(command):
    co = cohere.ClientV2("<ADD YOUR API KEY>")
    response = co.chat(
        model="command-r-plus",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": command}
        ]
    )
    return response.message.content[0].text

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif command.startswith("news"):
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles[:5]:  # Limit to 5 news items
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't fetch the news")
        except Exception as e:
            speak("Error fetching news")
            print(f"Error: {e}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    elif "how are you" in command:
        speak("I'm just a virtual assistant, but I'm here to help! How can I assist you today?")
    elif "who are you" in command:
        speak("I am Jarvis, your personal AI assistant, here to assist you with various tasks!")
    elif "what can you do" in command:
        speak("I can open websites, play music, fetch news, and assist you with various tasks. Just ask!")
    else:
        output = aicommnad(command)
        print("Response from Cohere:", output)  
        speak(output)  


if __name__ == "__main__":
    speak("Hello, Jarvis here. How can I assist you?")
    recognizer = sr.Recognizer()
    
    while True:
        print("Listening for wake word 'Jarvis'...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio).lower()
                
                if word == "jarvis":
                    speak("Yes, I am listening")
                    print("Jarvis activated...")

                    
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio).lower()
                    print("Heard Command:", command)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            speak("Sorry, speech service is down")
        except Exception as e:
            print(f"Error: {e}")
