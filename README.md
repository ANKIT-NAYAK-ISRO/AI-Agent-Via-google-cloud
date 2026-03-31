# 🚀 AI Agent using Google Gemini & FastAPI

## 🌟 Overview

This project is a **lightweight AI Agent** built using Google's Gemini model and FastAPI, designed to process text input and return meaningful insights.

The agent performs:

* 📄 Text Summarization
* 🔑 Key Point Extraction
* ❓ Question Generation

It is deployed on **Google Cloud Run** and accessible via a public HTTP endpoint.

---

## 🧠 Problem Statement

Build and deploy a single AI agent using ADK and Gemini that:

* Performs one clearly defined task
* Is accessible via HTTP
* Returns valid responses for input

---

## ⚙️ Features

* ✅ Fast and lightweight AI agent
* ✅ Uses **Gemini (GenAI)** for inference
* ✅ REST API using FastAPI
* ✅ Fully deployed on Cloud Run
* ✅ Publicly accessible endpoint

---

## 🏗️ Tech Stack

* 🐍 Python
* ⚡ FastAPI
* 🤖 Google Gemini API
* ☁️ Google Cloud Run
* 🐳 Docker

---

## 📡 API Endpoint

### 🔹 Base URL

```
https://ai-agent-360671078793.asia-south1.run.app/
```

### 🔹 Analyze Endpoint

```
POST /analyze
```

---

## 📥 Sample Request

```json
{
  "text": "Artificial Intelligence is transforming the world..."
}
```

---

## 📤 Sample Response

```
Summary:
AI is transforming industries by improving efficiency...

Key Points:
- Automation increases productivity
- AI enhances decision making
- Data-driven insights

Questions:
1. How does AI improve efficiency?
2. What industries benefit most from AI?
```

---

## ▶️ How to Run Locally

```bash
git clone <your-repo-url>
cd ai-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## ☁️ Deployment

This project is deployed using **Google Cloud Run** with Docker.

---

## 🎯 Use Cases

* 📚 Student revision tool
* 📝 Content summarization
* 🤖 AI-powered assistants
* 📊 Quick knowledge extraction

---

## 👨‍💻 Author

**Ankit Nayak**

---

## 📜 License

MIT License
