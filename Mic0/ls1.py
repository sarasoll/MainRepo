#This app to make a voice to txt ..Enjoy ;)
import speech_recognition
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as sou:
    print ("I am All Ears ;)")
    audio = recognizer.listen(sou)
print ("._.")
print(recognizer.recognize_google(audio))
