from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words (max words 100)")

chain = prompt | model

user_input = input("For which topic you need simple explaination in 100 words : ")

result = chain.invoke({"topic":user_input})

print(result.content)