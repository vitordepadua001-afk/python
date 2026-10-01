import requests

url = 'https://httpbin.org/post'
payload = {"name": "Vitor", "cargo": "Estudante"}

def desafio2(url: str, payload: dict):
    try:
        with requests.post(url, json=payload, timeout=10) as r:
            status_code = r.status_code
            if(r.ok):
                print("Status returned true")
            else:
                print(f"Status returned false: {status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error ocurred: {e}")
        return []

if __name__ == '__main__':
    desafio2(url, payload)