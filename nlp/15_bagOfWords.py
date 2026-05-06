import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

def read_file():
    df =pd.read_csv('email_dataset_10000.csv')
    return df

def preprocess_data(df):
    # Convert the 'label' column to binary values (1 for spam, 0 for ham)
    df['spam'] = df['category'].apply(lambda x: 1 if x == 'spam email' else 0)
    return df

def vectorize_text(x_train, x_test):
    vectorizer = CountVectorizer()
    x_train_vectorized = vectorizer.fit_transform(x_train)
    x_test_vectorized = vectorizer.transform(x_test)
    print("Vocabulary size:", len(vectorizer.vocabulary_))
    print("Sample feature names:", list(vectorizer.vocabulary_.keys())[:10])
    return x_train_vectorized, x_test_vectorized

def query(x_train_vectorized):
    x_train_array = x_train_vectorized.toarray()
    print("Shape of the vectorized training data:", x_train_array.shape)
    print(np.where(x_train_array[0]!=0))

def train_model(x_train_vectorized, y_train):
    model = MultinomialNB()
    model.fit(x_train_vectorized, y_train)
    return model

if __name__ == '__main__':
    df = read_file()
    df = preprocess_data(df)
    print(df.head())

    x_train, x_test, y_train, y_test = train_test_split(df['description'], df['spam'], test_size=0.2)

    print("Training data:", x_train.shape, y_train.shape)

    x_train_vectorized, x_test_vectorized = vectorize_text(x_train, x_test)

    query(x_train_vectorized)

    trained_model = train_model(x_train_vectorized, y_train)

    y_pred= trained_model.predict(x_test_vectorized)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    email =[
        'Congratulations! You have won a $1000 gift card. Click here to claim your prize.'
    ]

    vectorizer = CountVectorizer()
    vectorizer.fit_transform(x_train)
    email_vectorized = vectorizer.transform(email)
    print(trained_model.predict(email_vectorized))


    ##pipeline
    clf = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    clf.fit(x_train, y_train)
    y_pred_pipeline = clf.predict(x_test)
    print("Pipeline Accuracy:", accuracy_score(y_test, y_pred_pipeline))




