from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data = pd.read_csv("data.csv")

def clean_income(income_str):
    if isinstance(income_str, str):
        return float(income_str.replace('₹', '').replace(',', '').strip())
    return income_str

data['income'] = data['income'].apply(clean_income)
X = data.drop("status", axis=1)
y = data["status"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# save it :
import pickle
with open("knn_model_v1.pkl", "wb") as f:
    pickle.dump(model, f)
