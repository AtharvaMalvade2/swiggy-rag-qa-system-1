import streamlit as st
from rag_pipeline import ask_question

st.title("Swiggy Annual Report QA System")

st.write("Hey, Ask any question about the Swiggy Annual Report")

query = st.text_input("Enter your question")

if query:
    answer = ask_question(query)

    st.subheader("Answer")
    st.write(answer)