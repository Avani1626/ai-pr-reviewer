🧠 AI-Based GitHub Pull Request Reviewer

An AI-powered system that automatically reviews GitHub Pull Requests by analyzing code changes and providing merge recommendations.
The project is deployed on AWS EC2 and integrates GitHub APIs with a Large Language Model (LLM).

🚀 Project Overview

When a Pull Request (PR) is created on GitHub, developers usually need to manually:

Read the PR title and description

Inspect code diffs

Decide whether it is safe to merge

This project automates that process by:

Fetching PR details from GitHub

Extracting code changes (diffs)

Sending the information to an AI model

Returning a structured review and merge recommendation

🏗️ System Architecture (High Level)
GitHub Pull Request
        ↓
GitHub REST API
        ↓
AWS EC2 (Python Application)
        ↓
AI Reviewer (LLM)
        ↓
Review Output / Merge Recommendation

🔧 Technologies Used

Python 3

GitHub REST API

OpenAI API (LLM)

AWS EC2 (Ubuntu)

python-dotenv (for environment variables)

requests (for API calls)

📂 Project Structure
ai-pr-reviewer/
│
├── main.py               # Entry point of the application
├── github_fetch.py       # Fetches PR data and code diffs from GitHub
├── ai_reviewer.py        # Sends PR data to AI and generates review
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables (NOT committed)

⚙️ How the Project Works
1️⃣ Fetch Pull Request Data

Uses GitHub REST API

Retrieves:

PR title

PR description

Code diffs (patches)

2️⃣ AI-Based Code Review

PR details are sent to an LLM

AI analyzes:

Nature of changes

Potential risks

Code quality

Returns:

Summary

Issues (if any)

Merge recommendation

3️⃣ Safe Fallback Mechanism

If the AI API quota is exceeded or unavailable:

The application does not crash

A fallback review is generated

This ensures reliability and resilience

🔐 Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token   (optional for public repos)


⚠️ Important

Never commit .env

Add .env to .gitignore

☁️ Deployment on AWS EC2
Steps Summary:

Launch an Ubuntu EC2 instance (Free Tier)

SSH into the instance

Clone the GitHub repository

Create and activate a Python virtual environment

Install dependencies

Run the application

Commands Used:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

🛑 Cost Management

EC2 instances are billed only while running

After testing, the instance should be stopped

This prevents unnecessary cloud charges

🧠 Key Features

✔ Automated PR analysis
✔ Real GitHub API integration
✔ AI-based review generation
✔ Graceful fallback on API quota exhaustion
✔ Secure secret handling using environment variables
✔ Deployed on cloud (AWS EC2)

🧪 Example Output
PR Title:
Test PR for AI Reviewer

AI Review:
- The PR introduces documentation changes only.
- No risky logic or structural changes detected.
- Safe to merge.

📌 Use Cases

Faster code reviews

Assisting junior developers

CI/CD pipeline integration

Learning project for cloud + AI integration

📈 Future Enhancements

GitHub Webhook integration

FastAPI-based REST service

Docker containerization

Support for private repositories

Azure / GCP deployment

🧑‍💼 Interview / Manager Explanation (One-Liner)

“I built and deployed an AI-based GitHub Pull Request reviewer on AWS EC2 that fetches PR diffs, evaluates them using an LLM, and includes a graceful fallback when API quota limits are exceeded.”

📄 License

This project is for educational and research purposes.
