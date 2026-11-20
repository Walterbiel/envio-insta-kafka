"""Lê o tópico 'pedidos' e soma o faturamento por cidade. Rode: python consumer.py"""
import json
from collections import defaultdict

from confluent_kafka import Consumer

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "relatorio",
    "auto.offset.reset": "earliest",   # grupo novo → começa do início
})
consumer.subscribe(["pedidos"])

faturamento = defaultdict(float)
print("Escutando o tópico 'pedidos' → Ctrl+C para sair")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Erro →", msg.error())
            continue
        pedido = json.loads(msg.value())
        faturamento[pedido["cidade"]] += pedido["valor"]
        resumo = ", ".join(f"{c}: {v:.2f}" for c, v in sorted(faturamento.items()))
        print(f"Pedido {pedido['id']} (partição {msg.partition()}) → {resumo}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()                   # salva o offset e sai do grupo
