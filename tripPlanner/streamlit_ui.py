import streamlit as st
import requests
import datetime
import logging

import sys

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Streamlit UI Started")


BASE_URL = "http://localhost:9001"

st.set_page_config(
    page_title="Trip Planner",
    page_icon=":airplane_departure:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS to prevent horizontal scrolling and optimize layout
st.markdown("""
    <style>
        .main {
            max-width: 100%;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
            max-width: 100%;
        }
        
        /* Heading Styles */
        h1 {
            color: #1f77b4;
            font-size: 2.5em;
            font-weight: bold;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            border-bottom: 3px solid #1f77b4;
            padding-bottom: 0.5em;
        }
        
        h2 {
            color: #2ca02c;
            font-size: 2em;
            font-weight: bold;
            margin-top: 1.3em;
            margin-bottom: 0.4em;
            border-left: 5px solid #2ca02c;
            padding-left: 0.8em;
        }
        
        h3 {
            color: #d62728;
            font-size: 1.5em;
            font-weight: bold;
            margin-top: 1em;
            margin-bottom: 0.3em;
        }
        
        h4, h5, h6 {
            color: #555;
            font-weight: bold;
            margin-top: 0.8em;
            margin-bottom: 0.3em;
        }
        
        /* Paragraph and Text Styles */
        p, li {
            word-wrap: break-word;
            overflow-wrap: break-word;
            white-space: normal;
            line-height: 1.6;
            font-size: 1em;
        }
        
        /* List Styles */
        ul {
            margin-left: 1.5em;
            padding-left: 1.5em;
        }
        
        ul li {
            margin-bottom: 0.5em;
            list-style: disc;
        }
        
        ul li ul li {
            list-style: circle;
            margin-left: 1em;
        }
        
        ol {
            margin-left: 1.5em;
            padding-left: 1.5em;
        }
        
        ol li {
            margin-bottom: 0.5em;
        }
        
        /* Table Styles */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            border: 1px solid #ddd;
        }
        
        th {
            background-color: #2ca02c;
            color: white;
            padding: 0.8em;
            text-align: left;
            font-weight: bold;
        }
        
        td {
            padding: 0.8em;
            border-bottom: 1px solid #ddd;
        }
        
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        /* Code and Pre Styles */
        code {
            word-break: break-all;
            white-space: normal;
            background-color: #f4f4f4;
            padding: 0.2em 0.4em;
            border-radius: 3px;
        }
        
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow-x: auto;
            background-color: #f4f4f4;
            padding: 1em;
            border-radius: 5px;
            border-left: 4px solid #2ca02c;
        }
        
        /* Horizontal Rule */
        hr {
            margin: 2em 0;
            border: none;
            border-top: 2px solid #1f77b4;
        }
        
        /* Emphasis Styles */
        strong {
            font-weight: bold;
            color: #d62728;
        }
        
        em {
            font-style: italic;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Trip Planner")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("Ask your travel related questions here:")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("Your Question:", placeholder="e.g., Plan a trip to Paris for 5 days with a budget of $2000")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input.strip():
    logger.debug(f"Processing user input: {user_input[:50]}...")
    try:

        with st.spinner("Planning your trip..."):
            payload = {"question": user_input}
            logger.debug(f"Sending request to {BASE_URL}/query")
            response = requests.post(f"{BASE_URL}/query", json=payload)
            logger.debug(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer received.")
            logger.info("Query processed successfully")
            markdown_content = f"""# 🌍 AI Travel Plan

**Generated:** {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')}  
**Created by:** Travel Agent

---

{answer}

---

*This travel plan was generated by AI. Please verify all information, especially prices, operating hours, and travel requirements before your trip.*
            """
            st.markdown(markdown_content)
        else:
            st.error(f"Error: {response.status_code} - {"Bot failed to respond"}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")