# Hackathon2022
PeerIslands Hackathon 2022 Repository

## About Projects
This repository includes two projects:
1. [ML Analysis(Python)](https://github.com/ms143desh/Hackathon2022#ml-analysispython)<br/>
  a. [Deployment & Run commands](https://github.com/ms143desh/Hackathon2022#deployment--run-commands)<br/>
  b. [APIs - ML Analysis Application](https://github.com/ms143desh/Hackathon2022#apis---ml-analysis-application)<br/>
  c. [Instructions](https://github.com/ms143desh/Hackathon2022#instructions)<br/>
2. [IntelliJ Plugin(Demo)](https://github.com/ms143desh/Hackathon2022#intellij-plugindemo)<br/>
  a. [Run Commands](https://github.com/ms143desh/Hackathon2022#run-commands)

## ML Analysis(Python)
- Project code can be found in this repository - 'pythonMLAnalysis' directory
- This project structure (functionality) is divided into two parts:
  1. ***ML Model training(based on python code)***
  2. ***APIs to train/retrain ML models and anlysis of text and audio files***

- It provides the functionality based on ML trained models to do the sentiment analysis for text and audio files.
- It also has capability to train and retrain the ML models based on custom dataset, provided dataset schema is as defined
- Custom trained and retrained ML models can be used for further analysis
- Al this functionality can be accessed via the exposed APIs

### Deployment & Run commands
- ***Note*** - Commands given are as per Debian Linux. For other linux versions, change commands accordingly.
1. Launch VM instance (with Debian Linux)
2. Install Git, Python and Python packages. Use following commands 
```
sudo apt update
sudo apt install git

sudo apt install python3 python3-dev python3-venv
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

sudo python3 -m pip install virtualenv
sudo python3 -m pip install pandas
sudo python3 -m pip install tensorflow --no-cache-dir
sudo python3 -m pip install Flask
sudo python3 -m pip install pymongo
sudo python3 -m pip install pydub
sudo python3 -m pip install SpeechRecognition==1.1.2
```
3. Go to the 'pythonMLAnalysis' directory
4. Start application - ```python3 app.py```

### APIs - ML Analysis Application
- ```curl --location --request GET 'http://localhost:80/model/all_retrain_model'```

- ```curl --location --request GET 'http://localhost:80/model/retrain_model_by_id?id=63b042d9903fbee4d037bb5c'```

- ```curl --location --request POST 'http://localhost:80/analysis/sentiment_analysis' --header 'Content-Type: application/json' --data-raw '{"model_to_use": "default_sentiment_analysis_model","text": "I enjoyed my journey on this flight"}'```

- ```curl --location --request POST 'http://localhost:80/analysis/audio_text_analysis' --form 'file=@"/Users/deshaggarwal/PycharmProjects/pythonMLSentimentAnalysis/data/audio-files/text_to_speech_1670860292317137.wav"' --form 'data="{\"model_to_use\":\"default_sentiment_analysis_model\"}"'```

- ```curl --location --request POST 'http://localhost:80/model/train_model' --form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/airline_sentiment.csv"' --form 'data="{\"new_model\":\"default_sentiment_analysis_model\"}"'```

- ```curl --location --request POST 'http://localhost:80/model/retrain_model' --form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/custom_sentiment.csv"' --form 'data="{\"previous_model\":\"default_sentiment_analysis_model\",\"new_model\":\"retrained_model_01\"}"'```

- ***Note*** - On Google Cloud Platform (GCP), ```http://localhost:80/analysis/audio_text_analysis``` gives conflicting error with Google Cloud Speech API. Please make changes in code accordingly for GCP.

### Instructions
- API will give response using the already trained model.
- By default, application runs on port 80 and is enabled to be accessed from all IPv4 addresses
- Update the MongoDB connection url in the app_configuration.py file.
- Train the first default model using API(POST 'http://localhost:80/model/train_model')
- Schema files are stored in the project directory

## IntelliJ Plugin(Demo)
- Project code can be found in this repository - 'DemoIntellijPlugin' directory
- This projects functionality is divided into two sections:
  - ***ML Application APIs - Calling APIs of ML Analysis application and showing its response***
  - ***OpenAI (ChatGPT) - This is a wrapper, calling API for ChatGPT and showing its response***

### Run Commands
- Install IntelliJ Java & Kotlin IDE - Community Edition - https://www.jetbrains.com/idea/download/#section=mac
- Download project from this repository
- Import Project as IntelliJ Plugin
- Run gradle intellij task - 'runIde'
