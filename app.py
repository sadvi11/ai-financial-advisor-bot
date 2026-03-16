import streamlit as st
from advisor import financial_advice

st.title("AI Financial Advisor Bot")

income = st.number_input("Enter your monthly income")

expenses = st.number_input("Enter your monthly expenses")

goal = st.text_input("Enter your financial goal")

if st.button("Get Financial Advice"):

    advice = financial_advice(income, expenses, goal)

    st.subheader("Financial Recommendation")
    st.write(advice)
