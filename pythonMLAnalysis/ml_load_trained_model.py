import pickle
import datetime

import app_configuration
import tensorflow as tf
import ml_model_training_analysis
import ml_gcloud_speech_to_text
import pymongo_database_opterations as pdo

sentiment_label, tokenizer, vocab_size, padded_sequence = ml_model_training_analysis \
            .ml_read_dataset_for_modelling(app_configuration.training_dataset_file_path)
# default_trained_model = tf.keras.models.load_model(app_configuration.trained_model_file_path)

dict_of_trained_models = {}
dict_of_read_dataset_variables = {}


def predict_sentiment(text, model_to_use):
    if dict_of_trained_models.get(model_to_use, "empty") == "empty":
        pickled_model = pdo.load_trained_model_from_db(model_to_use)
        trained_model = pickle.loads(pickled_model)
        # trained_model = tf.keras.models.load_model(app_configuration.trained_model_base_path + model_to_use)
        dict_of_trained_models[model_to_use] = trained_model
    else:
        trained_model = dict_of_trained_models.get(model_to_use)

    # if dict_of_read_dataset_variables.get("sentiment_label", "empty") == "empty":
    #     sentiment_label, tokenizer, vocab_size, padded_sequence = ml_model_training_analysis \
    #         .ml_read_dataset_for_modelling(app_configuration.training_dataset_file_path)
    #     dict_of_read_dataset_variables["sentiment_label"] = sentiment_label
    #     dict_of_read_dataset_variables["tokenizer"] = tokenizer
    # else:
    #     sentiment_label = dict_of_read_dataset_variables["sentiment_label"]
    #     tokenizer = dict_of_read_dataset_variables["tokenizer"]

    # print(trained_model_dict)
    tw = tokenizer.texts_to_sequences([text])
    tw = tf.keras.preprocessing.sequence.pad_sequences(tw, maxlen=app_configuration.text_max_length)
    prediction = int(trained_model.predict(tw).round().item())
    return sentiment_label[1][prediction]


def predict_collection_documents(batch_processing, model_to_use, input_ns, text_field, output_ns):
    if batch_processing is False:
        documents_list = pdo.get_collection_all_document(input_ns)
        predict_documents(documents_list, model_to_use, input_ns, text_field, output_ns)
    else:
        limit = 20
        skip = 0
        collection_count = pdo.get_collection_documents_count(input_ns)
        while skip < collection_count:
            batch_documents_list = pdo.get_collection_documents_limit_skip(input_ns, limit, skip)
            skip += limit
            if len(batch_documents_list) == 0:
                break
            else:
                print("next skip ", skip)
                predict_documents(batch_documents_list, model_to_use, input_ns, text_field, output_ns)

        # collection_cursor = pdo.get_collection_cursor(input_ns)
        # while collection_cursor.alive:
        #     batch_documents_list = list(collection_cursor)
        #     if len(batch_documents_list) == 0:
        #         break
        #     else:
        #         predict_documents(batch_documents_list, model_to_use, input_ns, text_field, output_ns)


def predict_documents(documents_list, model_to_use, input_ns, text_field, output_ns):
    for document in documents_list:
        sentiment = predict_sentiment(document[text_field], model_to_use)
        document["sentiment"] = sentiment
        document["model_to_use"] = model_to_use
        if input_ns == output_ns:
            updated_values = {
                "$set": {"sentiment": sentiment, "model_to_use": model_to_use, "updated": datetime.datetime.utcnow()}}
            pdo.update_document(document["_id"], updated_values, app_configuration.sample_data_collection)
        else:
            pdo.insert_document(document, output_ns)


def predict_gcloud_audios(model_to_use, output_ns, gcloud_bucket, path_prefix):
    bucket_blobs_list = ml_gcloud_speech_to_text.get_gcloud_bucket_folder_objects(gcloud_bucket, path_prefix)
    for blob in bucket_blobs_list:
        if not blob.name.endswith("/"):
            gcloud_audio_file_path = "gs://" + blob.bucket.name + "/" + blob.name
            # print(gcloud_audio_file_path)
            whole_audio_text = ml_gcloud_speech_to_text.get_gcloud_speech_transcription(gcloud_audio_file_path)
            sentiment = predict_sentiment(whole_audio_text, model_to_use)
            document = {"sentiment": sentiment, "model_to_use": model_to_use, "input": whole_audio_text, "updated": datetime.datetime.utcnow()}
            pdo.insert_document(document, output_ns)

# test_sentence1 = "I enjoyed my journey on this flight."
# model_to_use_1 = "new_model_01"
# print(predict_sentiment(test_sentence1, model_to_use_1))
#
# test_sentence2 = "This is the worst flight experience of my life!"
# print(predict_sentiment(test_sentence2))
