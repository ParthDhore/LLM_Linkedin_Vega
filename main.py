from langchain.llms.huggingface_pipeline import HuggingFacePipeline
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from transformers import BitsAndBytesConfig

nf4_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_use_double_quant=True,
   bnb_4bit_compute_dtype=torch.bfloat16
)

model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
                 model_id,
                 quantization_config=nf4_config
                 )
pipe = pipeline("text-generation", 
               model=model, 
               tokenizer=tokenizer, 
               max_new_tokens=512
               )

hf = HuggingFacePipeline(pipeline=pipe)

query = "What is langchain?"

prompt = f"""
### System:
You are an AI assistant that follows instruction extremely well. 
Help as much as you can. Please be truthful and give direct answers

### User:
{query}

### Response:
"""

response = hf.predict(prompt)
print(response)