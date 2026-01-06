from github_fetch import get_pr_data
from ai_reviewer import ai_review_pr

print("Fetching Pull Request data...\n")

title, description, patches = get_pr_data()

print("PR Title:")
print(title)

print("\nPR Description:")
print(description)

print("\nCODE CHANGES (DIFF):\n")

if not patches:
    print("No code changes available.")
else:
    for i, patch in enumerate(patches, start=1):
        print(f"--- Patch {i} ---")
        print(patch)

print("\nRunning AI Review...\n")

ai_result = ai_review_pr(title, description, patches)

print(ai_result)

