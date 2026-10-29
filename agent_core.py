import os
import warnings
from typing import List, Tuple
from dotenv import load_dotenv

load_dotenv()
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

db = SQLDatabase.from_uri("sqlite:///company_data.db")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    agent_type="openai-tools", 
    agent_executor_kwargs={
        "handle_parsing_errors": True,
        "return_intermediate_steps": True
    },
    top_k=10
)

def fallback_direct_query(question: str, database: SQLDatabase, model: ChatGroq) -> str:
    schema = database.get_table_info()
    
    prompt = PromptTemplate.from_template("""
    You are a SQL expert. Given the following database schema write a SQL query to answer the question.
    Only return the SQL query without explanations.
    
    Schema:
    {schema}
    
    Question: {question}
    
    SQL Query:
    """)
    
    chain = prompt | model | StrOutputParser()
    
    try:
        sql_query = chain.invoke({"schema": schema, "question": question})
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        result = database.run(sql_query)
        return f"Generated Query: {sql_query}\n\nResult: {result}"
    except Exception as e:
        return f"Could not generate answer. Error: {str(e)}"

def run_agent_query(user_question: str) -> Tuple[str, List]:
    try:
        response = agent.invoke({
            "input": user_question,
            "agent_scratchpad": []
        })
        
        final_answer = response.get("output", "No answer generated.")
        steps = response.get("intermediate_steps", [])
        
        return final_answer, steps
        
    except Exception as e:
        error_msg = str(e)
        if "Tool choice is none" in error_msg or "Tool" in error_msg:
            return fallback_direct_query(user_question, db, llm), []
        return f"Error: {error_msg}", []

if __name__ == "__main__":
    print("Testing agent...")
    ans, steps = run_agent_query("What is the average salary of employees in the Sales department?")
    print(f"Final Answer: {ans}")