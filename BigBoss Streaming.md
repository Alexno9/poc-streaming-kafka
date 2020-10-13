# BigBoss Streaming

Simular web scrapping de anúncios imobiliários em diversos sites.
Os dados de anúncio tem periodicidade entre 5 até 10 dias.

  - Utilização de uma arquitetura streaming
  - Os dados são fakes e produzidos em larga escala
  - Não foram realizadas etapas de transformação


### Tecnologias

A arquitetura em streaming é composta das seguintes ferramentas:

* [Docker]
* [Apache Kafka]
* [Apache Zookeeper]
* [Apache Nifi]
* [Faker lib]
* [Python]
* [Apache Spark]
* [Elasticsearch]
* [Kibana]


### Instalação

Este projeto requer o docker instalado na máquina para rodar.
Siga este link para instalação no seu ambiente preferido: https://docs.docker.com/get-docker/

Este exemplo foi feito em um linux.
1 - Realize o download do arquivo 'docker-compose.yml' para uma pasta na sua máquina.
2 - Navegue até a pasta onde foi colocado o 'docker-compose.yml'.
3 - Execute os comandos abaixo e observe os containers iniciando...
```sh
$ cd 'caminho onde se encontra o arquivo'
$ docker-compose up -d # -d roda o comando em background
$ docker-compose logs -f # -f mostra os logs desde o início
$ Ctrl-C para o processo
```

Com os containers ativos é possível visualizar o que está rodando e quais as imagens e suas versões foram utilizadas...

```sh
$ docker-compose ps
$ docker-compose images
```

Com o comando ps é possível visualizar quais são as portas que cada container utiliza para se comunicar com o ambiente externo.
Caso queira alterar alguma porta de um container específico, vá até o arquivo 'docker-compose.yml' com qualquer editor de texto e mude as mesmas na sessão 'ports:'

### Papeis de cada Ferramenta

Nesta prova de conceito, nem todas as ferramentas foram utilizadas. Como o objetivo era a simulação de captura de anúncios, as ferramentas que compõe esse processo são:

| Ferramenta | Função |
| ------ | ------ |
| Kafka | Criação do tópico e execução do prod./consu. |
| Python | Construção do Producer executado pelo Kafka |
| Faker lib | Biblioteca que gera os dados falsos |
| Nifi | Cria os consumers do kafka e faz o processo de carga |
| Elasticsearch | Recebe a carga e armazena de maneira rápida |
| Kibana | Visualização dos índices e construção de Dashs |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
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

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


**Free Software, Hell Yeah!**

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
