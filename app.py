from langchain_community.llms import HuggingFaceHub
import os
from dotenv import load_dotenv


HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
load_dotenv()
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2", 
    model_kwargs={"temperature": 0.5}
)
# mistralai/Mixtral-8x7B-Instruct-v0.1
# mistralai/Mistral-7B-Instruct-v0.2
# query = "What is langchain?"

# prompt = f"""
#  <|system|>
# You are an AI assistant that follows instruction extremely well.
# Please be truthful and give direct answers
# </s>
#  <|user|>
#  {query}
#  </s>
#  <|assistant|>
# """

# response = llm.predict(query)
# print(response)
