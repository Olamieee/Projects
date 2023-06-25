import streamlit as st
import numpy as np

import joblib

saved_model = joblib.load('C:/Users/Ola/Desktop/320 project/Kentucky_model.joblib')

def predict_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,zipcode,lat,long,sqft_living15,sqft_lot15,tr_year,tr_month,yr_old,renovated_status):

    inputs = [bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,zipcode,lat,long,sqft_living15,sqft_lot15,tr_year,tr_month,yr_old,renovated_status]

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
            background-image: 'C:/Users/Ola/Desktop/320 project/dataset/house.jpg';
            
        }
        </style>
        """,
        unsafe_allow_html=True
            )
        
        html_temp = """
            
            <div style= "background-color:tomato; padding:10px">
            <h2 style ="color:black; text-aligh:center;">Kentucky House Price Prediction</h2> 
            </div>"""

        st.markdown(html_temp,unsafe_allow_html=True)
            

        bedrooms = st.text_input("No of Bedroom(s)")
        bathrooms = st.text_input("No if bathroom(s)") 
        sqft_living = st.text_input("Sqft_living")
        sqft_lot = st.text_input("Sqft_lot")
        floor = st.text_input("Floor(s)")
        waterfront = st.text_input("waterfront(O for NO, 1 for Yes)")
        view = st.selectbox("view",(0,1,2,3,4))
        condition = st.selectbox("condition",(1,2,3,4,5))
        grade = st.selectbox("grade",(1,2,3,4,5,6,7,8,9,10,11,12,13))
        sqft_above = st.text_input("Sqft_above")
        sqft_basement = st.text_input("Sqft_basement")
        zipcode = st.text_input("Zipcode")
        latitude = st.text_input("Latitude")
        longitude = st.text_input('Longitude')
        sqft_living15 = st.text_input("sqft_living15")
        sqft_lot15 = st.text_input("sqft_lot15")
        transaction_year = st.selectbox('Transaction Year',('2014', '2015'))
        transaction_month = st.selectbox('Transaction month',(1,2,3,4,5,6,7,8,9,10,11,12))
        year_old = st.text_input("Year Old")
        renovated_status = st.selectbox("Renovated Status (O for NO, 1 for Yes)", (0,1))


        

        if st.button("Get Price"):
            result = predict_price(bedrooms,bathrooms,sqft_living,sqft_lot,floor,waterfront,view,condition,grade,sqft_above,sqft_basement,zipcode,latitude,longitude,sqft_living15,sqft_lot15,
                                   transaction_year,transaction_month,year_old,renovated_status)
            st.success("Price: ${}".format(result[0]))
            st.balloons()

        else:
            st.error("Please enter values for all input fields.")

        if st.button('About'):
            st.write('House Price Prediction project by Alonge Olamide Samson, CSC/2019/1093 under the supervision of Dr. Adewole')
if __name__ == "__main__":
     main()