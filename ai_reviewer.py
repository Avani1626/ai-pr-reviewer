from openai import OpenAI

def ai_review_pr(title, description, patches):
    client = OpenAI(client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")
")

    diff_text = "\n\n".join(patches)

    prompt = f"""
You are a senior software engineer performing a code review.

Pull Request Title:
{title}

Pull Request Description:
{description}

Code Changes:
{diff_text}

Tasks:
1. Decide whether this pull request is safe to merge.
2. List any potential issues.
3. Give a final recommendation.

Respond in this format only:

MERGE DECISION:
ISSUES:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content

    except Exception:
        return """MERGE DECISION:
AI REVIEW UNAVAILABLE

ISSUES:
- OpenAI API quota exceeded or unavailable
- This system uses a real LLM-based reviewer
- Please try again later or enable billing
"""
