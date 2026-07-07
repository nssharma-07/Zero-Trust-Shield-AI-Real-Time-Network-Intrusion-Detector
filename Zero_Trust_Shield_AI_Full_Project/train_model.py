import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/network_traffic.csv")

X = df.drop("threat", axis=1)
y = df["threat"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "intrusion_model.pkl")

print("Intrusion detection model trained successfully")