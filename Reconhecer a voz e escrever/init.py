import speech_recognition as sr
import pyautogui
import time

recognizer = sr.Recognizer()

def ouvir_texto():
    with sr.Microphone() as mic:
        try:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=5)

            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Texto reconhecido: {texto}")
            return texto.lower()
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return ""
        except sr.RequestError:
            print("Erro de conexão.")
            return ""

def comecar():
    print("Diga o que você quiser. E apenas fale 'enviar' para apertar Enter.")
    while True:
        comando = ouvir_texto()
        
        if comando == "enviar":
            pyautogui.press("enter")
            print("Mensagem enviada")
        elif comando:
            pyautogui.typewrite(comando, interval=0.1)
            print(f"Texto digitado: {comando}")
        else:

            time.sleep(0.1)

comecar()
