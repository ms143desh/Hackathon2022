import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    try:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        # text = r.recognize_google(audio_data, language="es-ES")
        print(text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
