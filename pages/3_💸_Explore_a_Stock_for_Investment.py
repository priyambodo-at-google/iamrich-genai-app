#Act as Financial Advisor and Wealth Manager. Your client is interested in GOOG. 
#Please elaborate more on the history of company, latest growth of financial report, and give conclusion and recommendation.

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

st.title("Discover the detail and latest information of a Stock to invest")

def show_progress():
    with st.spinner('Please wait for my answer...'):
        time.sleep(5)

def article_outline(topic):
    # Prompt    
    prompt = f"Act as Financial Consultant and Wealth Advisor, please create a detail explanation article about a {vOpt} for {vText}.   "
    prompt += """
                It's essential to consider both the fundamental aspects of the company and any recent news or updates. Here's a structured approach you can follow:

                Introduction:
                Start by providing a brief overview of the company and its stock symbol.

                Company Background:
                Explain key details about the company, such as its industry, products/services, and market presence. Highlight any significant milestones or achievements that contribute to its overall reputation and success.

                Financial Performance:
                Discuss the company's financial performance, including revenue, profit, and growth trends. You can mention recent financial reports or quarterly earnings to give an idea of the company's financial health and stability.

                Competitive Landscape:
                Analyze the company's position within its industry and discuss its main competitors. Assess how Alphabet Inc. stands out from its competitors and what advantages or challenges it faces in the market.

                Recent News and Updates:
                Provide the latest news or updates related to the company. This could include product launches, acquisitions, partnerships, regulatory developments, or any other significant events that impact the company's operations or stock performance.

                Stock Performance:
                Discuss the historical stock performance of the company, including key metrics such as the stock price, market capitalization, and trading volume. Explain any notable trends, fluctuations, or recent developments that have influenced the stock's performance.

                Analyst Opinions:
                Summarize the viewpoints of financial analysts or experts regarding the company's stock. Highlight any upgrades, downgrades, or target price revisions provided by reputable analysts. Mention consensus estimates and the overall sentiment in the investment community.

                Risks and Challenges:
                Identify potential risks and challenges that Alphabet Inc. may face. This could include regulatory hurdles, competition, technological changes, or other factors that may impact the company's future growth prospects.

                Conclusion:
                Summarize the key points discussed and provide an overall assessment of the company's stock. Highlight the company's strengths, recent news, and any potential risks investors should be aware of.

                Call to Action:
                Inform the current price of the stock per-latest date (inform the date) and Make a recommendation whether to buy or not to buy the stock right now.

                Remember to update the information regularly as news and events unfold to keep your audience informed with the most up-to-date information.
             """

    # Show Progress Bar
    show_progress()
    # Run LLM model
    response = vapi.generate_text_from_genai_googlevertexapi(prompt)
    # Print results
    return st.info(response)

with st.form("myform1"):
    col1, col2 = st.columns(2)
    with col1:
        vOpt_options = ['Company Name', 'Stock Exchange Code/Symbol']
        vOpt = st.selectbox('Choose the type of information you want to extract:', vOpt_options)
    with col2:
        vText = st.text_input('Enter the name of the company or the company symbol:')
    submitted = st.form_submit_button("Submit")
    if not vText:
        st.info("Please enter your company name or symbol.")
    elif submitted:
        article_outline(vText)