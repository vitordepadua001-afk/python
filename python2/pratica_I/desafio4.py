import requests

# ou 'https://httpbin.org' para erro de RequestException
url = 'https://httpbin.org/status/404'

def desafio4(url: str):
    try:
        with requests.get(url, timeout=10) as r:
            r.raise_for_status()
            datas = r.json()
            print(f"Total de dados capturados: {len(datas)}")
    except requests.exceptions.HTTPError as http_error:
        print(f"Ocorreu um erro do tipo HTTP: {http_error}.")
    except requests.RequestException as request_error:
        print(f"Ocorreu um erro de rede ou conexão: {request_error}.")

if __name__ == '__main__':
    desafio4(url)