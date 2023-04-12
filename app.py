import numpy as np
import streamlit as st
import pickle

model = pickle.load(open("model.pkl",'rb'))

def predict(inp):
    feature = int(inp)
    feature = [[np.array(feature)]]
    print(feature)
    prediction = model.predict(feature)
    output = round(prediction[0],2)
    res = "Employee Salary should be $ {}".format(output)
    return res

def main():
    st.title("Salary Prediction")
    experience = st.text_input('Years of Experience')
    result = ''

    if(st.button("Predict")):
        result = predict(experience)
    st.success(result)
    
if __name__ == '__main__':
    main()