import certifi
from pymongo import MongoClient
import datetime

from bson import ObjectId

import app_configuration


def get_database():
    client = MongoClient(app_configuration.pymongo_connection_string, tlsCAFile=certifi.where())
    return client[app_configuration.hackathon_2022_mongodb_database]


def insert_document(item_json, collection_name):
    identity = str(ObjectId())
    item_json["_id"] = identity
    # print(item_json)
    get_database()[collection_name].insert_one(item_json)
    return identity


def get_retrain_record_by_identity(identity):
    document = get_database()[app_configuration.retrain_model_collection].find_one({'_id': identity})
    return document


def get_retrain_record_by_model_name(previous_model):
    document = get_database()[app_configuration.retrain_model_collection].find_one({'new_model': previous_model})
    return document


def get_collection_all_document(collection_name):
    return list(get_database()[collection_name].find({}))


def get_collection_documents_count(collection_name):
    return get_database()[collection_name].count_documents({})


def get_collection_documents_limit_skip(collection_name, limit, skip):
    return list(get_database()[collection_name].find({}).limit(limit).skip(skip))


def get_collection_cursor(collection_name):
    return get_database()[collection_name].find({}, batch_size=100)


def update_document(identity, updated_values, collection_name):
    get_database()[collection_name].update_one({'_id': identity}, updated_values)


def save_trained_model_to_db(model_coll_doc):
    get_database()[app_configuration.trained_model_data_collection].insert_one(model_coll_doc)


def load_trained_model_from_db(model_name):
    json_data = {}
    model_data = get_database()[app_configuration.trained_model_data_collection].find_one({"name": model_name})
    for field_name in model_data:
        json_data[field_name] = model_data[field_name]
    pickled_model = json_data[model_name]
    return pickled_model


# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     # Get the database
#     insert_items()
