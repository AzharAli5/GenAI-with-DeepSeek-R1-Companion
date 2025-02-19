import re
import time
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom CSS styling
st.markdown("""
<style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .sidebar .sidebar-content { background-color: #2d2d2d; }
    .stTextInput textarea { color: #ffffff !important; }
    .stSelectbox div[data-baseweb="select"], div[role="listbox"] div {
        color: white !important; background-color: #3d3d3d !important;
    }
    .stSelectbox svg { fill: white !important; }
    .stSelectbox option { background-color: #2d2d2d !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox("Choose Model", ["deepseek-r1:1.5b"], index=0)
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("- 🐍 Python Expert\n- 🐞 Debugging Assistant\n- 📝 Code Documentation\n- 💡 Solution Design")
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# Initialize chat engine
llm_engine = ChatOllama(model=selected_model, base_url="http://localhost:11434", temperature=0.3)

# System prompt
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Manage session state
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Extract thinking and response text
def extract_thinking_and_response(ai_text):
    # Extract the text inside <think> tags
    think_match = re.search(r"<think>(.*?)</think>", ai_text, re.DOTALL)
    thinking_text = think_match.group(1).strip() if think_match else "Thinking..."

    # Remove the <think> tags from the final response
    final_response = re.sub(r"<think>.*?</think>", "", ai_text, flags=re.DOTALL).strip()
    
    return thinking_text, final_response


# Stream text word by word
def stream_text(text, chat_placeholder):
    words = text.split()
    streamed_text = ""
    for word in words:
        streamed_text += word + " "
        chat_placeholder.markdown(streamed_text)
        time.sleep(0.05)  # Streaming speed

# Build prompt chain
def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

# Generate AI response
def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

# Display previous chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
user_query = st.chat_input("Type your coding question here...")

if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})

    with st.chat_message("ai"):
        chat_placeholder = st.empty()
    
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_raw_response = generate_ai_response(prompt_chain)

    # Extract the thinking text (inside <think>) and the clean response
    thinking_text, final_response = extract_thinking_and_response(ai_raw_response)

    # Display the thinking text (but NOT the <think> tags)
    chat_placeholder.markdown(f"**🧠 {thinking_text}...**")

    # Stream the final response word by word
    stream_text(final_response, chat_placeholder)

    # Store only the cleaned response in chat history
    st.session_state.message_log.append({"role": "ai", "content": final_response})

    st.rerun()