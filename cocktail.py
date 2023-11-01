import streamlit as st
import requests

API_BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1"

def fetch_cocktails_by_name(cocktail_name):
    url = f"{API_BASE_URL}/search.php?s={cocktail_name}"
    response = requests.get(url)
    data = response.json()
    return data["drinks"]

def fetch_cocktails_by_ingredient(ingredient_name):
    url = f"{API_BASE_URL}/filter.php?i={ingredient_name}"
    response = requests.get(url)
    data = response.json()
    return data["drinks"]

def fetch_cocktail_details(cocktail_id):
    url = f"{API_BASE_URL}/lookup.php?i={cocktail_id}"
    response = requests.get(url)
    data = response.json()
    return data["drinks"][0]

def main():
    st.title("Cocktail Recipes")

    cocktail_name = st.text_input("Search cocktails by name:")

    if st.button("Search"):
        if cocktail_name:
            cocktails = fetch_cocktails_by_name(cocktail_name)
            if not cocktails:
                st.error(f"No cocktails found for the name '{cocktail_name}'.")
            else:
                st.subheader(f"Cocktails matching '{cocktail_name}':")
                for cocktail in cocktails:
                    st.write(cocktail["strDrink"])

    ingredient_name = st.text_input("Filter cocktails by ingredient:")

    if st.button("Filter"):
        if ingredient_name:
            cocktails = fetch_cocktails_by_ingredient(ingredient_name)
            if not cocktails:
                st.error(f"No cocktails found with the ingredient '{ingredient_name}'.")
            else:
                st.subheader(f"Cocktails with the ingredient '{ingredient_name}':")
                for cocktail in cocktails:
                    st.write(cocktail["strDrink"])

    selected_cocktail_id = st.text_input("Enter the Cocktail ID to view the recipe:")

    if st.button("View Recipe"):
        if selected_cocktail_id:
            cocktail_details = fetch_cocktail_details(selected_cocktail_id)
            st.subheader(cocktail_details["strDrink"])
            st.image(cocktail_details["strDrinkThumb"], caption=cocktail_details["strDrink"], use_column_width=True)
            st.write("Category:", cocktail_details["strCategory"])
            st.write("Glass:", cocktail_details["strGlass"])
            st.write("Instructions:", cocktail_details["strInstructions"])

if __name__ == "__main__":
    main()
