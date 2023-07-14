from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

# Create function to call Generative AI from Vertex AI
def generate_text_from_genai_googlevertexapi(prompt: str=""):
    prompt = prompt.strip().replace('"',"")
    parameters = {
        "temperature": 0.2,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.                  
        }
    model = TextGenerationModel.from_pretrained("text-bison@latest")
    response = model.predict(
        prompt,
        **parameters,
    )
    msg = response.text
    return msg

def generate_chat_from_genai_googlevertexapi(prompt):

    context = "Act as a Financial Advisor, your name is IamRich. "
    context += "You are an Investment Expert and Wealth Manager consultant, very knowledgeable about financial industry especially investing in stock market. "

    examples = [
           InputOutputTextPair(
               input_text="How to be rich in a very short answer?",
               output_text="Gain valuable skills, work hard, and make smart investments.",
           ),
       ]

    prompt = prompt.strip().replace('"',"")
    model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.2,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 512,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.              
        }
    chat = model.start_chat(
        context=context,
        examples=examples,
        **parameters
    )
    response = chat.send_message(prompt)
    msg = {"role": "assistant", "content": response.text}
    return msg 

#--- Basic Chat Bison Implementation ---#
def f_chatbison_basic(prompt):
    chat_model = ChatModel.from_pretrained("chat-bison@latest")
    chat = chat_model.start_chat()
    print(
        chat.send_message(
            """
            Hello! Can you write a 300 word abstract for a research paper I need to write about the impact of AI on society?
            """
        )
    )
    print(
        chat.send_message(
            """
            Could you give me a catchy title for the paper?
            """
        )
    )

def f_chatbison_advanced(prompt):
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat(
        context="My name is Ned. You are my personal assistant. My favorite movies are Lord of the Rings and Hobbit.",
        examples=[
            InputOutputTextPair(
                input_text="Who do you work for?",
                output_text="I work for Ned.",
            ),
            InputOutputTextPair(
                input_text="What do I like?",
                output_text="Ned likes watching movies.",
            ),
        ],
        temperature=0.3,
        max_output_tokens=200,
        top_p=0.8,
        top_k=40,
    )
    print(chat.send_message("Are my favorite movies based on a book series?"))
    print(chat.send_message("When where these books published?"))

#--- Basic Text Bison Implementation ---#
def f_textbison_execute(prompt):
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")
    temp_val = 1.0
    max_output_tokens_val = 500
    top_p_val = 1.0
    top_k_val = 40
    response = generation_model.predict(
        prompt=prompt,
        max_output_tokens=max_output_tokens_val,
        temperature=temp_val,
        top_p=top_p_val,
        top_k=top_k_val
    )
    return response.text

def f_textbison_print(prompt):
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")
    #1
    print("1")
    prompt = "What is a large language model?"
    response = generation_model.predict(prompt=prompt)
    print(response.text)
    #2
    prompt = """Create a numbered list of 10 items. Each item in the list should be a trend in the tech industry. 
             Each trend should be less than 5 words.""" 
    response = generation_model.predict(prompt=prompt)
    print(response.text)
    #3
    my_industry = "tech" 
    response = generation_model.predict(
    prompt=f"""Create a numbered list of 10 items. Each item in the list should 
            be a trend in the {my_industry} industry.     
            Each trend should be less than 5 words."""
    )
    print(response.text)
    #4
    temp_val = 0.0
    prompt_temperature = "Complete the sentence: As I prepared the picture frame, I reached into my toolkit to fetch my:"
    response = generation_model.predict(
        prompt=prompt_temperature,
        temperature=temp_val,
    )
    print(f"[temperature = {temp_val}]")
    print(response.text)
    #5
    temp_val = 1.0
    response = generation_model.predict(
    prompt=prompt_temperature,
    temperature=temp_val,
    )
    print(f"[temperature = {temp_val}]")
    print(response.text)
    #6
    max_output_tokens_val = 5
    response = generation_model.predict(
        prompt="List ten ways that generative AI can help improve the online shopping experience for users",
        max_output_tokens=max_output_tokens_val,
    )
    print(f"[max_output_tokens = {max_output_tokens_val}]")
    print(response.text)
    #7 
    max_output_tokens_val = 500
    response = generation_model.predict(
        prompt="List ten ways that generative AI can help improve the online shopping experience for users",
        max_output_tokens=max_output_tokens_val,
    )
    print(f"[max_output_tokens = {max_output_tokens_val}]")
    print(response.text)
    #8 
    top_p_val = 0.0
    prompt_top_p_example = (
        "Create a marketing campaign for jackets that involves blue elephants and avocados."
    )
    response = generation_model.predict(
        prompt=prompt_top_p_example, temperature=0.9, top_p=top_p_val
    )
    print(f"[top_p = {top_p_val}]")
    print(response.text)
    #9 
    top_p_val = 1.0
    response = generation_model.predict(
        prompt=prompt_top_p_example, temperature=0.9, top_p=top_p_val
    )

    print(f"[top_p = {top_p_val}]")
    print(response.text)
    #10 
    prompt_top_k_example = "Write a 2-day itinerary for France."
    top_k_val = 1
    response = generation_model.predict(
        prompt=prompt_top_k_example, max_output_tokens=300, temperature=0.9, top_k=top_k_val
    )
    print(f"[top_k = {top_k_val}]")
    print(response.text)
    #11 
    top_k_val = 40
    response = generation_model.predict(
        prompt=prompt_top_k_example,
        max_output_tokens=300,
        temperature=0.9,
        top_k=top_k_val,
    )
    print(f"[top_k = {top_k_val}]")
    print(response.text)
