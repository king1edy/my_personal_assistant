# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
from utils import (
    create_email_chain,
    create_study_plan_chain,
    create_knowledge_qna_chain,
    create_action_items_chain,
    initialize_agent_executor,
    get_llm_instance
)

llm = get_llm_instance()
# Create all chains and the agent executor once to avoid repeated initialization
email_chain = create_email_chain(llm)
study_plan_chain = create_study_plan_chain(llm)
knowledge_qna_chain = create_knowledge_qna_chain(llm)
action_items_chain = create_action_items_chain(llm)
agent_executor = initialize_agent_executor()

st.tittle("Personal Assistant with LangChain")

task_type = st.sidebar.selectbox("Select a Task", [
    "Draft Email", "Knowledge-Based Q&A",
    "Genenrate Study Plan", "Extract Action Items", "Tool-Using Agent"
])

if task_type == "Draft Email":
    st.header("Draft an Email Based on Context")
    context_input = st.text_area("Enter the email context:")
    if st.button("Draft Email"):
        result = email_chain.run(context=context_input)
        st.text_area("Generated Email", result, height=300)