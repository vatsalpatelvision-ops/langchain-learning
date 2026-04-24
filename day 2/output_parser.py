from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser

load_dotenv()

llm = ChatGroq(
    model = "llama-3.1-8b-instant"
)

# ! Using string parser

# prompt = PromptTemplate.from_template("Explain {topic} in simple words and in 200 words")

# parser = StrOutputParser()

prompt = PromptTemplate.from_template("Explain {topic} and return JSON with: title, explanation, example (this 3 key must be present in json respose). Only return valid JSON. IMP NO TEXT OTHER THEN JSON")

parser = JsonOutputParser()

chain = prompt | llm | parser

response = chain.invoke({"topic" : "python"})

# print(response)
print(type(response))
print(response.get("title","No title found"))