def ai_review_pr(title, description, code):
    risky_keywords = ["bug", "fix", "null", "exception", "error", "crash"]

    text = (title + " " + description + " " + code).lower()

    issues = []

    for word in risky_keywords:
        if word in text:
            issues.append(f"Potential risk keyword detected: '{word}'")

    if issues:
        recommendation = "DO NOT MERGE"
    else:
        recommendation = "SAFE TO MERGE"

    return {
        "recommendation": recommendation,
        "issues": issues
    }
