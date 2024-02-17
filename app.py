from langchain.llms.huggingface_hub import HuggingFaceHub
import os
from dotenv import load_dotenv


HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
load_dotenv()
llm = HuggingFaceHub(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", 
    model_kwargs={"temperature": 0.5}
)

query = "What is langchain?"

prompt = f"""
 <|system|>
You are an AI assistant that follows instruction extremely well.
Please be truthful and give direct answers
</s>
 <|user|>
 {query}
 </s>
 <|assistant|>
"""

response = llm.predict(prompt)
print(response)
