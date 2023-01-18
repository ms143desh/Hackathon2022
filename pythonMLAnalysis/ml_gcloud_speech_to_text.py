
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud import storage
import os

# setting Google credential
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcloud-key/google_secret_key.json'


def get_gcloud_bucket_folder_objects(gcloud_bucket, path_prefix):
    gcloud_storage_client = storage.Client()
    gcloud_bucket = gcloud_storage_client.get_bucket(gcloud_bucket)
    # bucket_blobs_iterator = gcloud_bucket.list_blobs(prefix=path_prefix)
    bucket_blobs_list = list(gcloud_bucket.list_blobs(prefix=path_prefix))
    # print(bucket_blobs_list)
    # for blob in bucket_blobs_list:
    #     print(blob.name)
    #     print(blob.bucket.name)
    return bucket_blobs_list


# function that splits the audio file into chunks and applies speech recognition
def get_gcloud_speech_transcription(audio_file_path):
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    # gcs_uri = "gs://ml-workshop-poc/audio-files/sample-0.mp3"
    gcs_uri = audio_file_path
    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    whole_audio_text = ""
    for result in response.results:
        result_transcript = result.alternatives[0].transcript
        whole_audio_text += result_transcript
        print("Transcript: {}".format(result_transcript))
    return whole_audio_text


# get_gcloud_bucket_folder_objects("ml-workshop-poc", "audio-files/")
# get_gcloud_speech_transcription("gs://ml-workshop-poc/audio-files/machine-learning_speech-recognition_16-122828-0002"
#                                 ".wav")
# get_gcloud_speech_transcription("gs://ml-workshop-poc/audio-files/1-text-to-speech.mp3")
# get_gcloud_speech_transcription("gs://ml-workshop-poc/audio-files/2-text-to-speech.mp3")
# get_gcloud_speech_transcription("gs://ml-workshop-poc/audio-files/3-text-to-speech.mp3")

