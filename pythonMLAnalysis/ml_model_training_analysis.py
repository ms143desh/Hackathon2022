import pickle
import time

import pandas as pd
import tensorflow as tf
import app_configuration
import pymongo_database_opterations as pdo


def train_model(retrain_identity):
    print("getting train record from database for identity {}", retrain_identity)
    retrain_request = pdo.get_retrain_record_by_identity(retrain_identity)
    if "dataset_file_name" in retrain_request:
        dataset_file_name = retrain_request["dataset_file_name"]
    if "new_model" in retrain_request:
        new_model = retrain_request["new_model"]
    create_trained_model(retrain_identity, dataset_file_name, new_model)
    pdo.update_retrain_record(retrain_identity)
    print("new retrained model details saved successfully in database!")


def create_trained_model(layer_name_suffix, dataset_file_name, new_model_name):
    print("training for new model started")
    training_dataset_file_path = app_configuration.training_dataset_base_path + dataset_file_name
    model = ml_train_model_with_dataset(layer_name_suffix, training_dataset_file_path)
    print("start saving new model data!")
    # model.save(app_configuration.trained_model_base_path + new_model_name)
    save_trained_model_to_db(model, new_model_name)
    print("trained model data saved successfully!")


def retrain_trained_model(retrain_identity):
    print("getting retrain record from database for identity {}", retrain_identity)
    retrain_request = pdo.get_retrain_record_by_identity(retrain_identity)
    if "dataset_file_name" in retrain_request:
        dataset_file_name = retrain_request["dataset_file_name"]
    if "previous_model" in retrain_request:
        previous_model = retrain_request["previous_model"]
    if "new_model" in retrain_request:
        new_model = retrain_request["new_model"]
    create_retrained_model(retrain_identity, dataset_file_name, previous_model, new_model)
    pdo.update_retrain_record(retrain_identity)
    print("new retrained model details updated successfully in database!")


def create_retrained_model(retrain_identity, dataset_file_name, previous_model_name, new_model_name):
    print("retraining for new model started")
    training_dataset_file_path = app_configuration.training_dataset_base_path + dataset_file_name

    sentiment_label, tokenizer, vocab_size, padded_sequence = ml_read_dataset_for_modelling(training_dataset_file_path)

    model2 = ml_train_model_with_dataset(retrain_identity, training_dataset_file_path)
    # model1 = tf.keras.models.load_model(app_configuration.trained_model_base_path + previous_model_name)
    pickled_model = pdo.load_trained_model_from_db(previous_model_name)
    model1 = pickle.loads(pickled_model)
    print("combining new and previous models")
    combined_model = merge_two_trained_models(model1, model2, padded_sequence, sentiment_label)
    print("start saving new model data!")
    # combined_model.save(app_configuration.trained_model_base_path + new_model_name)
    save_trained_model_to_db(combined_model, new_model_name)
    print("new retrained model data saved successfully!")


# def merge_backup_func(model1, model2, layer_name_suffix, padded_sequence, sentiment_label):
#     model2.add(model1)
#     model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     model2.fit(padded_sequence, sentiment_label[0], validation_split=0.2,
#                        epochs=1, batch_size=32)
#     print(model2.output)
#     model2.summary()
#     return model2

# model_concat = tf.keras.layers.Concatenate([model1.output, model2.output], axis=-1, name=concatenated_layer_name)
# # model_concat = tf.keras.layers.Add()([model1.output, model2.output])
# dense_layer_name = "dense_0_" + layer_name_suffix
# model_concat = tf.keras.layers.Dense(1, activation='sigmoid', name=dense_layer_name)(model_concat)
#
# combined_model = tf.keras.models.Model(inputs=[(model1.input, model2.input)], outputs=model_concat)
# combined_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# combined_model.fit((padded_sequence, padded_sequence), sentiment_label[0], validation_split=0.2,
#                    epochs=1, batch_size=32)
# print(combined_model.output)
# combined_model.summary()
# return combined_model


def merge_two_trained_models(model1, model2, padded_sequence, sentiment_label):
    # for layer in model2.layers:
    #     print("model2 - " + layer.name)
    #
    # for layer in model1.layers:
    #     print("model1 - " + layer.name)
    # concatenated_layer_name = "concatenated_" + layer_name_suffix

    model2.add(model1)
    model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model2.fit(padded_sequence, sentiment_label[0], validation_split=0.2,
               epochs=1, batch_size=32)
    # print(model2.output)
    # model2.summary()
    return model2


def ml_train_model_with_dataset(layer_name_suffix, dataset_file_path):
    sentiment_label, tokenizer, vocab_size, padded_sequence = ml_read_dataset_for_modelling(dataset_file_path)
    embedding_vector_length = 32
    model = tf.keras.models.Sequential()
    embedding_layer = tf.keras.layers.Embedding(vocab_size, embedding_vector_length,
                                                input_length=app_configuration.text_max_length)
    embedding_layer._name = "embedding_" + layer_name_suffix
    model.add(embedding_layer)
    spatial_layer = tf.keras.layers.SpatialDropout1D(0.25)
    spatial_layer._name = "spatial_" + layer_name_suffix
    model.add(spatial_layer)
    lstm_layer = tf.keras.layers.LSTM(50, dropout=0.5, recurrent_dropout=0.5)
    lstm_layer._name = "lstm_" + layer_name_suffix
    model.add(lstm_layer)
    dropout_layer = tf.keras.layers.Dropout(0.2)
    dropout_layer._name = "dropout_" + layer_name_suffix
    model.add(dropout_layer)
    dense_layer = tf.keras.layers.Dense(1, activation='sigmoid')
    dense_layer._name = "dense_" + layer_name_suffix
    model.add(dense_layer)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # print(model.summary())

    model.fit(padded_sequence, sentiment_label[0], validation_split=0.2, epochs=1,
              batch_size=32)
    return model

    # plt.plot(history.history['accuracy'], label='acc')
    # plt.plot(history.history['val_accuracy'], label='val_acc')
    # plt.legend()
    # plt.show()
    # plt.savefig("Accuracy plot.jpg")
    #
    # plt.plot(history.history['loss'], label='loss')
    # plt.plot(history.history['val_loss'], label='val_loss')
    # plt.legend()
    # plt.show()
    # plt.savefig("Loss plot.jpg")


def ml_read_dataset_for_modelling(dataset_file_path):
    df = pd.read_csv(dataset_file_path)
    df.head()
    # df.columns

    training_df = df[['text', 'sentiment']]
    # print(training_df.shape)
    training_df.head(5)

    training_df = training_df[training_df['sentiment'] != 'neutral']
    # print(training_df.shape)
    training_df.head(5)

    training_df["sentiment"].value_counts()

    sentiment_label = training_df.sentiment.factorize()
    # sentiment_label

    airline_sentiment_text_values = training_df.text.values
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(airline_sentiment_text_values)
    vocab_size = len(tokenizer.word_index) + 1
    encoded_docs = tokenizer.texts_to_sequences(airline_sentiment_text_values)
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(encoded_docs,
                                                                    maxlen=app_configuration.text_max_length)
    return sentiment_label, tokenizer, vocab_size, padded_sequence


def save_trained_model_to_db(model, model_name):
    pickled_model = pickle.dumps(model)
    model_coll_doc = {model_name: pickled_model, "name": model_name, "created_time": time.time()}
    pdo.save_trained_model_to_db(model_coll_doc)

# if __name__ == "__main__":
#     # Get the database
#     trained_model("identity")
