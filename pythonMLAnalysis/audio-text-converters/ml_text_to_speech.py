import time

import playsound as playsound
from gtts import gTTS

import os

text_to_convert = 'This is a good analysis'
language = 'en'

gtts_obj = gTTS(text=text_to_convert, lang=language, slow=False)
text_to_speech_path = "data/audio-files/text_to_speech_" + str(int(time.time() * 1000000)) + ".wav"
gtts_obj.save(text_to_speech_path)

playsound.playsound(text_to_speech_path)
# os.system(text_to_speech_path)
