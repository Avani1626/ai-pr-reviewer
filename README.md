# AI-Based Pull Request Reviewer 🚀

An AI-powered prototype that automatically reviews GitHub Pull Requests by
analyzing PR metadata and code changes, and then provides a merge recommendation.

This project is inspired by recent research on automated code review,
mining software repositories, and Large Language Models (LLMs) in software engineering.

---

## 🔍 Problem Statement

Manual code review is time-consuming and error-prone.
Developers need quick feedback on whether a pull request is safe to merge.

This project demonstrates how:
- GitHub Pull Request data can be fetched automatically
- Code diffs can be analyzed
- AI models can assist in code review decisions

---

## 🎯 Objectives

- Fetch real GitHub Pull Request data using GitHub REST API
- Extract changed files and code diffs
- Analyze PRs using AI-based reasoning
- Provide a merge recommendation
- Handle real-world issues like API quota limits safely

---

## 🛠️ Tech Stack

- **Python**
- **GitHub REST API**
- **OpenAI API (LLM-based review)**
- **Git & GitHub**
- Command Line Interface (CLI)

---

## ⚙️ Project Architecture

main.py
├── github_fetch.py → Fetches PR title, description & code diff
├── reviewer.py → Rule-based reviewer (backup)
└── ai_reviewer.py → LLM-based AI reviewer with safe fallback

yaml
Copy code

---

## 🔄 How the System Works

1. User provides a GitHub repository and Pull Request number
2. The system fetches:
   - PR title
   - PR description
   - Code diffs (patches)
3. The AI reviewer analyzes the PR context and changes
4. The system outputs:
   - Merge decision
   - Potential issues
5. If AI quota is unavailable, a safe fallback message is shown

---

## 🤖 AI Integration Note

This project integrates a real Large Language Model (LLM) using the OpenAI API.

During testing, API quota limits may be reached.
In such cases, the system:
- Does NOT crash
- Displays a professional fallback message
- Demonstrates real-world AI system behavior

This design choice reflects industry practices.

---

## 🚨 Security Considerations

- API keys are **NOT hardcoded**
- Secrets are removed before pushing to GitHub
- `.gitignore` is used to avoid committing sensitive or generated files

---

## 📌 Current Status

- ✅ GitHub PR fetching implemented
- ✅ Code diff extraction implemented
- ✅ AI-based review logic integrated
- ✅ Safe fallback for AI unavailability
- 🔄 Future enhancements planned

---

## 🚀 Future Scope

- Environment variable based API key management
- RAG (Retrieval Augmented Generation) using bug datasets
- GitHub Action integration for automatic PR reviews
- Evaluation using real PR datasets
- UI or browser extension

---

## 🎓 Academic Relevance

This project is suitable for:
- Final-year project
- Mini-project
- Research prototype
- Demonstration of AI in Software Engineering

---

## 👩‍💻 Author

**Avani Shinde**

---

## 📄 License

This project is for educational and research purposes.