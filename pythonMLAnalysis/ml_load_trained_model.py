import pickle

import app_configuration
import tensorflow as tf
import ml_model_training_analysis
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


# test_sentence1 = "I enjoyed my journey on this flight."
# model_to_use_1 = "new_model_01"
# print(predict_sentiment(test_sentence1, model_to_use_1))
#
# test_sentence2 = "This is the worst flight experience of my life!"
# print(predict_sentiment(test_sentence2))
