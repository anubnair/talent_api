import os
import requests

def fetch_data_from_github(username):
    # GitHub API URL for the user's repositories
    url = f'https://api.github.com/users/{username}/repos'

    # Send GET request to GitHub API
    response = requests.get(url)

    skills = []

    # Check if the request was successful
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            if repo['language'] not in skills and repo['language'] != 'null':
                skills.append(repo['language'])
    else:
        print(f"Failed to retrieve data: {response.status_code}")

    return skills