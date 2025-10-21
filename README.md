# VaultofCodes
Major Project for Prompt Engineering: "AI Assistant Development"
# 🧠 AI Assistant Web Application

An interactive **AI Assistant** built using **Python Flask** and the **OpenAI API**.
This project allows users to ask questions, summarize text, and generate creative content through a simple and elegant web interface.

---

## 🚀 Features

- **Answer Questions:** Provides detailed answers to user queries.
- **Summarize Text:** Generates concise summaries from longer text.
- **Creative Writing:** Produces stories, poems, or ideas based on prompts.
- **Feedback System:** Users can indicate if the response was helpful.
- **Responsive UI:** Designed with CSS and Flask templates for a modern look.

---

## 🧩 Technology Stack

| Component      | Description                 |
|---------------|----------------------------|
| **Frontend**  | HTML / CSS                  |
| **Backend**   | Python (Flask Framework)    |
| **AI Model**  | OpenAI GPT-3.5 Turbo        |
| **Environment Management** | python-dotenv   |
| **Version Control** | Git & GitHub           |

---

## ⚙️ Setup & Installation

### Step 1: Clone This Repository :  https://github.com/mayanksinghgitu/VaultofCodes
cd ai-assistant-flask

text

### Step 2: Create a Virtual Environment
python -m venv venv
venv\Scripts\activate # For Windows

or
source venv/bin/activate # For macOS/Linux

text

### Step 3: Install Dependencies
pip install -r requirements.txt

text

### Step 4: Configure Environment Variables
Create a file named `.env` in your project directory:
OPENAI_API_KEY=sk-your-api-key-here

text
*(Important: Never share your actual API key publicly.)*

---

## ▶️ Running the Application
python ai_assistant.py

text
Then open your browser and visit:
[**http://127.0.0.1:5000/**](http://127.0.0.1:5000/)

---

## 🖼️ Screenshot (Example)
_Add your own app screenshot below for clarity._

![AI Assistant Screenshot](screenshot.png)

---

## 📁 Project Structure

ai-assistant-flask/
│
├── ai_assistant.py # Main Flask app
├── .env.example # Example environment file
├── requirements.txt # Dependencies
├── README.md # Documentation
└── feedback_log.txt # Stores user feedback

text

---

## 💡 Future Enhancements
- Chat-based continuous conversation
- Voice input and speech response using OpenAI’s TTS APIs
- Cloud deployment (Render / PythonAnywhere / Vercel)

---

## 🧾 License

This project is licensed under the **MIT License** – you’re free to use, modify, and share it with attribution.

---

## 🧑‍💻 Author

**MAYANK SINGH**
📧 Email: mayanksinghsara80@gmail.com
🌐 GitHub:  https://github.com/mayanksinghgitu/VaultofCodes

---

### ⚠️ Important Note
To use this application, you must have an **active OpenAI account** with a valid API key and available API credits.
