import requests
import os

# Configura i tuoi repository
REPOSITORIES = [
    "zalmoxes-laran/EM-blender-tools",
    "zalmoxes-laran/3D-survey-collection"
]

# Funzione per recuperare i commit
def get_commits(repo):
    url = f"https://api.github.com/repos/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore nel recuperare i commit da {repo}: {response.status_code}")
        return []

# Funzione per recuperare le pull request
def get_pull_requests(repo):
    url = f"https://api.github.com/repos/{repo}/pulls"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore nel recuperare le pull request da {repo}: {response.status_code}")
        return []

# Funzione per recuperare le discussioni
def get_discussions(repo):
    url = f"https://api.github.com/repos/{repo}/issues"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore nel recuperare le discussioni da {repo}: {response.status_code}")
        return []

# Assicurati che la directory 'content' esista
if not os.path.exists("content"):
    os.makedirs("content")

# Recupera i dati da tutti i repository
for repo in REPOSITORIES:
    commits = get_commits(repo)
    pulls = get_pull_requests(repo)
    discussions = get_discussions(repo)
    
    # Salva i dati o genera i contenuti per Pelican
    with open(f"content/{repo.replace('/', '_')}_commits.md", "w") as f:
        f.write("# Commits\n")
        for commit in commits:
            f.write(f"- {commit['commit']['message']}\n")

    with open(f"content/{repo.replace('/', '_')}_pulls.md", "w") as f:
        f.write("# Pull Requests\n")
        for pr in pulls:
            f.write(f"- {pr['title']}\n")

    with open(f"content/{repo.replace('/', '_')}_discussions.md", "w") as f:
        f.write("# Discussions\n")
        for discussion in discussions:
            f.write(f"- {discussion['title']}\n")