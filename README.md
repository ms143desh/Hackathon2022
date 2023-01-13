# Hackathon2022
PeerIslands Hackathon 2022 Repository

## Project Blogs
https://mohit-talniya.hashnode.dev/a-case-for-ml-platform-on-mdb-atlas-part-1<br/>
https://medium.com/@ms143desh/integrating-ml-solutions-with-mongodb-30a846a626db

## Linked Repositories
https://github.com/SuperMohit/ml-models<br/>
https://github.com/SuperMohit/mongo-ai-ui

## About Projects
This repository includes two projects:
1. [ML Analysis](https://github.com/ms143desh/Hackathon2022#ml-analysis)<br/>
  a. [Deployment & Run commands](https://github.com/ms143desh/Hackathon2022#deployment--run-commands)<br/>
  b. [APIs - ML Analysis Application](https://github.com/ms143desh/Hackathon2022#apis---ml-analysis-application)<br/>
  c. [Instructions](https://github.com/ms143desh/Hackathon2022#instructions)<br/>
2. [IntelliJ Plugin](https://github.com/ms143desh/Hackathon2022#intellij-plugin)<br/>
  a. [Run Commands](https://github.com/ms143desh/Hackathon2022#run-commands)

## Project Architecture
<img width="731" alt="image" src="https://user-images.githubusercontent.com/19534198/212213814-7a3f4a97-db11-4db4-a2c5-280de492bf88.png">

## ML Analysis
- Project code can be found in this repository - 'pythonMLAnalysis' directory
- Project code is written in Python programming language
- This project structure (functionality) is divided into two parts:
  1. ***ML Model training(based on python code)***
  2. ***APIs to train/retrain ML models and anlysis of text and audio files***

- It provides the functionality based on ML trained models to do the sentiment analysis for text, collection specified fields and audio text.
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
4. Start application - ```sudo python3 app.py```

### APIs - ML Analysis Application
- ```curl --location --request GET 'http://localhost:80/model/all_retrain_model'```

- ```curl --location --request GET 'http://localhost:80/model/retrain_model_by_id?id=63b042d9903fbee4d037bb5c'```

- ```curl --location --request POST 'http://localhost:80/analysis/sentiment_analysis' --header 'Content-Type: application/json' --data-raw '{"model_to_use": "default_sentiment_analysis_model","text": "I enjoyed my journey on this flight"}'```

- ```curl --location --request POST 'http://localhost:80/analysis/collection_text_analysis' --header 'Content-Type: application/json' --data-raw '{"model_to_use": "default_sentiment_analysis_model","input_ns": "sample-data","text_field": "input","output_ns": "sample-data"}'```

- ```curl --location --request POST 'http://localhost:80/analysis/audio_text_analysis' --form 'file=@"/Users/deshaggarwal/PycharmProjects/pythonMLSentimentAnalysis/data/audio-files/text_to_speech_1670860292317137.wav"' --form 'data="{\"model_to_use\":\"default_sentiment_analysis_model\"}"'```

- ```curl --location --request POST 'http://localhost:80/model/train_model' --form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/airline_sentiment.csv"' --form 'data="{\"new_model\":\"default_sentiment_analysis_model\"}"'```

- ```curl --location --request POST 'http://localhost:80/model/retrain_model' --form 'file=@"/Users/deshaggarwal/work/Hackathon/2022/custom_sentiment.csv"' --form 'data="{\"previous_model\":\"default_sentiment_analysis_model\",\"new_model\":\"retrained_model_01\"}"'```

- ***Note*** - On Google Cloud Platform (GCP), ```http://localhost:80/analysis/audio_text_analysis``` gives conflicting error with Google Cloud Speech API. Make changes in code accordingly for GCP.

### Instructions
- API will give response using the already trained model.
- By default, application runs on port 80 and is enabled to be accessed from all IPv4 addresses
- Update the MongoDB connection url in the app_configuration.py file.
- Train the first default model using API(POST 'http://localhost:80/model/train_model')
- Schema files are stored in the project directory

## IntelliJ Plugin
- Project code can be found in this repository - 'DemoIntellijPlugin' directory
- Project code is written using Java & Kotlin programming language
- This projects functionality is divided into two sections:
  - ***ML Application APIs - Calling APIs of ML Analysis application and showing its response***
  - ***OpenAI (ChatGPT) - This is a wrapper, calling API for ChatGPT and showing its response***

### Run Commands
- Install IntelliJ Java & Kotlin IDE - Community Edition - https://www.jetbrains.com/idea/download/#section=mac
- Download project from this repository
- Import Project as IntelliJ Plugin
- Run gradle intellij task - 'runIde'
