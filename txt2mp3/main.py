from gtts import gTTS 
text="Hello Soll! how are you!"
tts=gTTS(text,lang='en')
tts.save('mp3/sound.mp3')