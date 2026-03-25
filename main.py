from fastapi import FastAPI #biblioteca que cria api
import requests #permite fazer requisicoes
app = FastAPI()
@app.get("/pedido/{id}")
def buscar_pedido(id: int):

    resposta = requests.get("http://servico1:8000/produto/" + str(id))

    produto = resposta.json()

    return {
        "pedido": id,
        "produto": produto
    }