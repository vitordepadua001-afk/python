import requests

url = 'https://httpbin.org/get'

def desafio1(url: str):
    try:
        with requests.get(url, timeout=10) as r:
            status_code = r.status_code
            content = r.headers.get('content-type', "Não informado")
            server = r.headers.get("Server", "Não informado")
            print(f"Status: {status_code} \nContent: {content} \nServer: {server} \n")
    except requests.exceptions.RequestException as e:
        print(f"An error ocurred: {e}")
        return []

if __name__ == '__main__':
    desafio1(url)