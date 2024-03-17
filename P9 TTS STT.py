import pyttsx3
import speech_recognition as sr

#Text-To-Speech
engine = pyttsx3.init()
print("Saail Chavan - KFPMSCCS016 CL_P9")
print("TTS:")
text = input("Enter text: ")
engine.say(text)
engine.runAndWait()

#Speech-to-Text
print("\nSTT:")
filename = "Test.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.WavFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize(audio_data)
    print(text,"\n")