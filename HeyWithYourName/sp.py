import pyttsx3

engine = pyttsx3.init()
name = input("Tell me you name  ")
engine.say(f"Hey, {name}")
engine.runAndWait()
