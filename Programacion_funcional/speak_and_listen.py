import pyttsx3
import speech_recognition as sr
from speech_recognition import UnknownValueError


engine = pyttsx3.init()
engine.setProperty("rate", 170) # Para ajustar la velocidad con la que habla
engine.setProperty("voice", "spanish")
r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear_me():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
           text = r.recognize_google(audio, language="es-ES")
           print("He entendido lo siguiente: {}".format(text))
           return text
        except UnknownValueError:
            return

if __name__ == "__main__":
    speak("Probando el programa")
    hear_me()



