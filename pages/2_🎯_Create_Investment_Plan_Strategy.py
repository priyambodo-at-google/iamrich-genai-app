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

st.title("Create Your Investment Plan!")

def show_progress():
    with st.spinner('Please wait for my answer...'):
        time.sleep(5)

def clear_reset():
    st.experimental_rerun()

def create_investment_plan(vTitle, vRisk, vTime, vExperience, vAge, vIncome, vExpense, vProduct):
    # Prompt
    context = "Act as a Financial Advisor, your name is IamRich. "
    context += "You are an Investment Expert and Wealth Manager consultant, very knowledgeable about financial industry especially investing in stock market. "
    context += "Please make an detail investment plan with these characteristic of the person:"

    prompt = f"The person's Financial Goal is {vTitle} ."
    prompt += f"The comfortable Risk tolerance with scale 1 to 5 (1 is the lowest and 5 is the highest risk but possible of higher return) of this person is {vRisk}. "
    prompt += f"The person's investment knowledge and experience is considered as {vExperience}.  "
    prompt += f"The time horizon before the person needs to access the investment funds is {vTime} years. "
    prompt += f"The Age of this person right now is {vAge} years. "
    prompt += f"The average income of this person in USD per-Month? is {vIncome}. "
    prompt += f"The average expense of this person in USD per-Month? is {vExpense}.  "
    prompt += f"The investment preference of this person is {vProduct}. "

    prompt = context + prompt

    # Show Progress Bar
    show_progress()
    # Run LLM model
    response = vapi.generate_text_from_genai_googlevertexapi(prompt)
    # Print results
    st.markdown("""---""")
    print(prompt)
    return st.success(response)

with st.form("myform"):
    vTitle = st.text_input("What is your Financial Goal?", placeholder="save for retirement, a down payment of a house, pay child education, etc")
    col1, col2 = st.columns(2)
    with col1:
        vRisk_options = ['1', '2', '3', '4', '5']
        vRisk = st.selectbox('What is the Risk tolerance you are comfortable with? (scale 1 to 5, highest risk but possible of higher return)', vRisk_options)
    with col2:
        vTime = st.slider('What is the time horizon before you need to access the investment funds? (1 year to 50 years of expected profit)', min_value=1, max_value=50, step=1, value=5)
    col1, col2 = st.columns(2)
    with col1:
        vExperience_options = ['Beginner Investor', 'Advanced Investor', 'Expert Investor']
        vExperience = st.selectbox('What is your investment knowledge and experience?)', vExperience_options)
    with col2:
        vAge = st.slider('What is your Age right now?)', min_value=18, max_value=60, step=1, value=25)
    col1, col2 = st.columns(2)
    with col1:
        vIncome = st.number_input('What is your average income (US$) per-Month?', min_value=100, max_value=1000000, step=100, value=100)
    with col2:
        vExpense = st.number_input('What is your average expense (US$) per-Month?', min_value=100, max_value=1000000, step=100, value=100)
    vProduct = st.text_input("(optional) Enter your investment preference and constraint if any: (ex: I'd prefer stocks and avoid crypto)", placeholder="I prefer to invest in stocks, bonds, real estate but not bitcoin or other cryptocurrency")

    col1, col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button(label="Submit", type="primary")
    # with col2:
    #     clear = st.form_submit_button(label="Clear", type="secondary")

    if not vProduct: vProduct = "I don't have any investment preference. Consider all strategy and investment products"
    if not vTitle and not vRisk and not vTime and not vExperience and not vAge and not vIncome and not vExpense and not vProduct:
        st.info("Please complete your all your answer to create the investment plan ")
    elif submitted:
        create_investment_plan(vTitle, vRisk, vTime, vExperience, vAge, vIncome, vExpense, vProduct)
    # elif clear:
    #     clear_reset()
