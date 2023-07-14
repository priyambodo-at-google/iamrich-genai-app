import streamlit as st
from vertexai.language_models import TextGenerationModel
import call_vertex_api as vapi
import time

st.set_page_config(page_icon="image/usd.ico")

def show_progress():
    with st.spinner('Please wait for my answer...'):
        time.sleep(5)

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(vNoLabel, unsafe_allow_html=True)

def clear_chat():
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi..., I am a Financial Advisor and Wealth Manager, very knowledgeable about financial industry especially investing in stock market. How can I help you? (ex: Who are you? What are the top 10 best stocks to buy today? How can I be rich?)"}]

st.title("💬 Ask your Financial Questions")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi..., I am a Financial Advisor and Wealth Manager, very knowledgeable about financial industry especially investing in stock market. How can I help you? (ex: Who are you? What are the top 10 best stocks to buy today? How can I be rich?)"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    parameters = {
        "temperature": 0.2,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 512,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.                  
        }
    model = TextGenerationModel.from_pretrained("text-bison@latest")
    context = "Act as a Financial Advisor, your name is IamRich. "
    context += "You are an Investment Expert and Wealth Manager consultant, very knowledgeable about financial industry especially investing in stock market. "
    context += "Please answer this question: "
    prompt = context + prompt
    show_progress()
    response = model.predict(
        prompt,
        **parameters,
    )
    result = response.text

    #result = vapi.generate_text_from_genai_googlevertexapi(prompt)
    #result = vapi.generate_chat_from_genai_googlevertexapi(prompt)

    msg = {"role": "assistant", "content": result}
    st.session_state.messages.append(msg)
    st.chat_message("assistant").markdown(msg["content"])

if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)