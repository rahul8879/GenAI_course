import pickle
import pandas as pd
with open("knn_model_v1.pkl", "rb") as f:
    model_v1 = pickle.load(f)

with open("knn_model.pkl", "rb") as f:
    model_v2 = pickle.load(f)


# new customer data
new_data = pd.DataFrame({
    'cibil_score': [400],
    'income': [45000],
    # add all features used in training
})

predictions_v1 = model_v1.predict(new_data)
print(predictions_v1)

predictions_v2 = model_v2.predict(new_data)
print(predictions_v2)

# windsurf