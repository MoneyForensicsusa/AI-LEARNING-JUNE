import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return f"(Error: status code {response.status_code})"

    data = response.json()
    return {
        "name": data.get("name", "No name set"),
        "public_repos": data.get("public_repos", 0),
        "followers": data.get("followers", 0)
    }

user = get_github_user("MoneyForensicsusa")
print(user)
print(f"Repos: {user['public_repos']}, Followers: {user['followers']}")