from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

# prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words (max words 100)")
# prompt = ChatPromptTemplate.from_template("Explain {topic} to {audience} in simple words")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a strict teacher dont answer other then topic and give in strict and saccasting tone and in 100 words only"),
#     ("human", "Explain {topic} to {audience}")
# ])

#! Chaining multiple steps like summarize then expalin in simple words

prompt = ChatPromptTemplate.from_template("Summarize this text : {text}")

prompt2 = ChatPromptTemplate.from_template("Explain this in simple words : {summary} in 100 words")


chain = prompt | model | prompt2 | model

user_input = input("Enter text for simple explaintion  : ")


result = chain.invoke({
    "text":user_input
    })

print(result.content)