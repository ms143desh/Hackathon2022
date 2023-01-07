import datetime
import json
import time
import app_configuration

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

import ml_load_trained_model
import app_utility
import pymongo_database_opterations as pdo
import ml_big_audio_to_text

app = Flask(__name__)


@app.route('/model/train_model', methods=['POST'])
def train_model():
    input_json = json.loads(request.form.get('data'))
    # print("input_json" + input_json)
    app_utility.validate_train_model_request(input_json)
    retrain_response = {"base_model": input_json["new_model"],
                        "new_model": input_json["new_model"],
                        "status": "in_progress",
                        "created": datetime.datetime.utcnow()}
    app_utility.validate_upload_file(request, "dataset")
    file = request.files['file']
    filename = secure_filename(file.filename)
    retrain_response["dataset_file_name"] = filename
    app_utility.upload_file(file, filename, app_configuration.upload_folder)
    identity = pdo.insert_retrain_model(retrain_response)
    retrain_response["id"] = identity
    app_utility.run_train_process(identity)
    return jsonify(retrain_response)


@app.route('/analysis/sentiment_analysis', methods=["POST"])
def sentiment_analysis():
    input_json = request.get_json(force=True)
    model_to_use = input_json["model_to_use"]
    # if "model_to_use" in input_json:
    #     model_to_use = input_json["model_to_use"]
    dict_to_return = {"input": input_json["text"],
                      "model_to_use": model_to_use,
                      "sentiment": ml_load_trained_model.predict_sentiment(input_json["text"], model_to_use),
                      "created": datetime.datetime.utcnow()}
    pdo.insert_sentiment_analysis(dict_to_return)
    return jsonify(dict_to_return)


@app.route('/analysis/audio_text_analysis', methods=["POST"])
def audio_text_analysis():
    input_json = json.loads(request.form.get('data'))
    model_to_use = input_json["model_to_use"]
    app_utility.validate_upload_file(request, "audio")
    file = request.files['file']
    filename = secure_filename(file.filename)
    app_utility.upload_file(file, filename, app_configuration.audio_folder)
    whole_audio_text = ml_big_audio_to_text.get_large_audio_transcription(app_configuration.audio_folder + filename)
    dict_to_return = {"input": whole_audio_text,
                      "model_to_use": model_to_use,
                      "sentiment": ml_load_trained_model.predict_sentiment(whole_audio_text, model_to_use),
                      "created": datetime.datetime.utcnow()}
    pdo.insert_sentiment_analysis(dict_to_return)
    return jsonify(dict_to_return)


@app.route('/model/retrain_model', methods=["POST"])
def retrain_model():
    input_json = json.loads(request.form.get('data'))
    app_utility.validate_retrain_model_request(input_json)
    previous_model = input_json["previous_model"]
    previous_model_details = pdo.get_retrain_record_by_model_name(previous_model)
    retrain_response = {"base_model": previous_model_details["base_model"],
                        "previous_model": previous_model,
                        "new_model": input_json["new_model"],
                        "status": "in_progress",
                        "created": datetime.datetime.utcnow()}
    app_utility.validate_upload_file(request, "dataset")
    file = request.files['file']
    filename = secure_filename(file.filename) + "-" + str(int(time.time() * 1000000))
    retrain_response["dataset_file_name"] = filename
    app_utility.upload_file(file, filename, app_configuration.upload_folder)
    identity = pdo.insert_retrain_model(retrain_response)
    retrain_response["id"] = identity
    app_utility.run_retrain_process(identity)
    return jsonify(retrain_response)


@app.route('/model/all_retrain_model', methods=["GET"])
def get_all_retrain_model():
    return pdo.get_all_retrain_model()


@app.route('/model/retrain_model_by_id', methods=["GET"])
def get_retrain_model_by_id():
    args = request.args
    print(args)
    identity = args.get('id')
    return pdo.get_retrain_record_by_identity(identity)


if __name__ == "__main__":
    # app.run(host="localhost", port=8000, debug=True)
    app.run(host='0.0.0.0', port=80)
