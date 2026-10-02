import requests

url = 'https://jsonplaceholder.typicode.com/comments'
payload = {"postId": 1}

def desafio3(url: str, payload: dict):
    try:
        with requests.get(url, params=payload, timeout=10) as r:
            status_code = r.status_code
            if r.ok: 
                comments = r.json()
                print(f"\nComentários encontrados: {len(comments)}")
                print(f"postId: {payload.get('postId')}\n")
                for c in comments:
                    print(f"De: {c['email']}")
                    print(f"Nome: {c['name']}")
                    print(f"Comentário: {c['body']}")
                    print('\n')
            else:
                print(f"Falha.\n Status: {status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na busca: {e}")

if __name__ == '__main__':
    desafio3(url, payload)