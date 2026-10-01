
# Integração com API utilizando urllib (api_client.py)

**Objetivo:** Consumir o endpoint `/users` da API JSONPlaceholder de forma nativa e segura.

## Estrutura e Fluxo do Código

1. **Importações e Configuração:**

   - Usa as bibliotecas nativas `json` (tratamento de dados) e `urllib.request` / `urllib.error` (comunicação web).
   - Define a variável global `url` apontando para o recurso alvo.
2. **Função `fetch_data(url)`:**

   - **Tipagem:** Configurada com Type Hints para receber uma `str` e retornar `dict | list`.
   - **Tratamento de Erros (`try/except`):** Envolve a conexão para capturar de forma robusta falhas de rede (`URLError`) ou erros do servidor (`HTTPError`).
   - **Gerenciador de Contexto (`with`):** Abre a URL usando `urllib.request.urlopen` com um `timeout=10` segundos. O bloco `with` garante o fechamento automático da conexão de rede.
   - **Processamento (`as response`):** Lê os bytes gerados pela resposta, decodifica em `utf-8` para texto plano e faz o *parsing* da string para estruturas nativas do Python com `json.loads()`.
   - **Fallback Seguro:** Caso ocorra uma exceção, o erro é printado e a função retorna uma **lista vazia `[]`**, evitando o travamento do programa por completo (`raise`).
3. **Execução Principal (`if __name__ == '__main__':`):**

   - Garante que a requisição só aconteça se o arquivo for executado diretamente, armazenando e exibindo o resultado final no terminal através da variável `result`.
