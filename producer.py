"""Envia pedidos para o tópico 'pedidos'. Rode: python producer.py"""
import json
import random
import time

from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})

CIDADES = ["Recife", "Salvador", "Curitiba", "São Paulo"]


def confirmar(erro, msg):
    """Chamado quando o Kafka confirma (ou recusa) a mensagem."""
    if erro:
        print("Falhou →", erro)
    else:
        print(f"Enviado → partição {msg.partition()} offset {msg.offset()}")


for i in range(1, 21):
    pedido = {
        "id": i,
        "cliente": f"cliente_{random.randint(1, 5)}",
        "cidade": random.choice(CIDADES),
        "valor": round(random.uniform(20, 500), 2),
    }
    producer.produce(
        topic="pedidos",
        key=pedido["cliente"],                 # mesma chave → mesma partição
        value=json.dumps(pedido, ensure_ascii=False),
        callback=confirmar,
    )
    producer.poll(0)                           # dispara os callbacks
    time.sleep(0.5)

producer.flush()                               # espera tudo ser confirmado
