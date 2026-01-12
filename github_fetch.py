import requests

token = "YOUR_GITHUB_TOKEN_HERE"

headers = {
    "Authorization": f"token {token}"
}

def get_pr_data(owner, repo, pr_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    response = requests.get(url, headers=headers)
    return response.json()
