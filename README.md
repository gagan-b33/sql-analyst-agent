# AI-Powered SQL Analyst Agent

## Overview
An Agentic AI application that translates natural language queries into executable SQL and queries a relational database to return accurate data insights. Built to demonstrate end-to-end AI application development and agentic workflow orchestration for enterprise decision science.

## Tech Stack
- **Core Language:** Python
- **AI Framework:** LangChain (Agentic workflows and Tool calling)
- **LLM API:** Groq (GPT-OSS-120b)
- **Database:** SQLite (Relational data storage)
- **Frontend:** Streamlit (Interactive web UI)
- **Deployment:** Docker (Containerized environment)

## Key Features
- **Agentic Workflow:** Uses LangChain to autonomously plan and write SQL queries without human intervention.
- **Self-Correction:** Implements error handling allowing the agent to review failed executions and rewrite queries automatically.
- **Transparent Logging:** The UI exposes intermediate steps to support functional testing and output validation.
- **Secure Configuration:** Uses environment variables for API key management to prevent credential leakage.

## Project Structure
- `agent_core.py`: Contains the core LangChain agent logic and fallback mechanisms.
- `app.py`: The Streamlit frontend interface for user interaction.
- `create_db.py`: Script to generate the mock SQLite database with sample data.
- `Dockerfile`: Configuration for containerizing the application.
- `requirements.txt`: List of top-level Python dependencies.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/gagan-b33/sql-analyst-agent.git
   cd sql-analyst-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Groq API key:
   ```text
   GROQ_API_KEY=your_actual_api_key_here
   ```

4. Generate the mock database:
   ```bash
   python create_db.py
   ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to Run with Docker

1. Build the Docker image:
   ```bash
   docker build -t sql-analyst-agent .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 --env-file .env sql-analyst-agent
   ```

3. Open your browser to `http://localhost:8501`

## Example Output

**User Question:** "Who is the top employee by total sales?"

**Agent Workflow:**
1. Tool Used: `sql_db_list_tables` -> Identifies `employees` and `sales` tables.
2. Tool Used: `sql_db_schema` -> Reads table structures to understand relationships.
3. Tool Used: `sql_db_query_checker` -> Validates the generated SQL syntax.
4. Tool Used: `sql_db_query` -> Executes the final query.

**Final Answer:** The employee with the highest total sales is Bob Johnson with total sales amounting to $32000.

## Alignment with Decision Science Practices
- **Generative AI and Agentic Concepts:** Demonstrates practical use of LLMs for tool calling and workflow orchestration.
- **Functional Testing and Validation:** The transparent UI allows developers to trace the exact reasoning path of the AI to identify improvement opportunities.
- **AI Engineering and Deployment:** Follows sound software engineering practices including version control and containerized deployment for consistent environments.
