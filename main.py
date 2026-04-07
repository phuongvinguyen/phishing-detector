import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from analyzer.url_checks import extract_features
import sys

def predict_url(url, model):
    features = extract_features(url)
    df = pd.DataFrame([features])[model.feature_names_in_]
    phishing_index = list(model.classes_).index(1)
    prob = model.predict_proba(df)[0][phishing_index]

    if prob > 0.7:
        return "Phishing", prob
    else:
        return "Safe", prob


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Corrected syntax: python main.py <url>")
        sys.exit(1)
    
    input = sys.argv[1]

    df = pd.read_csv("phishing_site_urls.csv")

    print(df.columns)  # debug check

    X = df["URL"].apply(extract_features).apply(pd.Series)
    y = df["Label"].map({
        "good" : 0,
        "bad" : 1
    })

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    print("Accuracy:", model.score(X_test, y_test))

    # test prediction
    result, prob = predict_url(input, model)
    print(f"{input} → {result} ({prob:.2f})")