import speech_recognition as sr

audio_filename = "../data/audio-files/default_small_audio_file.wav"

# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(audio_filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
