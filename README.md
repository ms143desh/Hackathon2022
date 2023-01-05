# Hackathon2022
PeerIslands Hackathon 2022 Repository

# About Projects
This repository includes two projects:
1. [ML Analysis(Python)](https://github.com/ms143desh/Hackathon2022#ml-analysispython)<br/>
  a. [Run Commands](https://github.com/ms143desh/Hackathon2022#run-commands)<br/>
  b. [APIs - ML Analysis Application](https://github.com/ms143desh/Hackathon2022#apis---ml-analysis-application)<br/>
  c. [Instructions](https://github.com/ms143desh/Hackathon2022#instructions)<br/>
2. [IntelliJ Plugin(Demo)](https://github.com/ms143desh/Hackathon2022#intellij-plugindemo)<br/>
  a. [Run Commands](https://github.com/ms143desh/Hackathon2022#run-commands-1)

# ML Analysis(Python)
- Project code can be found in this repository - 'pythonMLAnalysis' directory
- This project structure (functionality) is divided into two parts:
  1. ***ML Model training(based on python code)***
  2. ***APIs to train/retrain ML models and anlysis of text and audio files***

- It provides the functionality based on ML trained models to do the sentiment analysis for text and audio files.
- It also has capability to train and retrain the ML models based on custom dataset, provided dataset schema is as defined
- Custom trained and retrained ML models can be used for further analysis
- Al this functionality can be accessed via the exposed APIs

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
- This projects functionality is divided into two sections:
  - ***ML Application APIs - Calling APIs of ML Analysis application and showing its response***
  - ***OpenAI (ChatGPT) - This is a wrapper, calling API for ChatGPT and showing its response***

## Run Commands
- Install IntelliJ Java & Kotlin IDE - Community Edition - https://www.jetbrains.com/idea/download/#section=mac
- Download project from this repository
- Import Project as IntelliJ Plugin
- Run gradle intellij task - 'runIde'
