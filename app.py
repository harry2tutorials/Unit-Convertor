import streamlit as st

st.set_page_config("UNIT CONVERTOR", layout="wide")

length = {
    "Kilometers":1,   # base
    "meters": 1000
}

weight = {
    "kilograms" : 1, # base
    "grams": 1000
}

def Length_conversion(conversion_from, conversion_to, value):
    from_conversion = length[conversion_from]
    to_conversion = length[conversion_to]

    result = (value/from_conversion) * to_conversion
    st.write(f'result : {result} {conversion_to}')

def Weight_conversion(conversion_from, conversion_to, value):
    from_conversion = weight[conversion_from]
    to_conversion = weight[conversion_to]

    result = (value/from_conversion) * to_conversion
    st.write(f'result : {result} {conversion_to}')



def main():
    st.title("Unit Convertor")
    option = st.selectbox(
    "Select Conversion Type",
    ("Length", "Weight"))

        # length conversion
    if option == "Length":
        conversionFrom = st.selectbox(
        "From",
        ("Kilometers", "meters"))
        
        conversionTo = st.selectbox(
        "To",
        ("Kilometers", "meters"))
        
        values = st.number_input("insert value", min_value= 0.0)

        if st.button("Enter"):
            Length_conversion(conversionFrom, conversionTo, values)
            
        # Weight Conversion
    if option == "Weight":
        conversionFrom = st.selectbox(
        "From",
        ("kilograms", "grams"))
        
        conversionTo = st.selectbox(
        "To",
        ("kilograms", "grams"))
        
        values = st.number_input("insert value", min_value= 0.0)
        if st.button("Enter"):
            Weight_conversion(conversionFrom, conversionTo, values)
            

            
main()