# Import Libraries
import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
# Import Model Libraries
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, roc_curve, auc
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


with open('model.pkl', 'rb') as file:
    # Load the pickled object
    loaded_model = pickle.load(file)

# Streamlit app
def predict_text(text):
    prediction = loaded_model.predict([text])
    return "Yes, it's a scam" if prediction[0] == 1 else "No, it's not a scam"

def app():
    st.title("👨‍💻 Text-Base Scam Detection Tool")

    # User input for the subreddit's content
    user_input = st.text_area("Paste the subreddit content here:", height=250)

    # Button to predict
    if st.button("Analyze"):
        result = predict_text(user_input)
        st.write(result)
        
    st.write("Note: The analysis is based on the provided training dataset and may not cover all types of scams accurately. The app is still in beta phase v1.1. 27 Mar 2024")

if __name__ == "__main__":
    app()



