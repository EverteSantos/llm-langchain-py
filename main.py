from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto do usuário para {language}."),
    ("human", "{texto}")
])

parser = StrOutputParser()

chain = prompt | llm | parser

resposta = chain.invoke({"language": "Alemão", "texto": "Primeira LLM criada"})

print(resposta)