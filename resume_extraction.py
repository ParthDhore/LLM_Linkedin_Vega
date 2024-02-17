from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
# from app import llm

loader = PyPDFLoader("./raghav_vinayak_dadhich.pdf")
pages = loader.load()
print(pages[0].page_content)

PROFILE_PROMPT_TEMPLATE="""From the Resume text for a job aspirant below, extract Entities strictly as instructed below.
Instructions:
1. First, look for the Person Entity type in the text and extract the needed information defined below:
    Extract the details from the given text based on the mention entity types.
    Entity Types:
    label:'Person',role:string,description:string
    label: 'Skills',  'names':string
    label: 'Education', 'Name':string, 'Duration':string
    label: 'Projects', 'Title':string, 'Description':string 
    label: 'Position', 'Company':string, 'Duration':string,'roles':string

    For the above entity types, make sure of the following:
    1. For the label Position, Duration is given as string, but try to calculate the difference of the (dates/years/months).
    
2. Description property should be a crisp text summary and MUST NOT be more than 60 characters
3. If you cannot find any information on the entities above, it is okay to return empty value. DO NOT create fictious data.
4. Do NOT create duplicate entities
5. Restrict yourself to the above Person, Position, Company, Education and Skill information.
6. NEVER Impute missing values

Question: Now, extract the Person details for the text below -
{text}

Answer:
"""

res="""Example Output JSON:
{"entities": [{"label":"Person","id":"person1","role":"Prompt Developer","description":"Prompt Developer with more than 30 years of LLM experience"}]}
"""

# prompt_template = PromptTemplate.from_template(PROFILE_PROMPT_TEMPLATE)
# prompt_template.format(text=pages[0].page_content)



query=""
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

# response = llm.predict(prompt_template)
# print(response)