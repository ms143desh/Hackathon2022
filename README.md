# Hackathon2022
PeerIslands Hackathon 2022 Repository

# About Projects
This repository includes two projects:
1. [ML Analysis(Python)](https://github.com/ms143desh/Hackathon2022/edit/main/README.md#ml-analysispython)
2. [IntelliJ Plugin(Demo)](https://github.com/ms143desh/Hackathon2022/edit/main/README.md#intellij-plugindemo)

# ML Analysis(Python)
- Project code can be found in this repository - 'pythonMLAnalysis' directory

## Run Commands
- Install following python packages
```
python3 -m pip install virtualenv
python3 -m pip install pandas
python3 -m pip install tensorflow
python3 -m pip install Flask
python3 -m pip install pymongo
python3 -m pip install pydub
```

- Import application using Python IDE
```
virtualenv .
source bin/activate
```

- Start application
```
python app.py
```
## APIs - ML Analysis Application
- ```curl --location --request GET 'http://localhost:8000/model/all_retrain_model'```

- ```curl --location --request GET 'http://localhost:8000/model/retrain_model_by_id?id=63b042d9903fbee4d037bb5c'```

- ```curl --location --request POST 'http://localhost:8000/analysis/sentiment_analysis' --header 'Content-Type: application/json' --data-raw '{"model_to_use": "default_sentiment_analysis_model","text": "I enjoyed my journey on this flight"}'```
- ```curl --location --request POST 'http://localhost:8000/analysis/audio_text_analysis' --form 'file=@"/Users/deshaggarwal/PycharmProjects/pythonMLSentimentAnalysis/data/audio-files/text_to_speech_1670860292317137.wav"' --form 'data="{\"model_to_use\":\"default_sentiment_analysis_model\"}"'```
- ```curl --location --request POST 'http://localhost:8000/model/train_model' --form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/airline_sentiment.csv"' --form 'data="{\"new_model\":\"default_sentiment_analysis_model\"}"'```
- ```curl --location --request POST 'http://localhost:8000/model/retrain_model' --form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/custom_sentiment.csv"' --form 'data="{\"previous_model\":\"default_sentiment_analysis_model\",\"new_model\":\"retrained_model_01\"}"'```

## Instructions
- API will give response using the already trained model.
- Application runs on port 8000
- Update the MongoDB connection url in the app_configuration.py file.
- Train the first default model using API(POST 'http://localhost:8000/model/train_model')
- Schema files are stored in the project directory

# IntelliJ Plugin(Demo)
- Project code can be found in this repository - 'DemoIntellijPlugin' directory

## Run Commands
- Install IntelliJ Java & Kotlin IDE - Community Edition - https://www.jetbrains.com/idea/download/#section=mac
- Download project from this repository
- Import Project as IntelliJ Plugin
- Run gradle intellij task - 'runIde'

## Functionality
- This functionality is divided into two categories
  - Application - Calling APIs of ML Analysis application and showing its response
  - OpenAI - This is an wrapper, calling API for ChatGPT and showing its response
