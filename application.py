import pyttsx3
text = input("Enter any sentence: ")
voice_rate = int(input("Enter voice Rate: "))
voice_type = int(input("Type '0' for Male or '1' for Female: "))

engine = pyttsx3.init()

engine.setProperty('rate', voice_rate)
voices = engine.getProperty('voices')

if voice_type >= len(voices):
    print("Invalid voice type. Defaulting to the first available voice.")
    voice_type = 0

engine.setProperty('voice', voices[voice_type].id)
engine.say(text)

engine.save_to_file(text, 'application.mp3')

engine.runAndWait()
