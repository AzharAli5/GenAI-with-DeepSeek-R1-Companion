**🚀 DeepSeek Code Companion
**
📝 Overview

DeepSeek Code Companion is an AI-powered coding assistant built with Ollama and LangChain. It provides real-time debugging, code explanations, and AI-assisted pair programming. This app is developed using Streamlit for an interactive and seamless coding experience.

🔧 Features

✅ AI Pair Programming: Get AI-generated code suggestions.

🐞 Debugging Assistance: Identify and fix errors in your code.

📝 Code Documentation: Automatically generate documentation for your code.

🎯 Real-time AI Streaming: Get responses word-by-word in real time.

⚡ Custom Model Selection: Choose between deepseek-r1:1.5b and deepseek-r1:3b.

📦 Installation

Follow these steps to install and run the app on your local machine.

1️⃣ Prerequisites

Ensure you have the following installed:

Python 3.9+ (Required for compatibility)

pip (Python package manager)

Ollama (For running AI models locally)

2️⃣ Clone the Repository

cd GenAI-with-DeepSeek-R1-Companion

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Install & Start Ollama

Install Ollama (if not already installed):

Visit: Ollama.ai

Download and install for your OS.

Run Ollama and download models:

ollama pull deepseek-r1:1.5b

Start the Ollama server:

ollama serve

5️⃣ Run the Application

Once Ollama is running, start the Streamlit app:

streamlit run app.py

⚙️ Usage

Open the web interface in your browser.

Type your coding questions or debugging queries.

Choose your preferred AI model from the sidebar.

Get real-time AI responses, streamed word-by-word.

🛠 Tech Stack

Python 3.9+

Streamlit (UI)

LangChain (AI Pipeline)

Ollama (Model Serving)

DeepSeek Models (LLMs for AI coding support)

🤝 Contributions

Want to improve the project? Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request.


