## FullStack-SMS-Spam-Classifier

## Introduction
This repository contains a comprehensive SMS Spam Classifier web application. The backend is developed with Flask, while the frontend utilizes HTML, CSS, and JavaScript. The application leverages a machine learning model based on Naive-Bayes-Classification-Algorithm, trained on a dataset of SMS messages, to determine whether incoming messages are 'spam' or 'not spam'. Users can enjoy an intuitive interface to input their messages and receive immediate classification results.

## Technologies used
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Machine Learning: scikit-learn, NLTK

## Frontend
The frontend of the application is built with HTML, CSS, and JavaScript. It provides a user-friendly interface where users can input their SMS messages and receive immediate classification results. The design is responsive and intuitive, making it easy for users to interact with the application. The frontend communicates with the backend Flask server through **HTTP requests**, providing a seamless user experience.

## Dataset
The machine learning model is trained on a dataset of SMS messages. You can download the dataset from [here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/download?datasetVersionNumber=1).

## Installation
1. Download the dataset and place it in the project directory.
2. Clone this repository to your local machine.
3. Install the required Python packages using pip:
    ```
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```
    python app.py
    ```

## Usage
1. Open your web browser and navigate to `http://localhost:5000`.
2. Enter your message in the input field and click 'Submit'.
3. The application will display whether the message is 'spam' or 'not spam'.


