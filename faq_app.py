import streamlit as st
import requests


# ---------------------------------------
# FastAPI URL
# ---------------------------------------

FASTAPI_URL = "https://processors-finished-dietary-stainless.trycloudflare.com/question"


# ---------------------------------------
# Streamlit UI
# ---------------------------------------

st.title("Clothing FAQ Chatbot")

st.write("Ask a question about clothing orders.")


question = st.text_input(
    "Ask your question:"
)


# ---------------------------------------
# Send question to FastAPI
# ---------------------------------------

if st.button("Ask"):

    if question.strip():

        response = requests.get(
            FASTAPI_URL,
            params={
                "question": question
            },
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Answer")

            st.write(result["answer"])

            st.write(
                "Matched FAQ:",
                result["matched_faq_question"]
            )

            st.write(
                "Similarity Score:",
                result["similarity_score"]
            )

        else:

            st.error(
                f"FastAPI Error: {response.status_code}"
            )

    else:

        st.warning("Please enter a question.")
