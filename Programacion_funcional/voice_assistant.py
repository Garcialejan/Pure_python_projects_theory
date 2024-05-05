import pyttsx3
import speech_recognition as sr
import re


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 200) # Para ajustar la velocidad con la que habla
    engine.setProperty("voice", "spanish")
    return engine


def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
        name = identify_name(text)
    return text


def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:# We define multiple ways to take the name od the user
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def main():
    engine = initialize_engine()
    engine.say("Hola, ¿como te llamas?")
    engine.runAndWait()
    r = sr.Recognizer()
    text = recognize_voice(r)
    name = identify_name(text)
    if name:
        engine.say("Encantado de conocerte {}".format(name))
    else:
        engine.say("No me has dicho tu nombre todavía")
    engine.runAndWait()

if __name__ == "__main__":
    main()
