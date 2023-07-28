import streamlit as st
from joblib import load

# Load the best model
best_model = load('C:/Users/Ola/Desktop/churn/rfc_credit_card.joblib')

# Define the prediction function
def predict_churn(data):
    # Make predictions using the best model
    prediction = best_model.predict(data)
    if prediction[0] == 1:
        return 'The customer is likely to churn.'
    else:
        return 'The customer is likely to stay.'

# Create the web app
def main():
    # Page title and header
    st.title('Churn Modelling')
    st.markdown('<h1 style="text-align: center; color: #FF9C00;">Churn Modelling</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center;">Analyze and Predict Customer Churn</h2>', unsafe_allow_html=True)
    
    # Prediction section
    st.subheader('Predict Customer Churn')
    st.markdown('<p style="font-size: 18px; margin-bottom: 1rem;">Please fill in the following information:</p>', unsafe_allow_html=True)
    
    # Input fields
    credit_score = st.number_input('Credit Score', value=0)
    age = st.number_input('Age', value=0)
    tenure = st.number_input('Tenure', value=0)
    balance = st.number_input('Balance', value=0)
    num_of_products = st.number_input('Number of Products', value=0)
    has_cr_card = st.selectbox('Has Credit Card', ['Yes', 'No'])
    is_active_member = st.selectbox('Is Active Member', ['Yes', 'No'])
    estimated_salary = st.number_input('Estimated Salary', value=0)
    geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
    gender = st.selectbox('Gender', ['Female', 'Male'])

    # Predict button
    predict_button_html = """
    <style>
    #predict-button {
        background-color: #FF9C00;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        cursor: pointer;
        border: none;
    }
    </style>
   
    """
    st.markdown(predict_button_html, unsafe_allow_html=True)
    
    # Prediction result
    if st.button('Predict', key='predict_button'):
        if credit_score == 0 or age == 0 or tenure == 0 or balance == 0 or num_of_products == 0 or estimated_salary == 0:
            st.warning('Please fill in all the fields.')
        else:
            data = [
                credit_score,
                age,
                tenure,
                balance,
                num_of_products,
                1 if has_cr_card == 'Yes' else 0,
                1 if is_active_member == 'Yes' else 0,
                estimated_salary,
                1 if geography == 'Germany' else 0,
                1 if geography == 'Spain' else 0,
                1 if gender == 'Male' else 0
            ]
            result = predict_churn([data])
            st.success(result)
            st.balloons()

if __name__ == '__main__':
    main()
