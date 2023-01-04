import os
from multiprocessing import Process

from flask import jsonify

import ml_model_training_analysis

allowed_train_dataset_extensions = set(['csv'])
allowed_audio_extensions = set(['wav'])


def validate_train_model_request(input_json):
    if "new_model" not in input_json:
        resp = jsonify({'message': 'new_model field is required'})
        resp.status_code = 400
        return resp


def upload_file(file, filename, upload_folder):
    print(upload_folder + filename)
    file.save(os.path.join(upload_folder, filename))
    resp = jsonify({'message': 'ML model dataset successfully uploaded'})
    resp.status_code = 201
    return resp


def validate_upload_file(request, source):
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if source == "audio":
        if not allowed_audio_file_extension(file.filename):
            resp = jsonify({'message': 'Allowed file types are wav'})
            resp.status_code = 400
            return resp
        elif not allowed_dataset_file_extension(file.filename):
            resp = jsonify({'message': 'Allowed file types are txt, csv'})
            resp.status_code = 400
            return resp


def allowed_dataset_file_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_train_dataset_extensions


def allowed_audio_file_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_audio_extensions


def validate_retrain_model_request(input_json):
    if "previous_model" not in input_json:
        resp = jsonify({'message': 'previous_model field is required'})
        resp.status_code = 400
        return resp
    if "new_model" not in input_json:
        resp = jsonify({'message': 'new_model field is required'})
        resp.status_code = 400
        return resp


def run_train_process(identity):
    retrain_process = Process(target=ml_model_training_analysis.train_model, args=(identity,))
    retrain_process.daemon = True
    retrain_process.start()


def run_retrain_process(identity):
    retrain_process = Process(target=ml_model_training_analysis.retrain_trained_model, args=(identity,))
    # you have to set daemon true to not have to wait for the process to join
    retrain_process.daemon = True
    retrain_process.start()
