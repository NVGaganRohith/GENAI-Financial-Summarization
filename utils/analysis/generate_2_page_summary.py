from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.llm import LLMChain
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
import logging

logging.basicConfig(level=logging.INFO)

def initialize_document_db(directory: str) -> Chroma:
    """Initializes the document database.

    Args:
        directory (str): Path to the directory containing the document database.

    Returns:
        Chroma: Initialized document database.
    """
    try:
        return Chroma(persist_directory=directory, embedding_function=OpenAIEmbeddings())
    except Exception as e:
        logging.error(f"Error initializing document database at {directory}: {e}")
        raise

def create_prompt_template() -> PromptTemplate:
    """Creates a prompt template for the LLM.

    Returns:
        PromptTemplate: The prompt template.
    """
    template = """
    You are a helpful Financial assistant. Use the vectors present in database. If not present, say that the data is not present.
    Answer based on the context provided. Answer in around 600 words.
    context: {context}
    input: {input}
    ANSWER
    """
    return PromptTemplate.from_template(template)

def analyze_with_llm_openai(document_db_directory: str) -> str:
    """
    Analyzes documents in a vector database using OpenAI's GPT-4 model.
    
    Args:
        document_db_directory (str): Path to the directory containing the document database.
    
    Returns:
        str: The analysis result from the LLM.
    """
    try:
        document_db = initialize_document_db(document_db_directory)
        retriever = document_db.as_retriever()
        
        prompt = create_prompt_template()

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

        llm_chain = LLMChain(llm=llm, prompt=prompt)
        combine_docs_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
        
        # """
        # Please use the vectors present in the provided database. If a vector is not available, use your own knowledge base, but do not overwrite anything already present in the provided knowledge base.
        # Carefully check the company name for which the financial report is being made.

        # Generate a 750-word report with a 10-word buffer. Do not include any introductory or concluding text. Ensure the report fits within 2 A4 size pages without exceeding the limit or leaving white space at the end. If there is extra space, add relevant information in the appropriate sections.

        # Follow these guidelines:

        # - Use the company name instead of the word "company" throughout the report.
        # - Ensure all information provided is accurate and up-to-date.
        # - Format the report with exactly 8 sections, each marked with '###' as a heading.
        # - Do not use any symbols like '*', '**' in the headings or subheadings.
        # """


        #         Use the vectors present in database.
        # If not present, use your own knowledge base, but don't overwrite any thing which is already present in the provided knowledge base.
        # Carefully check the company name about which the financial report is being made.
        # Answer in 800 words with 10 words buffer and don't add unnecessary space.
        # Add titles for each section.
        # Don't write any generic text like introducing and concluding.
        # Make it look like a 2 page report.
        # Make sure the entire text fits in 2 A4 size pages and does not exceeds it. 
        # Also make sure there is no white space in the end rather add some more essential information in the relevant sections.
        # Make sure not to add any '*' or '**' or '***' to any of the headings or subheadings, and make it look like a clean report.
        # Instead of using word 'company' use the name of the company in the report.
        # Make sure you give the correct information about the company and any external info that you are giving is accurate.
        # Add '###' for any headings or titles. In total there will be only 8 headings. 
        # Give the given company's business overview.
        # Include information such as the company's formation/incorporation date, headquarters location, business description, employee count, latest revenues, stock exchange listing and market capitalization, number of offices and locations, and details on their clients.


        # Original prompt-
      



        response = retrieval_chain.invoke({"input": """
        Use the vectors present in database. If not present, use your own knowledge base, but don't overwrite any thing which is already present in the provided knowledge base.
        Carefully check the company name about which the financial report is being made.
        Answer in 570 words with 30 words buffer and dont add unnecessary space. Add titles for each section. Don't write any generic text like introducing and concluding, just make it look like a 2 page report.
        Make sure the entire text fits in 2 A4 size pages and there is no white space in the end rather add some more essential information in the relevant sections. Make sure not to add any '*' or '**' or '***' to any of the headings or subheadings, and make it look like a clean report.
        Instead of using word 'company' use the name of the company in the report.
        Make sure you are using the same company name about which the whole report is, throughout the report.
        Make sure you give the correct information about the company and any external info that you are giving is accurate.
        Add '###' for any headings or titles. In total there will be only 8 headings. 
        Give the given company's business overview. Include information such as the company's formation/incorporation date of first headquarter, headquarters location, business description, employee count, latest revenues, stock exchange listing and market capitalization, number of offices and locations, and details on their clients.

        Business Segment Overview
        Extract the revenue percentage of each component (verticals, products, segments, and sections) as a part of the total revenue.
        Performance: Evaluate the performance of each component by comparing the current year's sales perrevenue and market share with the previous year's numbers.  
        Sales Increase/Decrease explanation: Explain the causes of the increase or decrease in the performance of each component.


        Breakdown of sales and revenue by geography, specifying the percentage contribution of each region to the total sales.

        Summarize geographical data, such as workforce, clients, and offices, and outline the company's regional plans for expansion or reduction.

        Analyze and explain regional sales fluctuations, including a geographical sales breakdown to identify sales trends.

        Year-over-year sales increase or decline and reasons for the change

        Summary of rationale & considerations (risks & mitigating factors)

        SWOT Analysis

        Information about credit rating/credit rating change/change in the rating outlook.
    
        """})
        
        return response['answer']
    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        return "An error occurred during analysis."
