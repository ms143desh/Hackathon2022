import datetime
import logging

import certifi
import pymongo
from pymongo import MongoClient

import app_configuration
import ml_load_trained_model
import pymongo_database_opterations

client = MongoClient(app_configuration.pymongo_connection_string, tlsCAFile=certifi.where())
resume_token = None


def predict_sentiment_inserted_document(inserted_full_document):
    identity = inserted_full_document["_id"]
    input_text = inserted_full_document["input"]
    sentiment = ml_load_trained_model.predict_sentiment(input_text, app_configuration.default_model)
    updated_values = {
        "$set": {"sentiment": sentiment, "model_to_use": app_configuration.default_model,
                 "updated": datetime.datetime.utcnow()}}
    pymongo_database_opterations.update_document(identity, updated_values, app_configuration.sample_data_collection)


def watch_insert_change_stream():
    global resume_token
    change_operation_pipeline = [{'$match': {'operationType': 'insert'}}]
    with client[app_configuration.hackathon_2022_mongodb_database][app_configuration.sample_data_collection] \
            .watch(change_operation_pipeline) as stream:
        for inserted_document in stream:
            predict_sentiment_inserted_document(inserted_document["fullDocument"])
            resume_token = stream.resume_token


def enable_change_stream():
    try:
        print("enabling change stream")
        watch_insert_change_stream()
    except pymongo.errors.PyMongoError:
        if resume_token is None:
            logging.error("Resume token is None")
        else:
            watch_insert_change_stream()


if __name__ == "__main__":
    enable_change_stream()
