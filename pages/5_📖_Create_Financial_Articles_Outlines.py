import streamlit as st
import call_vertex_api as vapi
import time

st.set_page_config(page_icon="image/usd.ico")

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(vNoLabel, unsafe_allow_html=True)

st.title("Generate Article Outlines and Contents for Financial Topic")

def show_progress():
    with st.spinner('Please wait for my answer...'):
        time.sleep(5)

def article_outline(topic):
    # Prompt
    prompt = f"Act as Financial Consultant and Wealth Advisor, please create an article about {topic}. "
    prompt += "Structure the article with the following format: "
    prompt += "1. Please create an inspiring Title or Headline for the article. Make it clear and concise and it should be attention-grabbing"
    prompt += "2. Create the outlines of the article in bullet points."
    prompt += "3. Then create the article with this format:"
    prompt += """
                Introduction: The lead is the first paragraph of the article, and it should summarize the most important information in the story. The lead should be no more than 3-5 sentences long, and it should answer the basic questions of who, what, when, where, why, and how.
                Content: The body of the article should provide more detail about the story. The body should be divided into paragraphs, and each paragraph should focus on one main point. The body should also include quotes from people involved in the story, as well as facts and statistics.
                Facts and Supporting Information: Provide relevant facts, statistics, or supporting information to back up your statements or claims. This helps strengthen the article's credibility and provides readers with additional contex
                Conclusion: The conclusion should summarize the main points of the article and leave the reader with something to think about. The conclusion should not introduce any new information, and it should be no more than 1-2 paragraphs long.
              """
    # Show Progress Bar
    show_progress()
    # Run LLM model
    response = vapi.generate_text_from_genai_googlevertexapi(prompt)
    # Print results
    return st.info(response)

with st.form("myform"):
    topic_text = st.text_input("Enter the Topic of your Article:", placeholder="ex: What is the value of Bitcoin? Should we buy it now?")
    submitted = st.form_submit_button("Submit")
    if not topic_text:
        st.info("Please add your financial Topic to continue. Ex: Investment, Stock Market, Millenials, Cryptocurrency, Bitcoin, etc")
    elif submitted:
        article_outline(topic_text)