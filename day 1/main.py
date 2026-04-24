from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage
# from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)
# temperature = 0.2
# max_tokens = 2


while True:
    user_input = input("Enter your question : ")

    if user_input.lower() == "exit":
        break
    
    # !normal plain text 
    # response = llm.invoke(user_input)

    # ! Text with roles
    # Clear Instruction + Context + Constraint = Good Output
    response = llm.invoke([
        SystemMessage(content="You are a Strict coding teacher ! only answer quesetions related to coding"),
        HumanMessage(content=user_input)
    ])

    print(f"AI : {response.content}")

# print(response.content)
# print("-"*30)
# print(response.response_metadata)
# print("-"*30)
# print(response.response_metadata)



