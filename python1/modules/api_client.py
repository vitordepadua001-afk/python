import json
import urllib.error
import urllib.request

url = 'https://jsonplaceholder.typicode.com/users'

def fetch_data(url: str) -> dict | list:
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            raw_data = response.read().decode("utf-8")
            return json.loads(raw_data)
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print(f"An error ocurred: {e}")
        return []

if __name__ == '__main__':
    result = fetch_data(url)
    print(result)