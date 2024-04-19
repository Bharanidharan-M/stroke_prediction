import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

def predict_stroke(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    # Prepare input data
    input_data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]])
    
    # Predict stroke probability
    prediction = model.predict_proba(input_data)
    # Return the probability of stroke (second element in the prediction output)
    return float(prediction[0][1])

def main():
    # Streamlit application title
    st.title('Stroke Prediction')

    # Collect user input
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    hypertension = st.radio("Hypertension", ["No", "Yes"])
    heart_disease = st.radio("Heart Disease", ["No", "Yes"])
    ever_married = st.radio("Ever Married", ["No", "Yes"])
    work_type = st.selectbox("Work Type", ["Children", "Govt_job", "Private", "Self-employed", "Never worked"])
    residence_type = st.radio("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0)
    bmi = st.number_input("BMI", min_value=0.0)
    smoking_status = st.selectbox("Smoking Status", ["Never smoked", "Formerly smoked", "Smokes"])

    # Map user input to numeric values
    gender_map = {"Male": 1, "Female": 0}
    hypertension_map = {"No": 0, "Yes": 1}
    heart_disease_map = {"No": 0, "Yes": 1}
    ever_married_map = {"No": 0, "Yes": 1}
    residence_type_map = {"Urban": 0, "Rural": 1}
    work_type_map = {"Children": 0, "Govt_job": 1, "Private": 2, "Self-employed": 3, "Never worked": 4}
    smoking_status_map = {"Never smoked": 0, "Formerly smoked": 1, "Smokes": 2}
    
    # Convert user input to numeric values for prediction
    gender = gender_map[gender]
    hypertension = hypertension_map[hypertension]
    heart_disease = heart_disease_map[heart_disease]
    ever_married = ever_married_map[ever_married]
    residence_type = residence_type_map[residence_type]
    work_type = work_type_map[work_type]
    smoking_status = smoking_status_map[smoking_status]

    # Prediction button
    if st.button("Predict Stroke"):
        try:
            # Make prediction
            probability = predict_stroke(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status)
            
            # Display the probability of stroke
            st.success(f"The probability of having a stroke is {probability:.2%}")
            
            # Provide feedback based on prediction probability
            if probability < 0.5:  # You can adjust this threshold value as needed
                st.warning("Warning: High risk of stroke. Please consult a medical professional.")
            else:
                st.success("You have a low risk of stroke.")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}. Please check your input data and try again.")

if __name__ == '__main__':
    main()
