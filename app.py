from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = ""   # MUST exist

    if request.method == "POST":
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        previous_grade = float(request.form['previous_grade'])
        extra_curricular = int(request.form['extra_curricular'])

        input_data = np.array([[study_hours, attendance, previous_grade, extra_curricular]])

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            prediction_text = "PASSED ✅"
        else:
            prediction_text = "FAILED ❌"

    # 👇 THIS LINE IS CRITICAL
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
