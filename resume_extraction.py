from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


from app import llm

loader = PyPDFLoader("./raghav_vinayak_dadhich.pdf")
pages = loader.load()
text=pages[0].page_content

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=600,chunk_overlap=90)
docs=text_splitter.split_documents(pages)


PROFILE_PROMPT_TEMPLATE="""
From the Resume text provided for a job aspirant, extract the Entity as instructed below.
Instructions:
1. Extract the name of the person, description of the person, relevant social media links for the person.

The Description SHOULD NOT exceed more than 30 words.
Question: Now, extract the Person description for the text below -
{text}
Answer:
"""

SKILLS_PROMPT_TEMPLATE="""
From the Resume text provided for a job aspirant, extract the Entity as instructed below.
Instructions:
1. Extract the relevant  technical and personal skills from the text that would help the person get a job.

Question: Now, extract the Skill details for the text below -
{text}
Answer:
"""

COMPANIES_PROMPT_TEMPLATE="""
From the Resume text provided for a job aspirant, extract the Entity as instructed below.
Instructions:
1. Extract the companies the person has worked, the role of the person and time/year the person has worked for in from the text.
Question: Now, extract the Company details for the text below -
{text}
Answer:
"""

EDUCATION_PROMPT_TEMPLATE="""
From the Resume text provided for a job aspirant, extract the Entity as instructed below.
Instructions:
1. Extract the Education level the person has , Name of the school or college, Percentage/Marks/GPA achieved in the respective college, year of school/college.
Question: Now, extract the Educational details of the person for the text below -
{text}
Answer:
"""

PROJECT_PROMPT_TEMPLATE="""
From the Resume text provided for a job aspirant, extract the Entity as instructed below.
Instructions:
1. Extract the  Title of the Projects the person has worked on and give the description of the project in NOT MORE THAN 30 words.
Question: Now, extract the Project details for the text below -
{text}
Answer:
"""

def get_entities(template):
    prompt=PromptTemplate(
        input_variables=['text'],template=template
    )

    llm_chain=LLMChain(llm=llm,prompt=prompt)
    res=llm_chain({"text":text})
    return res

entities=[PROFILE_PROMPT_TEMPLATE,SKILLS_PROMPT_TEMPLATE,COMPANIES_PROMPT_TEMPLATE,EDUCATION_PROMPT_TEMPLATE,PROJECT_PROMPT_TEMPLATE]

results={"profile":"","skills":"","companies":"","education":"","project":""}


results['profile']=get_entities(entities[0])

for res,entity in zip(results.items(),entities):
    results[res[0]]=get_entities(entity)['text'].split("\nAnswer")[1]


print(results)