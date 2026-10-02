
# Prática I

Série de práticas iniciais para entendimento de python + HTTP

## desafio1

**Enunciado**:

Faça uma requisição para `https://httpbin.org`. Descubra e exiba na tela:
    1. O código de status da resposta.
    2. Qual é o servidor web (`Server`) que está rodando do outro lado.
    3. Qual é o tipo de conteúdo (`Content-Type`) que ele te devolveu.

**Código**:

```python
import requests

url = 'https://httpbin.org/get'

def desafio1(url: str):
	try:
		with resquests.get(url, timeout=10) as r:
			status_code = r.status_code
			content = r.headers.get('content-type', "Não informado")
			server = r.headers.get("Server", "Não informado")
		    print(f"Status: {status_code} \nContent: {content} \nServer: {server} \n")
	except requests.exceptions.RequestException as e:
		print(f"An error ocurred: {e}")
		return []
	
if __name__ == '__main__':
	desafio1(url)
```

Esse código pega as informações do método `/get` do site `httpbin.org/` e manipula ele de forma inteligente. Criamos uma função que recebe o parâmetro da url a ser manipulada, englobamos tudo dentro de um `try/except` para fins de segurança e usamos a função `with`, para quando terminar tudo ela encerrar a função de forma autônoma.

Depois disso pegamos as 3 informações que o enunciado pediu: `status_code`, `content`, `server` e imprimimos na tela o resultado gerado. Caso de erro manipulamos ele e também imprimimos na tela para saber oque ocorreu.

**Saída**:

```bash
aura@aura:~/novo/python/python2$ python3 desafio1.py
Status: 200
Content: application/json
Server: gunicorn/19.9.0

aura@aura:~/novo/python/python2$ curl -I "https://httpbin.org/"
HTTP/2 200
date: Thu, 01 Oct 2026 17:26:50 GMT
content-type: text/html; charset=utf-8
content-length: 9593
server: gunicorn/19.9.0
access-control-allow-origin: *
access-control-allow-credentials: true
```

## desafio2

**Enunciado**:

Envie uma requisição do tipo **POST** para `https://httpbin.org` contendo o seu nome e sua profissão/estudo em formato JSON (ex: `{"nome": "Seu Nome", "cargo": "Estudante"}`). Confirme se o servidor recebeu exatamente o que você enviou olhando o JSON de retorno.

**Código**:

```python
import requests

url = 'https://httpbin.org/post'
payload = {"name": "Vitor", "cargo": "Estudante"}

def desafio2(url: str, payload: dict):
	try:
		with request.post(url, json=payload, timeout=10) as r:
			status_code = r.status_code
			if(r.ok):
				print("Status = True")
			else:
				print(f"Status = False \nStatus log: {status_code}")
	except requests.exception.RequestException as e:
		print(f"An error ocurred: {e}")
		return []
	
if __name__ == '__main__':
	desafio2(url, payload)
```

Esse código pega as informações do método `get` do site `httpbin.org` para inserir um `json` com duas entidades. Depois disso vamos fazer uma função que chama o `post` pela biblioteca `request` e pega seu `status_code` para saber oque foi retornado. Uma estrutura de condição simples (`if/else`), decidindo oque vai ser mostrado na hora. Pra fechar envelopamos tudo dentro de `try/except` para maior segurança sobre o código e depois executamos ele.

**Saída**:

```bash

python/python2  main  v3.14.7 
╰─❯ curl -X POST -H "Content-Type: application/json" -d '{"name": "Vitor", "cargo": "Estudante"}' https://httpbin.org/post
{
  "args": {}, 
  "data": "{\"name\": \"Vitor\", \"cargo\": \"Estudante\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "39", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/8.22.0", 
    "X-Amzn-Trace-Id": "Root=1-6abfdbe4-7501f9cc461753ca0aa697fa"
  }, 
  "json": {
    "cargo": "Estudante", 
    "name": "Vitor"
  }, 
  "origin": "189.61.53.242", 
  "url": "https://httpbin.org/post"
}

python/python2  main  v3.14.7 
╰─❯ python3 desafio2.py 
Status returned true

python/python2  main  v3.14.7 
╰─❯ 
```

## desafio3

**Enunciado:**

Simule uma busca por produtos. Faça uma requisição **GET** para `https://typicode.com`, mas não traga todos os comentários. Filtre a URL para trazer **apenas** os comentários do post de ID número 1 (geralmente usa-se a chave `postId`).

**Código**:

```python
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
```

O código seleciona apenas os comentários requisitados pelo enunciado do método `/comments`. Depois faz uma função envelopada por `try/except` para garantir mais segurança e integridade e faz um request do tipo `get` passando a url desejada, o parâmetro e tempo de espera caso fique travado.

Depois disso ele apenas verifica o status retornado se for `true (200)`, ele guarda o retorno na variável `comments` e faz uma sequência de outputs informando quantidade encontrada, números, mensagens, quem mandou etc. Logo em seguida apenas tratamos os erros e executamos o código.

**Saída**:

```bash
python/python2  main ?  v3.14.7 
╰─❯ python3 desafio3.py 

Comentários encontrados: 5
postId: 1

De: Eliseo@gardner.biz
Nome: id labore ex et quam laborum
Comentário: laudantium enim quasi est quidem magnam voluptate ipsam eos
tempora quo necessitatibus
dolor quam autem quasi
reiciendis et nam sapiente accusantium


De: Jayne_Kuhic@sydney.com
Nome: quo vero reiciendis velit similique earum
Comentário: est natus enim nihil est dolore omnis voluptatem numquam
et omnis occaecati quod ullam at
voluptatem error expedita pariatur
nihil sint nostrum voluptatem reiciendis et


De: Nikita@garfield.biz
Nome: odio adipisci rerum aut animi
Comentário: quia molestiae reprehenderit quasi aspernatur
aut expedita occaecati aliquam eveniet laudantium
omnis quibusdam delectus saepe quia accusamus maiores nam est
cum et ducimus et vero voluptates excepturi deleniti ratione


De: Lew@alysha.tv
Nome: alias odio sit
Comentário: non et atque
occaecati deserunt quas accusantium unde odit nobis qui voluptatem
quia voluptas consequuntur itaque dolor
et qui rerum deleniti ut occaecati


De: Hayden@althea.biz
Nome: vero eaque aliquid doloribus et culpa
Comentário: harum non quasi et ratione
tempore iure ex voluptates in ratione
harum architecto fugit inventore cupiditate
voluptates magni quo et

python/python2  main ?  v3.14.7 
╰─❯  curl curl -G -d "postId=1" "https://jsonplaceholder.typicode.com/comments"
curl: (6) Could not resolve host: curl
[
  {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  },
  {
    "postId": 1,
    "id": 2,
    "name": "quo vero reiciendis velit similique earum",
    "email": "Jayne_Kuhic@sydney.com",
    "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
  },
  {
    "postId": 1,
    "id": 3,
    "name": "odio adipisci rerum aut animi",
    "email": "Nikita@garfield.biz",
    "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
  },
  {
    "postId": 1,
    "id": 4,
    "name": "alias odio sit",
    "email": "Lew@alysha.tv",
    "body": "non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati"
  },
  {
    "postId": 1,
    "id": 5,
    "name": "vero eaque aliquid doloribus et culpa",
    "email": "Hayden@althea.biz",
    "body": "harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et"
  }
]
python/python2  main ?  v3.14.7 
╰─❯ 
```

## desafio4

**Enunciado**:

Force um erro. Tente acessar `https://httpbin.org` no curl e no Python.

**Código**:

```python
import requests

# ou 'https://httpbin.org' para erro de RequestException
url = 'https://httpbin.org/status/404'

def desafio4(url: str):
	try:
		with request.get(url, timeout=10) as r:
			r.raise_status_code()
			dados = r.json()
			print(f"Total de dados encontrados: {len(dados)}")
	except requests.exception.HTTPError as http_error:
		print(f"Ocorreu um erro do tipo HTTP: {http_error}")
	except requests.exception.RequestException as request_error:
		print(f"Ocorreu um erro de conexão ou rede: {request_error}")

if __name__ == '__main__':
	desafio4(url)
```

Basicamente esse código vai atuar sobre uma URL inválida para testar erros e também testar a função `raise_status_code()` onde caso retorne erro ao tentar usar o método na url proposta ele retorna `None` e acaba a execução (vai para o `except`). Por isso o `try/except` é tão importante, pois em casos de erros ele vai avisar, retornar qual o problema e finalizar o código de forma limpa. Se retornar erro apenas tratamos de forma distintas os motivos e o output vai depender de qual erro retornou, no final executamos.

**Saída**:

```bash
╰─❯ python3 desafio4.py 
Ocorreu um erro do tipo HTTP: 404 Client Error: NOT FOUND for url: https://httpbin.org/status/404.

python/python2  main ?  v3.14.7 
╰─❯ curl -f -G "https://httpbin.org/status/404"
curl: (22) The requested URL returned error: 404
```

## desafio5

**Enunciado**:

Acesse a rota protegida `https://httpbin.org`. Se você tentar acessar direto, vai tomar um erro `401 Unauthorized`. Descubra como passar o usuário `user` e a senha `passwd` para que o servidor te dê um `200 OK`.

**Código**:

```python
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
	except requests.exception.RequestException as e:
		print(f"Erro ao tentar autenticação: {e}")

if __name__ == '__main__':
	desafio5(url)
```

Esse código testa a autenticação de um user com o método `get`, depois ele guarda dentro da variável `basic` a autenticação validada para as entidades `user` e `passwd`.

Depois faz uma função que faz um request para a url desejada, com a autenticação prevista (`basic`) e tempo limite para caso entre em loop ou não consiga concluir. Verifica o `status_code` retornado, se for válidado ele continua e mostra o que retornou se não for entra no `try/except` e o erro é manipulado, no final apenas executamos.

**Saída**:

```bash
python/python2  main ?  v3.14.7 
╰─❯ python3 desafio5.py 

Detalhes da autenticação:

Autenticação: Aprovada
Nome do usuário: user

python/python2  main ?  v3.14.7 
╰─❯ curl -u "user:passwd" "https://httpbin.org/basic-auth/user/passwd"
{
  "authenticated": true, 
  "user": "user"
}
```
