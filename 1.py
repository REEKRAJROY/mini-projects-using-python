from gtts import gTTS
import os
f = open('smth.txt')
x = f.read()  # extracted text
language = 'en'
audio = gTTS(text=x, lang=language, slow=False)
audio.save("1.wav")  # .wav audio file
os.system("1.wav")

