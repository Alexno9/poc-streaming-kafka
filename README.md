# BigBoss Streaming

A proposta deste projeto é simular os dados gerados de um web scrapping em anúncios imobiliários de diversos sites. O foco é construir uma arquitetura que seja capaz de realizar a ingestão/carga destes dados de maneira eficiente e conscistente.

### Sumário
  - Tecnologias utilizadas no projeto
  - Papéis de cada ferramenta
  - Instalação do projeto para teste
  - Desenvolvimento
  - Como melhorar..
  - Links e Referências


### Tecnologias

A arquitetura em streaming é composta das seguintes ferramentas:

* [Docker] - Virtualização de nível de S.O. para entregar software em pacotes chamados contêineres;
* [Apache Kafka] - Plataforma open-source de eventos distribuidos em streaming;
* [Apache Zookeeper] - Serviço centralizado que mantém informação da configuração, nomeações, sincronizações e pode prover grupos de serviços;
* [Apache Nifi] - Projetado para automatizar o fluxo de dados distribuídos entre sistemas;
* [Faker lib] - Biblioteca disponível para python que gera dados aleatórios e localizados;
* [Python] - Linguagem de programação de alto nível;
* [Apache Spark] - Motor de processamento distribuído;
* [Elasticsearch] - Mecanismo de busca e análise de dados distribuído;
* [Kibana] - Interface de Usuário para visualizar dados do Elasticsearch.

### Papeis de cada Ferramenta

Nesta prova de conceito, nem todas as ferramentas foram utilizadas. Como o objetivo era a simulação de captura de anúncios, as ferramentas que compõe esse processo são:

| Ferramenta | Função |
| ------ | ------ |
| Kafka | Criação do tópico e execução do prod./consu. |
| Python | Construção do Producer executado pelo Kafka |
| Faker lib | Biblioteca que gera os dados falsos |
| Nifi | Orquestra os consumers do kafka e faz o processo de carga |
| Elasticsearch | Recebe a carga e armazena de maneira rápida |
| Kibana | Visualização dos índices e construção de Dashs |

### Instalação

Este projeto requer o docker instalado na máquina para rodar.
Siga este link para instalação no seu ambiente preferido: https://docs.docker.com/get-docker/

Este projeto foi executado em um Ubuntu 20:
Realize o download do arquivo 'docker-compose.yml' para uma pasta na sua máquina.
Navegue até a pasta onde foi colocado o 'docker-compose.yml'.
Execute os comandos abaixo e observe os containers iniciando...

```sh
$ cd 'caminho onde se encontra o arquivo'
$ docker-compose up -d # -d roda o comando em background
$ docker-compose logs -f # -f mostra os logs desde o início
$ Ctrl-C para o processo
```
O Docker nos da a possibilidade de pausar/tirar de pause, parar/iniciar a execução dos containers logo depois de construidos:
```sh
$ docker-compose pause
$ docker-compose unpause

# após o 'up' nos containers, use start/stop para controlar os mesmos
$ docker-compose stop
$ docker-compose start
```

Com os containers ativos é possível visualizar o que está rodando e quais as imagens e suas versões foram utilizadas...

```sh
$ docker-compose ps
$ docker-compose images
```

Com o comando ps é possível visualizar quais são as portas que cada container utiliza para se comunicar com o ambiente externo.
Caso queira alterar alguma porta de um container específico, vá até o arquivo 'docker-compose.yml' com qualquer editor de texto e mude as mesmas na sessão 'ports:'

### Desenvolvimento

##### Criação e produção dos dados
#
Com as ferramentas em funcionamento, podemos partir para os dados. 
Optamos por simular dados de anúncio devido a restrição atual de algumas empresas que disponibilizam anúncios de imóveis. Você é limitado a requisição de seus próprios anúncios, necessitando de autorização de outros anunciantes caso queira buscar seus anúncios.

Utilizamos a biblioteca Faker para geração dos dados falsos, com ele é possível:
- Gerar dados em diversas localizações diferentes;
- Sem limites no quesito quantidade de dados gerados;
- Geração de nomes e sobrenomes, endereços, codigos postais, idade, telefones;
- Liberdade de construir os próprios geradores a partir de valores passados por parâmetro.

Exemplo do objeto 'anúncio' construído com o Faker:
```sh
$ {
   "titulo": "",
   "endereco": {
     "rua": "",
     "bairro": "",
     "complemento": "",
     "cep": "",
     "cidade": "",
     "estado": ""
   },
   "preco": 123,
   "preco_cond": 10,
   "iptu": 100,
   "lote": {
     "largura": 6,
     "comprimento": 30,
     "total": 180
   },
   "quartos": 3,
   "garagem": 2,
   "banheiros": 2,
   "caracteristicas": [
     ""
   ],
   "descricao": "",
   "anuciante": {
     "nome": "",
     "telefone": "",
     "cresci": ""
   }
 }
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Links e Referências
##### Docker
- https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b
- https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421
- https://towardsdatascience.com/big-data-managing-the-flow-of-data-with-apache-nifi-and-apache-kafka-af674cd8f926
##### Nifi & Kafka
- https://community.cloudera.com/t5/Community-Articles/Integrating-Apache-NiFi-and-Apache-Kafka/ta-p/247433
- https://blogs.apache.org/nifi/entry/integrating_apache_nifi_with_apache
##### Kafka
- https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster/#:~:text=Therefore%2C%20in%20general%2C%20the%20more,consumption%20(call%20it%20c).
##### Elasticsearch
- https://medium.com/@anselmoborges/lab-nifi-elasticseach-parte-1-3fa0bab4126d


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Docker]: <https://www.docker.com/>
   [Apache Kafka]: <https://kafka.apache.org/>
   [Apache Zookeeper]: <https://zookeeper.apache.org/>
   [Apache Nifi]: <https://nifi.apache.org/>
   [Faker lib]: <https://faker.readthedocs.io/en/master/>
   [Python]: <https://www.python.org/>
   [Apache Spark]: <https://spark.apache.org/>
   [Elasticsearch]: <https://www.elastic.co/pt/elasticsearch/>
   [Kibana]: <https://www.elastic.co/pt/kibana>
