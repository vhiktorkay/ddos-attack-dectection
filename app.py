import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("best_rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# Feature names used in the model
feature_names = [
    'Total Length of Bwd Packets', 'Fwd Packet Length Max', 'Fwd Packet Length Mean',
    'Bwd Packet Length Max', 'Bwd Packet Length Mean', 'Bwd Packet Length Std',
    'Fwd IAT Min', 'Fwd Header Length', 'Bwd Header Length', 'Bwd Packets/s',
    'Packet Length Mean', 'Packet Length Std', 'Packet Length Variance',
    'Average Packet Size', 'Avg Fwd Segment Size', 'Avg Bwd Segment Size',
    'Fwd Header Length.1', 'Subflow Fwd Bytes', 'Init_Win_bytes_forward', 'Init_Win_bytes_backward'
]

# Class labels mapping
class_mapping = {
    0: 'BENIGN',
    1: 'Bot',
    2: 'BruteForce',
    3: 'DoS',
    4: 'Infiltration',
    5: 'PortScan',
    6: 'WebAttack'
}

# Create a dictionary to store user input
user_input = {}

# Streamlit UI
st.title("Network Traffic Classifier")

# Collect user input for each feature
for feature in feature_names:
    user_input[feature] = st.number_input(f"{feature}:", min_value=0.0, max_value=100000.0, value=0.0)


# Predict button
if st.button("Predict"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame([user_input])

    # Make a prediction
    prediction = model.predict(input_data)

    # Map the numeric prediction to the corresponding class label
    predicted_class = class_mapping.get(prediction[0], 'Unknown')

    # Display the prediction
    st.subheader("Prediction:")
    st.success(f"Predicted Class: {predicted_class}")
