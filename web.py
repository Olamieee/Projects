import streamlit as st
import numpy as np

# from PIL import Image

import joblib

saved_model = joblib.load('https://github.com/Olamieee/320-project/blob/main/kc.ipynb')


def predict_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,zipcode,yr_old,renovated_status):

    inputs = [bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,zipcode,yr_old,renovated_status]

    # convert the inputs to numpy array
    inputs_to_numpy = np.asarray(inputs,dtype=object)

    reshape_inputs = inputs_to_numpy.reshape(1,-1)

    price = saved_model.predict(reshape_inputs)
    print(price)
    return price



def main():
        
        st.markdown(
        """
        <style>
        body {
            background-image: url('C:/Users/Ola/Downloads/house.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
            )
        
        html_temp = """
            
            <div style= "background-color:tomato; padding:10px">
            <h2 style ="color:black; text-aligh:center;">Kentucky House Price Prediction Website </h2> 
            </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)
            

        bedrooms = st.text_input("No of Bedroom(s)")
        bathrooms = st.text_input("No if bathroom(s)") 
        sqft_living = st.text_input("Sqft_living")
        sqft_lot = st.text_input("Sqft_lot")
        floor = st.text_input("Floor(s)")
        waterfront = st.text_input("waterfront(O for NO, 1 for Yes)")
        view = st.text_input("view")
        condition = st.text_input("condition")
        grade = st.text_input("grade")
        sqft_above = st.text_input("Sqft_above")
        sqft_basement = st.text_input("Sqft_basement")
        zipcode = st.text_input("Zipcode")
        yr_old = st.text_input("Year Old")
        renovated_status = st.text_input("Renovated Status (O for NO, 1 for Yes)")

        

        if st.button("Get Price"):
            result = predict_price(bedrooms,bathrooms,sqft_living,sqft_lot,floor,waterfront,view,condition,grade,sqft_above,sqft_basement,zipcode,yr_old,renovated_status)
            st.success("Price: ${}".format(result[0]))
            st.balloons()

        else:
            st.error("Please enter values for all input fields.")

        if st.button('About'):
            st.write('House Price Prediction project by Alonge Olamide Samson, CSC/2019/1093 under the supervision of Dr. Adewole')
if __name__ == "__main__":
     main()
