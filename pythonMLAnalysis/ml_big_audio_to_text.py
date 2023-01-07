import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
# from pydub.utils import which

# create a speech recognition object
from app_configuration import audio_chunk_folder_name

r = sr.Recognizer()


# function that splits the audio file into chunks and applies speech recognition
def get_large_audio_transcription(audio_file_path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """

    # AudioSegment.converter = which("ffmpeg")
    # sound = AudioSegment.from_wav(audio_file_path)
    sound = AudioSegment.from_file(audio_file_path)
    chunks = split_on_silence(sound,
                              min_silence_len=500,
                              silence_thresh=sound.dBFS - 14,
                              keep_silence=500,
                              )
    audio_file_path_split_list = audio_file_path.split("/")
    audio_file_name = audio_file_path_split_list[len(audio_file_path_split_list)-1].split(".")[0]
    if not os.path.isdir(audio_chunk_folder_name):
        os.mkdir(audio_chunk_folder_name)
    whole_audio_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(audio_chunk_folder_name, f"{audio_file_name}_{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.WavFile(chunk_filename) as source:
            audio_listened = r.record(source)
        # with sr.AudioFile(chunk_filename) as source:
        #     audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                # print(chunk_filename, ":", text)
                whole_audio_text += text
    # return the text for all chunks detected
    return whole_audio_text


# path = "data/large-audio-files/machine-learning_speech-recognition_7601-291468-0006.wav"
# print("\nFull text:", get_large_audio_transcription(path))
