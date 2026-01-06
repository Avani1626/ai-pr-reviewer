import requests

def get_pr_data():
    # 🔴 CHANGE THESE VALUES
    owner = "octocat"
    repo = "Hello-World"
    pr_number = 1

    # 🔴 PASTE YOUR TOKEN HERE
   token = "YOUR_GITHUB_TOKEN_HERE"


    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching PR data")
        print("Status Code:", response.status_code)
        return "Unknown PR", "Could not fetch PR description", []

    data = response.json()

    title = data.get("title", "")
    description = data.get("body") or "No description provided by author."

    files_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    files_response = requests.get(files_url, headers=headers)

    patches = []

    if files_response.status_code == 200:
        files = files_response.json()
        for file in files:
            patch = file.get("patch")
            if patch:
                patches.append(patch)

    return title, description, patches
