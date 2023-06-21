# Langchain with OPENAI API
This code integrates the OpenAI API with the Langchain framework. It uses Streamlit for creating a user interface to interact with the code.

## Requirements
* Python 3.x
* Streamlit
* Langchain
* OpenAI

## Installation
1. Clone the repository.
2. Install the required dependencies by running the following command:
```pip install -r requirements.txt```

## Usage
Set the OpenAI API key by assigning it to the `openai_api_key` variable in the `constants.py` file.
Run the code using the following command:
```streamlit run main.py```

Access the Streamlit application through your web browser.
Enter the name of the celebrity you want to search in the provided text input.

## Code Explanation
The OpenAI API key is set as an environment variable.

1. The Streamlit application is created with a title and a text input field for entering the celebrity name.
2. Conversation buffer memories are defined to store the chat history for different inputs (name, person, dob, description).
3. Prompt templates are created for generating prompts dynamically based on the input variables.
4. The OpenAI language model (LLM) is initialized with a temperature of 0.8.
5. Three LLM chains are created, each using a prompt template, the OpenAI LLM, and a specific memory.
6. A sequential chain is created by combining the three LLM chains. It takes the input variable 'name' and outputs variables 'person', 'dob', and 'description'.
7. If the input text is provided, the parent chain is executed with the input variable 'name' set to the input text. The output is displayed using st.write().
8. The chat histories stored in the conversation buffer memories are displayed in expandable sections using st.expander() and st.info().
9. Feel free to explore the code and modify it according to your needs!

![output image](D:\LangChain\celebrity-search-application\output.png)