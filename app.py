from flask import Flask, request, render_template
import nltk
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

dataset = pd.read_csv('spam.csv', encoding='latin-1')
sent = dataset.iloc[:, [1]]['v2']
label = dataset.iloc[:, [0]]['v1']

le = LabelEncoder()
label = le.fit_transform(label)

stem = PorterStemmer()
sentences = []
for sen in sent:
    senti = re.sub('[^A-Za-z]', ' ', sen)
    senti = senti.lower()
    words = word_tokenize(senti)
    word = [stem.stem(i) for i in words if i not in stopwords.words('english')]
    senti = ' '.join(word)
    sentences.append(senti)

cv = CountVectorizer(max_features=5000)
features = cv.fit_transform(sentences)
features = features.toarray()

feature_train, feature_test, label_train, label_test = train_test_split(features, label, test_size=0.2, random_state=7)

model = MultinomialNB()
model.fit(feature_train, label_train)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    senti = re.sub('[^A-Za-z]', ' ', message)
    senti = senti.lower()
    words = word_tokenize(senti)
    word = [stem.stem(i) for i in words if i not in stopwords.words('english')]
    senti = ' '.join(word)
    features = cv.transform([senti])
    prediction = model.predict(features)
    return render_template('index.html', prediction='SPAM!!!' if prediction == 1 else 'NOT SPAM')

if __name__ == '__main__':
    app.run(debug=True)
