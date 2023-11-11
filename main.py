import os
import openai
from dotenv import load_dotenv #To read the API Key and can deal with it here!
import streamlit as st

load_dotenv()
#To use openai I must define the API key 
openai.api_key= os.getenv("open_API_key")


#Function to read the files inside data folder 
def load_files():
    text= ""
    #Take the current path and make the join process with data
    data_dir= os.path.join(os.getcwd(), "data") #Best practice to solve sharing problem
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(data_dir, filename), "r") as f: #>>>> "with" will close the file automatically without explicit coding!
                text += f.read()
    return text


def get_response(text):
    prompt= f"""
You are an expert checker in spelling and grammar.
You will be given a text delimited by four backquotes, 
Make sure to check the spelling and the grammar correctly.
If the text is correct, you need only to print No mistakes in the text.
text: ''''{text}''''
    """
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {
                "role":"system",
                "content": prompt,
            },
        ],
    )
    
    return response["choices"][0]["message"]["content"]



def main():

    #Page configuration
    st.set_page_config(
        page_title="Spelling and Grammar checking",
        page_icon="Icon.ico"
    )
    #Header
    st.title("Spelling and Grammar checker")
    st.divider()
    
    user_input= st.text_area("Enter Text", "")

    if st.button("Submit") and user_input !="": #Empty 
            response= get_response(user_input)

            #Disply the summary 
            st.subheader("Checking Result")
            st.markdown(f">{response}")

    else:
            st.error("Please enter text")

    
    
if __name__ == "__main__":
    main()