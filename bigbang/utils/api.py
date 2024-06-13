import requests


def get(endpoint):
    """function for GET request
    for getting node's block status, not async request
    """
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print(f"error {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None
