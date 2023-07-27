import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("log_model_loan.joblib")


def main():
    # Set the app title and header using Markdown
    st.markdown("<h1 style='text-align: center; color: #ff9900;'>Loan Approval Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Enter the applicant's details to predict loan approval</h2>", unsafe_allow_html=True)

    # Add input fields for the features with CSS styling
    gender = st.selectbox("Gender", ["Male", "Female"], format_func=lambda x: "Select an option" if x == "" else x, key="gender", help="Select the gender")
    married = st.selectbox("Marital Status", ["Single", "Married"], format_func=lambda x: "Select an option" if x == "" else x, key="married", help="Select the marital status")
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"], format_func=lambda x: "Select an option" if x == "" else x, key="dependents", help="Select the number of dependents")
    education = st.selectbox("Education", ["Graduate", "Not Graduate"], format_func=lambda x: "Select an option" if x == "" else x, key="education", help="Select the education level")
    self_employed = st.selectbox("Self Employed", ["No", "Yes"], format_func=lambda x: "Select an option" if x == "" else x, key="self_employed", help="Select if the applicant is self-employed")
    applicant_income = st.number_input("Applicant Income", key="applicant_income", help="Enter the applicant's income")
    coapplicant_income = st.number_input("Coapplicant Income", key="coapplicant_income", help="Enter the coapplicant's income")
    loan_amount = st.number_input("Loan Amount", key="loan_amount", help="Enter the loan amount")
    loan_amount_term = st.number_input("Loan Amount Term", key="loan_amount_term", help="Enter the loan amount term")
    credit_history = st.selectbox("Credit History", ["No", "Yes"], format_func=lambda x: "Select an option" if x == "" else x, key="credit_history", help="Select the credit history")
    property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"], format_func=lambda x: "Select an option" if x == "" else x, key="property_area", help="Select the property area")

    # Add predict button with CSS styling
    if st.button("Predict", key="predict_button"):
        # Validate input fields
        if (
            gender == "" or
            married == "" or
            dependents == "" or
            education == "" or
            self_employed == "" or
            applicant_income == 0 or
            coapplicant_income == 0 or
            loan_amount == 0 or
            loan_amount_term == 0 or
            credit_history == "" or
            property_area == ""
        ):
            st.warning("Please fill in all the fields.")
        else:
            # Convert input values to numeric
            gender = 1 if gender == "Male" else 0
            married = 1 if married == "Married" else 0
            dependents = int(dependents[0])
            education = 1 if education == "Graduate" else 0
            self_employed = 1 if self_employed == "Yes" else 0
            credit_history = 1 if credit_history == "Yes" else 0
            
            # Convert property area to numeric
            property_area_mapping = {
                "Rural": 0,
                "Semiurban": 1,
                "Urban": 2
            }
            property_area = property_area_mapping[property_area]

            # Create a dictionary with input values
            input_data = {
                "Gender": [gender],
                "Married": [married],
                "Dependents": [dependents],
                "Education": [education],
                "Self_Employed": [self_employed],
                "ApplicantIncome": [applicant_income],
                "CoapplicantIncome": [coapplicant_income],
                "LoanAmount": [loan_amount],
                "Loan_Amount_Term": [loan_amount_term],
                "Credit_History": [credit_history],
                "Property_Area": [property_area],
            }

            # Create a dataframe from the input data
            input_df = pd.DataFrame(input_data)

            # Convert dataframe to NumPy array
            input_array = input_df.astype(float).values

            # Make predictions using the loaded model
            prediction = model.predict(input_array)[0]

            # Display the prediction result
            if prediction == 0:
                st.error("Loan Application Rejected")
            else:
                st.success("Loan Application Approved")

                st.balloons()


if __name__ == "__main__":
    main()
