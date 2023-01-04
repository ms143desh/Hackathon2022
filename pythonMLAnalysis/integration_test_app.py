import json
import time

import requests

base_url = "http://localhost:8000"
base_path_integration_test_data = "integration-test-data/"


def integration_test_train_model():
    url = base_url + "/model/train_model"
    payload = {'data': '{"new_model":"default_sentiment_analysis_model"}'}
    files = [('file', (
        'airline_sentiment.csv', open(base_path_integration_test_data + 'airline_sentiment.csv', 'rb'), 'text/csv'))]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)


def integration_test_retrain_model():
    url = base_url + "/model/retrain_model"
    payload = {'data': '{"previous_model":"default_sentiment_analysis_model","new_model":"retrained_model_01"}'}
    files = [('file', (
        'custom_sentiment.csv', open(base_path_integration_test_data + 'custom_sentiment.csv', 'rb'), 'text/csv'))]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)


def integration_test_sentiment_analysis():
    url = base_url + "/analysis/sentiment_analysis"
    payload = json.dumps({"model_to_use": "default_sentiment_analysis_model",
                          "text": "I enjoyed my journey on this flight"})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def integration_test_audio_text_analysis():
    url = base_url + "/analysis/audio_text_analysis"
    payload = {'data': '{"model_to_use":"default_sentiment_analysis_model"}'}
    files = [('file', ('default_small_audio_file.wav',
                       open(base_path_integration_test_data + 'default_small_audio_file.wav', 'rb'), 'audio/wav'))]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)


def integration_test_all_retrain_model():
    url = base_url + "/model/all_retrain_model"
    payload = {}
    files = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    print(response.text)


def integration_test_retrain_model_by_id(identity):
    url = base_url + "/model/retrain_model_by_id?id=" + identity
    payload = {}
    files = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    print(response.text)


if __name__ == "__main__":
    integration_test_train_model()
    time.sleep(120)
    integration_test_retrain_model()
    time.sleep(120)
    integration_test_sentiment_analysis()
    time.sleep(30)
    integration_test_audio_text_analysis()
    integration_test_all_retrain_model()
    integration_test_retrain_model_by_id("6393c65d3c5e0a8d7e484603")


# @mock.patch('app.app_utility.run_train_process', return_value=True)
# def test_train_model(mocker):
#     file_name = "airline_sentiment.csv"
#     file_path = "data/training-dataset/" + file_name
#     file_type = 'application/octet-stream'

# data_list = [encode('Content-Disposition: form-data; name=file; filename={0}'.format(file_name)),
#              encode('Content-Type: {}'.format(file_type))]
# with open(file_path, 'rb') as f:
#     data_list.append(f.read())
#
# data_list = []
# data_list.append(encode('Content-Disposition: form-data; name=param_data;'))
# data_list.append(encode('Content-Type: {}'.format('text/plain')))
# data_list.append(encode("{\"new_model\":\"default_sentiment_analysis_model\"}"))
# body = b'\r\n'.join(data_list)
# payload = body

# headers = {'Content-type': 'multipart/form-data'}

# data = {"file": (open(file_path, 'rb', encoding='utf-8'), file_name),
#         "param_data": {"new_model": "default_sentiment_analysis_model"}}
# payload = {"param_data": {"new_model": "default_sentiment_analysis_model"}}
# print(payload)
# mocker.patch('app.app_utility.upload_file', return_value=True)
# mocker.patch('app.app_utility.run_train_process', return_value=True)
#
# response = app.test_client().post("/model/train_model", data=payload, headers=headers)
# # response = client.post("/model/train_model", data=data)
# assert response.status_code == 200
# assert response.data.decode('utf-8') == 'Testing, Flask!'
