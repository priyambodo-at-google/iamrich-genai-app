import streamlit as st
st.set_page_config(page_icon="image/usd.ico")
vNoLabel = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
html_code = """
    "IamRich" is a cutting-edge personal financial advisor application designed to empower users in managing their finances with intelligence and ease. This innovative app combines smart technology with personalized guidance to provide a comprehensive financial experience.
    """
with st.sidebar:
   st.success("Choose the menu that you would like to explore above 👆")
   st.info("app version: IamRich v1.1-STABLE")
   st.image("image/doddihead.png", width=200)
   st.error("This application is created and maintained by Doddi Priyambodo")

def run():
    st.markdown(vNoLabel, unsafe_allow_html=True)
    st.write("# About IamRich")
    st.subheader("//powered by Google Cloud Generative AI!")
    st.write(html_code)
    st.write(
        """
        **This is the Technical Architecture** of IamRich Application: 
        """
    )
    st.image("image/iamrich-arch.png")
    #st.sidebar.success("Select the use cases that you would like to see above.")

    st.markdown("---")    

if __name__ == "__main__":
    run()
