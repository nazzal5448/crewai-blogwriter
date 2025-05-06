
# 🧠 SEO Blog Generator with CrewAI and FastAPI

An AI-powered, agent-based blog generation system using [CrewAI](https://github.com/joaomdmoura/crewai), [Groq LLMs](https://console.groq.com/), and FastAPI. This project automates the creation of human-like, SEO-optimized blog posts using a team of expert agents for writing, humanizing, optimizing, and finalizing content.

---

## 🚀 Features

- ✅ Multi-agent workflow using CrewAI
- ✅ SEO blog post generation with a manager, writer, editor, SEO auditor, and AI detection specialist
- ✅ Groq LLM integration for blazing-fast responses
- ✅ FastAPI server for HTTP-based access
- ✅ Easily extendable to send blog output to Google Sheets, Telegram, or even auto-publish

---

## 📁 Project Structure

```
workflow-1/
│
├── agents.yaml          # Agent definitions (roles, goals, backstories)
├── tasks.yaml           # Task definitions (mapped to agents)
├── main.py              # CrewAI workflow setup and execution
├── app.py               # FastAPI server for accessing the workflow
├── .env                 # Store GROQ_API_KEY here
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nazzal5448/crewai-blogwriter.git
cd crewai-blogwriter
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your Groq API Key

Create a `.env` file in the root and add:

```env
GROQ_API_KEY=your-groq-api-key
```

### 5. Run the FastAPI Server

```bash
uvicorn app:app --reload
```

Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs) to test the endpoints.

---

## 📡 API Endpoints

### `GET /`
Health check.

**Response**
```json
{ "message": "Hello from CrewAI!" }
```

### `GET /generate`

Generate a blog based on keywords.

**Query Parameters**
- `main_keyword`: Main SEO keyword
- `related_keywords`: List of supporting keywords

**Example**
```
/generate?main_keyword=AI%20SEO&related_keywords=ranking&related_keywords=traffic
```

---

## 📌 Roadmap

- [ ] ✅ Add Telegram integration
- [ ] ✅ Google Sheets update
- [ ] ✅ Web publishing hook (WordPress or Ghost CMS)
- [ ] 🔄 Add progress tracking per agent

---

## 🤝 Contributions

PRs and suggestions welcome! Let's build smarter content automation tools together.

---

## 📜 License

MIT License
