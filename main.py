import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from analyzer.url_checks import extract_features
#load dataset
df = pd.read_csv("data.csv")

#extract features
x = df["url"].apply(extract_features).apply(pd.Series)
y = df["label"]

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#train
model = LogisticRegression()
model.fit(x_train, y_train)

#evaluate
print("Accuracy: ", model.score(x_test, y_test))

def predict_url(url, model):
    features = extract_features(url)
    df = pd.DataFrame([features])
    prob = model.predict_proba(df)[0][1]

    if prob > 0.7:
        return "Phishing", prob
    else:
        return "Safe", prob