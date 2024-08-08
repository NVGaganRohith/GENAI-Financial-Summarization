from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
import logging

logging.basicConfig(level=logging.INFO)

def create_summary_prompt_template() -> PromptTemplate:
    """Creates a prompt template for generating a one-page summary.

    Returns:
        PromptTemplate: The prompt template.
    """
    template = """
    You are a professional document summariser who has a keen eye for identifying the key details and important points. You are the best at your job.
    Condense the following text to a 400 words with a buffer of 10 words summary without losing key information. Make sure that the entire text fits in a single A4 page.
    Ensure to include the numbers from Business segment overview and geographical segment overview.
    Make sure not to add any '*' or '**' anywhere, and make it look like a clean summary without any headings. Condense as much as info as possible.
    Make sure you give the correct information about the company and any external info that you are giving is accurate.
    context: {context}
    input: {input}
    ANSWER
    """
    return PromptTemplate.from_template(template)

def summarize_text(text: str) -> str:
    """
    Generates a one-page summary of the provided text using OpenAI's GPT-4 model.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The one-page summary from the LLM.
    """
    try:
        prompt = create_summary_prompt_template()

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

        llm_chain = LLMChain(llm=llm, prompt=prompt)

        response = llm_chain.run({"context": "", "input": text})

        # If response is a string directly
        return response
    except Exception as e:
        logging.error(f"Error during summary generation: {e}")
        return "An error occurred during summary generation."

