from sklearn.feature_extraction.text import CountVectorizer
import pickle

def topic_detect(df):
    db1= df["text"]
    with open ('list_1.ob', 'rb') as fp:
        list_1 = pickle.load(fp)
    
    vectorizer = CountVectorizer(max_features = 1420)
    x = vectorizer.fit(list_1)
    tops1 = vectorizer.transform(db1)

    filename = 'topic.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    predictions2_SVM = loaded_model.predict(tops1)
    df["topic"] = predictions2_SVM
    df["topic"].replace(1, "Delay", inplace=True)
    df["topic"].replace(0, "Not Delay", inplace=True)
    return df