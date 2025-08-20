import os
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

_ = load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llmModel = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    google_api_key=GEMINI_API_KEY,
    temperature=0.2,
    max_output_tokens=4096
)

for chunk in llmModel.stream("What is the capital of France?"):
    print(chunk.content, end="", flush=True)