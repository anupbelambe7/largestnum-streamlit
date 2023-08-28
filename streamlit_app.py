import streamlit as st

st.header("Find Largest Number App")
"""
This application finds the largest among the 3 given numbers
"""
num1 = st.number_input("First Number:",step=1)
num2 = st.number_input("Second Number:",step=1)
num3 = st.number_input("Third Number:",step=1)
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3
st.divider() 
ans = f"""
The largest among the 3 given numbers is **:blue[{largest}]**"""
st.markdown(ans)
st.metric(label="Largest",value=largest)

