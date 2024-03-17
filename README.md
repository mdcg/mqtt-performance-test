# mqtt-performance-test

## Dependências

- Python 3.11
- Docker e Docker Compose

## Configuração inicial

Existe um arquivo localizado na pasta `config` chamado `.env-example`, que deverá ser utilizado como base para a criação de um arquivo `.env` no mesmo local. O arquivo `.env` será carregado na inicialização dos containers do Docker injetando todas as variáveis de ambiente necessárias para configuração dos mesmos.

## Rodando o sistema localmente

Antes de mais nada, é extremamente aconselhável que você utilize uma virtualenv antes de instalar as dependências do sistema. Com a virtualenv ativada, execute o seguinte comando para instalar as dependências do projeto:

```bash
make poetry/setup
make poetry/install
```

Só é necessário executar os comandos acima uma única vez.

Para iniciarlizar os containers com o Eclipse Mosquitto MQTT Broker e o InfluxDB, execute:

```bash
docker-compose up
```

PS: Caso você queira deixar os containers rodando em background, adicione a flag `-d` ao final do comando.

Para inicializar o subscriber:

```bash
make start/subscriber-worker
```

Para inicializar o publisher:

```bash
make start/publisher-worker
```

## Acessando as métricas

Para acessar o InfluxDB e verificar as métricas do publisher e do subscriber, abra o navegador e acesse [http://localhost:8086/](http://localhost:8086/). Será solicitado as credenciais de autenticação, estas por sua vez podem ser encontradas no arquivo `config/.env` (**INFLUXDB_USERNAME** e **INFLUXDB_PASSWORD**). No menu lateral acesse "Explore" e filtre as métricas como desejar.
