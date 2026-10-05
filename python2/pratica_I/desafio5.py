import requests
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/user/passwd'
basic = HTTPBasicAuth('user', 'passwd')

def desafio5(url: str):
    try:
        with requests.get(url, auth=basic, timeout=10) as r:
            r.raise_for_status()
            dados = r.json()
            print("\nDetalhes da autenticação:\n")
            if dados['authenticated']: 
                print("Autenticação: Aprovada")
            print(f"Nome do usuário: {dados['user']}\n")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar autenticação: {e}")

if __name__ == '__main__':
    desafio5(url)