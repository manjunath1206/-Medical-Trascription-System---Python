tokens = word_tokenize(text, language='english')


##import os
##import nltk
##import string
##import pandas as pd
##import speech_recognition as sr
##from nltk.corpus import stopwords
##from nltk.tokenize import word_tokenize
##from sklearn.feature_extraction.text import CountVectorizer
##from sklearn.model_selection import train_test_split
##from sklearn.linear_model import LogisticRegression
##
### Ensure necessary NLTK resources are downloaded
##nltk.download('punkt')
##nltk.download('stopwords')
##
### Load dataset
##csv_path = r"E:\Medical Transcription\Medical_transcreption.csv"
##df = pd.read_csv(csv_path)
##
### Text processing function
##def clean_text(text):
##    text = text.lower()
##    text = ''.join([char for char in text if char not in string.punctuation])
##    tokens = word_tokenize(text)
##    tokens = [word for word in tokens if word not in stopwords.words('english')]
##    return ' '.join(tokens)
##
### Apply text cleaning
##df['cleaned_symptoms'] = df['Symptoms'].astype(str).apply(clean_text)
##
### Vectorize text
##vectorizer = CountVectorizer()
##X = vectorizer.fit_transform(df['cleaned_symptoms'])
##
### Split data for training
##X_train, X_test, y_train, y_test = train_test_split(X, df['Disease'], test_size=0.2, random_state=42)
##
### Train model
##model = LogisticRegression(max_iter=1000)
##model.fit(X_train, y_train)
##
### Speech to Text Function
##def speech_to_text():
##    recognizer = sr.Recognizer()
##    with sr.Microphone() as source:
##        print("Adjusting for ambient noise... Please wait.")
##        recognizer.adjust_for_ambient_noise(source)
##        print("Listening... Speak now.")
##        try:
##            audio = recognizer.listen(source)
##            text = recognizer.recognize_google(audio)
##            print("\nYou said: ", text)
##
##            # Predict Disease
##            processed_text = clean_text(text)
##            vectorized_text = vectorizer.transform([processed_text])
##            predicted_disease = model.predict(vectorized_text)[0]
##
##            # Retrieve details from dataset
##            disease_info = df[df['Disease'] == predicted_disease].iloc[0]
##            symptoms = disease_info['Symptoms']
##            treatment = disease_info['Treatment']
##            testings = disease_info['Testings']
##
##            # Print Results
##            print("\nPredicted Disease:", predicted_disease)
##            print(f"Symptoms: {symptoms}")
##            print(f"Recommended Treatment: {treatment}")
##            print(f"Required Testings: {testings}")
##
##        except sr.UnknownValueError:
##            print("Speech Recognition could not understand the audio.")
##        except sr.RequestError as e:
##            print(f"Could not request results from Google Speech Recognition service; {e}")
##
### Run Speech-to-Text
##if __name__ == "__main__":
##    print("Press Enter to start voice input...")
##    input()
##    speech_to_text()
