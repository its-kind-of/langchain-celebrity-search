# Integrate the open ai api
import os
from constants import openai_api_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st


os.environ["OPENAI_API_KEY"] = openai_api_key

# streamlit framework
st.title('Langchain with OPENAI API')
input_text = st.text_input("Search the celebrity you want!")

# Memory
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
description_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# Prompt Templates (Custom)
first_input_prompt = PromptTemplate(
	input_variables=["name"],
	template = "Tell me about celebrity {name}"
)

# OPENAI LLM ENVIRONMENT
llm = OpenAI(temperature=0.8)
chainOne = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)

second_input_prompt = PromptTemplate(
	input_variables=["person"],
	template = "Tell me about celebrity {person}"
)

# OPENAI LLM ENVIRONMENT
chainSecond = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)

third_input_prompt = PromptTemplate(
	input_variables=["dob"],
	template = "Mention 5 Major events happened around {dob} in the world"
)
chainThird = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=description_memory)



parentChain = SequentialChain(chains=[chainOne, chainSecond, chainThird], input_variables=['name'], verbose=True, output_variables=['person', 'dob', 'description'])

if input_text:
	st.write(parentChain({"name": input_text}))

	with st.expander("Person Name"):
		st.info(person_memory.buffer)

	with st.expander('Major Events'):
		st.info(description_memory.buffer)
