import streamlit as st
from streamlit.logger import get_logger
import authrich

authrich.authenticate()
LOGGER = get_logger(__name__)

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
html_code = """
    "IamRich" is a cutting-edge personal financial advisor application designed to empower users in managing their finances with intelligence and ease. This innovative app combines smart technology with personalized guidance to provide a comprehensive financial experience.
    """

def run():
    st.set_page_config(page_icon="image/usd.ico")
    st.markdown(vNoLabel, unsafe_allow_html=True)
    st.write("# 💰 IamRich - Your Smart Personal Financial Advisor application")
    st.subheader("//powered by Google Cloud Generative AI!")
    st.write(html_code)
    st.markdown(
        """
        **👈 Select the menu from the sidebar** to start your experience. 
        """
    )
    st.image("image/IamRich.png")
    #st.sidebar.success("Select the use cases that you would like to see above.")

    st.markdown(
        """
        This application is maintained by Doddi Priyambodo (priyambodo@google.com)   
        v1.0.0
        """
    )
    st.image("image/doddihead.png", width=200)

if __name__ == "__main__":
    run()
