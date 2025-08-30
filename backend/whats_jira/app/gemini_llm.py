import dotenv
dotenv.load_dotenv()
from google import genai
import speech_recognition as sr
import os

gemini_api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=gemini_api_key)


def gemini_response(command):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=command)    
    return response

# def audio_to_text(file):
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Load audio file
#     with sr.AudioFile("app/command.wav") as source:
#         audio_data = recognizer.record(source)  # read the entire audio file
        
#         # Convert speech to text
#         try:
#             text = recognizer.recognize_google(audio_data)  # uses Google Speech API
#             print("Text from audio:", text)
#         except sr.UnknownValueError:
#             print("Sorry, could not understand the audio.")
#         except sr.RequestError:
#             print("API request error.")
  

