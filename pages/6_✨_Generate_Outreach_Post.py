import logging
import streamlit as st
import streamlit.components.v1 as components
import call_vertex_api as vapi

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

st.set_page_config(page_icon="image/usd.ico")

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(vNoLabel, unsafe_allow_html=True)

# Define functions
def generate_text(topic: str="", mood: str="", audience: str=""):
    st.session_state.socmed = ""
    st.session_state.text_error = ""

    if not topic:
        st.session_state.text_error = "Please enter a topic"
        return

    with text_spinner_placeholder:
        with st.spinner("Please wait while your caption is being generated..."):
            mood_prompt = f"{mood} " if mood else ""
            audience_prompt = f"{audience} " if audience else ""
            prompt = f"Act as Financial Consultant and Wealth Advisor. Write a {mood_prompt} social media caption about {topic} for {audience_prompt} audience in less than 280 characters. Don't forget to put some relevant hashtags for this post. \n\n"
            mood_output = f", Mood: {mood}" if mood else ""
            audience_output = f", Mood: {mood}" if mood else ""
            st.session_state.text_error = ""
            st.session_state.socmed = (
                vapi.generate_text_from_genai_googlevertexapi(prompt)
            )
            logging.info(
                f"Topic: {topic}{mood_output}{audience_output}\n"
                f"socmed: {st.session_state.socmed}"
                )

# Configure Streamlit page and state
if "socmed" not in st.session_state:
    st.session_state.socmed = ""
if "text_error" not in st.session_state:
    st.session_state.text_error = ""
if "impactful" not in st.session_state:
    st.session_state.impactful = False

# Force responsive layout for columns also on mobile
st.write(
    """<style>
    [data-testid="column"] {
        width: calc(50% - 1rem);
        flex: 1 1 calc(50% - 1rem);
        min-width: calc(50% - 1rem);
    }
    </style>""",
    unsafe_allow_html=True,
)

# Render Streamlit page
st.title("Generate Social Media Content")
myAppDesc = "Introducing 280 characters of Social Media Content Generator created by our Financial Experts. Our app uses advanced generative AI technology to create automated content, saving you valuable time and effort. Try it today and take your social media game to the next level!"
st.markdown(myAppDesc)

# Create Inputs
vtopic = st.text_input(
    label="1. **Choose the Topic, Subject** (or hashtag) that you would like to generate: (Mandatory)", 
    placeholder="the importance of investing early "),
vmood = st.text_input(
    label="2. **Choose the Mood** (e.g. inspirational, empowered, positive, exciting, concerned, funny, serious, others): (Optional)",
    placeholder="funny"),
vaudience = st.text_input(
    label="3. **Choose the Audience** (e.g. millenial, 20-40 years male or female, teenagers, etc): (Optional)",
    placeholder="millenial",
)

col1, col2 = st.columns(2)
with col1:
    st.session_state.impactful = not st.button(
        label="Generate text",
        type="primary",
        on_click=generate_text,
        args=(vtopic, vmood, vaudience),
    )
with col2:
    vmood="impactful"
    st.session_state.impactful = st.button(
        label="Impactful Mood!",
        type="secondary",
        on_click=generate_text,
        args=(vtopic, vmood, vaudience),
    )
text_spinner_placeholder = st.empty()
if st.session_state.text_error:
    st.error(st.session_state.text_error)
if st.session_state.socmed:
    st.markdown("""---""")
    st.write("This is the generated content base on your request:")
    st.info(st.session_state.socmed)
    col1, col2 = st.columns(2)
    with col1:
        components.html(
            f"""
                <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-size="large" data-text="{st.session_state.socmed}"</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            """,
            height=45,
        )
    with col2:
        st.button(
            label="Regenerate text",
            type="secondary",
            on_click=generate_text,
            args=(vtopic, vmood, vaudience),
        )
    st.markdown("""---""")    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "**Maintained by [@doddipriyambodo](https://twitter.com/doddipriyambodo)**"
        )
    with col2:
        st.write("Hope this app is useful for you!")