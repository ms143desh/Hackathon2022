# hackathon-2022
PeerIslands Hackathon 2022

# Run Commands
```
Python3 -m pip install virtualenv
Python3 -m pip install pandas
Python3 -m pip install tensorflow
Python3 -m pip install Flask

virtualenv .
source bin/activate
python app.py
```

# API
```
curl --location --request POST 'http://localhost:8000/analysis/sentiment_analysis' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model_to_use": "default_sentiment_analysis_model",
    "text": "i have good experience"
}'

curl --location --request POST 'http://localhost:8000/model/train_model' \
--form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/airline_sentiment.csv"' \
--form 'data="{\"new_model\":\"default_sentiment_analysis_model\"}"'

curl --location --request POST 'http://localhost:8000/model/retrain_model' \
--form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/custom_sentiment.csv"' \
--form 'data="{\"previous_model\":\"default_sentiment_analysis_model\",\"new_model\":\"retrained_model_01\"}"'

curl --location --request GET 'http://localhost:8000/model/all_retrain_model'

curl --location --request GET 'http://localhost:8000/model/retrain_model_by_id?id=6393c65d3c5e0a8d7e484603'

curl --location --request POST 'http://localhost:8000/analysis/audio_text_analysis' \
--form 'file=@"/Users/deshaggarwal/PycharmProjects/pythonMLSentimentAnalysis/data/audio-files/text_to_speech_1670860292317137.wav"' \
--form 'data="{\"model_to_use\":\"default_sentiment_analysis_model\"}"'
```

# Comments
By default, API will give response using the already trained model.
