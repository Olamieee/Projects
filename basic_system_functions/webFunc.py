import streamlit as st
from PIL import Image
import functions

def main():
    st.title("Awesome System")
    st.write("Welcome to the Awesome System! This system provides various functionalities to perform calculations, process images, and unit conversion.")
    st.write("You can perform calculations by selecting the operation and providing the required numbers. The system can also calculate the average of a list of numbers.")
    st.write("For image processing, you can upload an image and apply operations such as resizing, cropping, applying filters, and flipping horizontally.")
    st.write("For unit conversion, you can convert between different units of length, temperature, and weight.")
    st.write("Feel free to explore and have fun with the Awesome System!")

    # Create a sidebar with options
    st.sidebar.title("Options")
    perform_calculations = st.sidebar.checkbox("Perform Calculations")
    perform_processing = st.sidebar.checkbox("Perform Image Processing")
    perform_conversion = st.sidebar.checkbox("Perform Unit Conversion")

    if perform_calculations:
        st.subheader("Calculations")
        num1 = st.number_input("Enter number 1", value=0.0)
        num2 = st.number_input("Enter number 2", value=0.0)
        operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Power"])

        if st.button("Calculate"):
            result = functions.perform_calculation(num1, num2, operation)
            if result is None:
                st.warning("No result. Please check your input.")
            else:
                st.success("Result: {}".format(result))
                st.balloons()

        # Additional calculation
        number_list = st.text_input("Enter numbers (comma-separated)", "")
        numbers = [float(num) for num in number_list.split(",") if num.strip()]
        average = functions.calculate_average(numbers)
        if average is None:
            st.warning("No average. Please provide valid numbers.")
        else:
            st.info("Average: {:.2f}".format(average))

    if perform_processing:
        st.subheader("Image Processing")
        image_file = st.file_uploader("Upload an image")

        if image_file is not None:
            try:
                image = Image.open(image_file)
                st.image(image, caption="Original Image", use_column_width=True)
                st.write("Image Size: {} x {}".format(image.width, image.height))

                st.subheader("Processing Options")
                resize = st.checkbox("Resize")
                if resize:
                    st.write("Current Image Size: {} x {}".format(image.width, image.height))
                    width = st.number_input("Enter width", value=image.width, min_value=1, max_value=image.width)
                    height = st.number_input("Enter height", value=image.height, min_value=1, max_value=image.height)

                crop = st.checkbox("Crop")
                if crop:
                    st.write("Current Image Size: {} x {}".format(image.width, image.height))
                    left = st.number_input("Enter left coordinate", value=0, min_value=0, max_value=image.width - 1)
                    upper = st.number_input("Enter upper coordinate", value=0, min_value=0, max_value=image.height - 1)
                    right = st.number_input("Enter right coordinate", value=image.width - 1, min_value=left + 1, max_value=image.width)
                    lower = st.number_input("Enter lower coordinate", value=image.height - 1, min_value=upper + 1, max_value=image.height)

                filter_type = st.selectbox("Select filter type", ["Grayscale", "Blur", "Edge", "Sharpen"])

                if st.button("Process Image"):
                    if resize:
                        image = functions.resize_image(image, width, height)

                    if crop:
                        image = functions.crop_image(image, left, upper, right, lower)

                    if filter_type != 'None':
                        image = functions.apply_filter(image, filter_type)

                    st.image(image, caption="Processed Image", use_column_width=True)

                    # Additional image manipulation
                    flipped_image = functions.flip_image(image)
                    st.image(flipped_image, caption="Flipped Image", use_column_width=True)
                    st.balloons()

            except Exception as e:
                st.error("Error processing image: {}".format(str(e)))

    if perform_conversion:
        st.subheader("Unit Conversion")
        value = st.number_input("Enter value", value=0.0)
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin", "cm", "m", "km", "inch", "ft", "yd", "mile", "kg", "g", "lb", "oz"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin", "cm", "m", "km", "inch", "ft", "yd", "mile", "kg", "g", "lb", "oz"])

        if st.button("Convert"):
            if from_unit in ["cm", "m", "km", "inch", "ft", "yd", "mile"]:
                converted_value = functions.convert_length(value, from_unit, to_unit)
                unit_name = "Length"
            elif from_unit in ["kg", "g", "lb", "oz"]:
                converted_value = functions.convert_weight(value, from_unit, to_unit)
                unit_name = "Weight"
            else:
                converted_value = functions.convert_temperature(value, from_unit, to_unit)
                unit_name = "Temperature"

            if converted_value is None:
                st.warning("Invalid conversion. Please check your units.")
            else:
                st.success("Converted value: {:.2f} {} ({})".format(converted_value, to_unit, unit_name))
                st.balloons()

if __name__ == '__main__':
    main()
