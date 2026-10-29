import streamlit as st
from agent_core import run_agent_query

st.set_page_config(page_title="SQL Analyst Agent", page_icon="", layout="wide")

st.markdown("""
    <style>
    .stTextArea textarea {font-size: 16px;}
    .step-box {background-color: #f0f2f6; padding: 10px; border-radius: 5px; margin-bottom: 5px; font-family: monospace;}
    </style>
""", unsafe_allow_html=True)

st.title(" AI-Powered SQL Analyst Agent")
st.markdown("Ask questions in plain English. The agent will write the SQL execute it and return the data.")

user_input = st.text_area("Enter your question:", placeholder="e.g. Who is the top employee by total sales?")

if st.button("Analyze Data", type="primary"):
    if user_input:
        with st.spinner("Agent is thinking writing SQL and querying the database..."):
            final_answer, steps = run_agent_query(user_input)
            
        st.subheader(" Agent's Workflow & Validation Steps")
        if steps:
            for i, step in enumerate(steps):
                action = step[0]
                observation = step[1]
                st.markdown(f"**Step {i+1}:** Tool Used: `{action.tool}`")
                st.markdown(f"**Action Input:** `{action.tool_input}`")
                st.markdown(f"**Observation/Result:** `{observation}`")
                st.markdown("---")
        else:
            st.info("Agent answered directly without using tools.")

        st.subheader("✅ Final Answer")
        st.success(final_answer)
    else:
        st.warning("Please enter a question.")

with st.sidebar:
    st.header("Example Questions")
    st.markdown("- What is the average salary in Engineering?")
    st.markdown("- Which employee made the highest single sale?")
    st.markdown("- List all employees hired in 2022 or later.")