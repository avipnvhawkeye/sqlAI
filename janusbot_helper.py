import streamlit as st
# Warning control
import warnings
warnings.filterwarnings('ignore')

# from dotenv import find_dotenv, load_dotenv
# load_dotenv(find_dotenv())

import os

#HUGGINGFACEHUB_API_TOKEN="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"

HUGGINGFACEHUB_API_TOKEN=st.secrets["OPENAI_API_KEY"]

from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import chromadb

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature= 0.01,
    token=HUGGINGFACEHUB_API_TOKEN
    )

collection = chromadb.PersistentClient(path="janus.db").get_collection(name="janus_database")

def searchDataByVector(query: str):
    try:
        res = collection.query(
            query_texts=[query],
            n_results=1,
            include=['distances','embeddings', 'documents', 'metadatas'],
        )

    except Exception as e:
        print("Vector search failed : ", e)

    return res


def query_response(user_query:str):

    context=[]
    question=user_query
    #question="Why do we have DEI policy?"

    results=searchDataByVector(question)

    for result in results['documents']:
        context.append(result)
        #print(result)


    template="""You are Janus Chatbot.
                Your creator is Publicis Groupe. 
                Your job is to help publicis employees in identfying the right information related to the Publicis way to behave and to operate.
                You will answer the user question by utilizing the below context.Please be consice and always think harder than you think.
            
    ============
    {context}
    ============

    Now based on the above context, please answer:{question}        

    Your output will always and always be after the format given below. If not then create it in the format given below.

    Output: Your response will start from here...."""

    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    contexts=context[0]

    response=llm_chain.invoke({"question":question,"context":contexts})
    return(response["text"].split("Output: Your response will start from here....")[-1].strip())




