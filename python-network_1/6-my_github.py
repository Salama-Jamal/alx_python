import requests
import sys

def get_github_id(username, token):
    url = "https://api.github.com/user"
    auth = (username, token)

    response = requests.get(url, auth=auth)
    
    try:
        json_data = response.json()
        if 'id' in json_data:
            print(json_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    get_github_id(username, token)