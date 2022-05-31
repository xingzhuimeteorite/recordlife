from github import Github
from configinfo import Github_token
# First create a Github instance:

# using an access token
access_token = Github_token
g = Github(Github_token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
