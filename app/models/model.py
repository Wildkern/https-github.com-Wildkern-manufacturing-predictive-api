import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

def train_model(data: pd.DataFrame):
    X = data[["Temperature", "Run_Time"]]
    y = data["Downtime_Flag"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    return model, {"accuracy": accuracy, "f1_score": f1}

def predict(model, features: dict):
    import numpy as np

    input_features = np.array([[features["Temperature"], features["Run_Time"]]])
    prediction = model.predict(input_features)
    confidence = max(model.predict_proba(input_features)[0])

    return {"Downtime": "Yes" if prediction[0] else "No", "Confidence": confidence}
