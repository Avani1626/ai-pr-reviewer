def review_pr(title, description):
    risky_keywords = ["bug", "fix", "null", "exception", "error", "crash"]

    text = (title + " " + description).lower()

    issues = []

    for word in risky_keywords:
        if word in text:
            issues.append(f"Potential risk keyword detected: '{word}'")

    if issues:
        recommendation = "DO NOT MERGE"
    else:
        recommendation = "SAFE TO MERGE"
        issues.append("No obvious issues detected")

    return recommendation, issues
