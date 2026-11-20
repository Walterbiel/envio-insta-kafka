# Kafka na Prática

Material gratuito do QG da Engenharia de Dados. Você recebeu porque comentou **KAFKA**.

Um producer que envia pedidos e um consumer que calcula o faturamento por cidade em tempo real.

## Como usar este material

1. Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/) e o Python
2. Suba o Kafka:

```bash
docker compose up -d
```

3. Instale a biblioteca:

```bash
pip install -r requirements.txt
```

4. Abra **dois terminais**:

```bash
python consumer.py     # terminal 1 → fica escutando
python producer.py     # terminal 2 → envia 20 pedidos
```

5. Veja o terminal 1 atualizar a cada pedido → `Ctrl+C` para parar

## O fluxo

```
producer.py → tópico "pedidos" (3 partições) → consumer.py (grupo "relatorio")
```

## Conceitos em uma linha

**Tópico** → onde as mensagens ficam, como uma tabela de eventos
**Partição** → divide o tópico para processar em paralelo
**Chave** → mensagens com a mesma chave vão para a mesma partição (mantém a ordem)
**Offset** → a posição de cada mensagem na partição
**Consumer group** → consumidores do mesmo grupo dividem as partições entre si

## Testes para entender

→ Rode **dois** `consumer.py` ao mesmo tempo → as partições se dividem entre eles
→ Pare o consumer, rode o producer, suba o consumer de novo → ele continua de onde parou
→ Mude o `group.id` → o novo grupo lê tudo desde o início

## Comandos úteis

```bash
docker exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
docker exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic pedidos
docker compose down
```

## Material completo

[Guia-Kafka](https://github.com/Walterbiel/Guia-Kafka)

## QG da Engenharia de Dados

Este material é uma amostra do que você encontra no QG.

→ Trilha completa do zero ao sênior
→ Projetos reais para o portfólio
→ Comunidade para tirar dúvidas

Acesse → [qg-engenharia-de-dados.com.br](https://qg-engenharia-de-dados.com.br)
YouTube → [@gonzagadosdados](https://www.youtube.com/@gonzagadosdados)
