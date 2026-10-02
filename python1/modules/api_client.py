import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

url = 'https://jsonplaceholder.typicode.com/users'

def fetchData(url: str):
    try:
        with urlopen(url, timeout=10) as response:
            data = response.read().decode("utf-8")
            users = json.loads(data)
            names = {user["name"] for user in users}
            emails = {user["email"] for user in users}
            return names, emails
    except (HTTPError, URLError) as e:
        print(f"An error ocurred: {e}")
        return []

if __name__ == '__main__':
    result = fetchData(url)
    print(result)