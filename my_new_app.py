import streamlit as st
import pandas as pd 
#from streamlit.proto.Selectbox_pb2 import Selectbox 
def main():
    st.title('My Calculator')
    first_number = st.text_input("Enter your first number: ")
    first_number = int(first_number)
    second_number = st.text_input("Enter your second number: ")
    second_number = int(second_number)
    operation_box = st.selectbox('Select the operation: ', ['Addition', 'Substraction'])
    operation(operation_box, first_number, second_number)
    st.image('background.png')
    st.header('This is the Pokemon List')
    df = pd.read_excel('Pokemon_data.xlsx')
    st.dataframe(df.iloc[1])
    

def operation(selection, x, y):
    if st.button('Perform Operation'):
        if selection == 'Addition':
            result = x + y
            st.success(f'Your result is: {result}')

        elif selection == 'Substraction':
            result = x - y
            st.success(f'Your result is: {result}')

#st.markdown(result)
#st.header('Second title')
#st.markdown("I don't know what to do with this")


main()