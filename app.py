import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Prediction")

st.write("Enter student details below:")

# User inputs
study_hours = st.number_input("Study Hours per Week", min_value=0, max_value=50)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100)
previous_grade = st.number_input("Previous Grade (%)", min_value=0, max_value=100)
extra_curricular = st.selectbox(
    "Extra-Curricular Activities",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# Predict button
if st.button("Predict"):
    input_data = np.array([[study_hours, attendance, previous_grade, extra_curricular]])
    prediction = model.predict(input_data)[0]

    # POPUP-STYLE RESULT
    if prediction == 1:
        st.success("🎉 PASSED ✅")
    else:
        st.error("❌ FAILED")

