import datetime
import json
import time

from confluent_kafka import Producer
from faker import Faker

# -------------------------------------------------------------------------------------------------------------------- #
#                                                    Configurações                                                     #
# -------------------------------------------------------------------------------------------------------------------- #

# Inicializar o Faker
#Faker.seed(123456) Rodar o faker no modo aleatório
fake = Faker(['pt_BR'])

# Quantidade para inserir: 200 mil
max = 200000

# Quantidade de itens gerados a cada flush
step = 1000

# Sleep entre cada passo de geração
step_ts = 0.1  # em segundos

# Endereço (ip + porta) do kafka
#kafka_bootstrap_servers = 'my-cluster-kafka-0.my-cluster-kafka-brokers.kafka.svc:9092'
kafka_bootstrap_servers = 'broker:29092'

# Nome do tópico no kafka
kafka_topic = 'diario'

# -------------------------------------------------------------------------------------------------------------------- #
#                                                   Modelo de dados                                                    #
# -------------------------------------------------------------------------------------------------------------------- #

# {
#   "titulo": "",
#   "endereco": {
#     "rua": "",
#     "bairro": "",
#     "complemento": "",
#     "cep": "",
#     "cidade": "",
#     "estado": ""
#   },
#   "preco": 123,
#   "preco_cond": 10,
#   "iptu": 100,
#   "lote": {
#     "largura": 6,
#     "comprimento": 30,
#     "total": 180
#   },
#   "quartos": 3,
#   "garagem": 2,
#   "banheiros": 2,
#   "caracteristicas": [
#     ""
#   ],
#   "descricao": "",
#   "anuciante": {
#     "nome": "",
#     "telefone": "",
#     "cresci": ""
#   }
# }

tipo_apto = 'apartamento'
tipo_casa = 'casa'

tipos = [tipo_casa, tipo_apto]

caracteristicas = [
    'ar condicionado',
    'área de serviço',
    'porcelanato',
    'rodapé embutido',
    'cozinha americana',
    'armário embutido'
]

caracteristicas_apt = caracteristicas + [
    '1 vaga coberta',
    'elevador',
    'varanda',
    'porteiro 24 horas',
    'área de lazer'
]


# -------------------------------------------------------------------------------------------------------------------- #
#                                                       Geração                                                        #
# -------------------------------------------------------------------------------------------------------------------- #

total = 0

p = Producer({'bootstrap.servers': kafka_bootstrap_servers})

for idx in range(max):
    items = []

    for sidx in range(step):
        tipo = fake.random_choices(tipos, 1)

        lista_selecionada = []
        if tipo == tipo_casa:
            lista_selecionada = caracteristicas
        else:
            lista_selecionada = caracteristicas_apt

        qtd_selecoes = fake.random_int(0, len(lista_selecionada))
        lista_caracts = fake.random_elements(lista_selecionada, qtd_selecoes, unique=True)

        item = {
            'titulo': '',
            'tipo': tipo,
            'endereco': {
                'rua': fake.street_name(),
                'numero': fake.building_number(),
                'cep': fake.postcode(),
                'bairro': fake.bairro(),
                'cidade': fake.city(),
                'estado': fake.estado_nome()
            },
            'preco': fake.random_int(120000, 500000, 10000),
            'preco_cond': fake.random_int(100, 500, 50),
            'iptu': fake.random_int(500, 2000, 25),
            'lote': {
                'largura': fake.random_int(6, 15, 1),
                'comprimento': fake.random_int(6, 50, 2),
                'total': 0
            },
            'quartos': fake.random_int(1, 4, 1),
            'garagem': fake.random_int(1, 2, 1),
            'banheiros': fake.random_int(1, 3, 1),
            'caracteristicas': lista_caracts,
            'descricao': '',
            'anunciante': {
                'nome': fake.first_name(),
                'telefone': fake.cellphone_number(),
                'cresci': ''
            }
        }

        item['lote']['total'] = item['lote']['largura'] * item['lote']['comprimento']

        items.append(item)

        item_json = json.dumps(item).encode('utf-8')
        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above, or flush() below, when the message has
        # been successfully delivered or failed permanently.
        p.produce(kafka_topic, item_json)

        if total >= max:
            break

    # end inner step for

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()

    total += len(items)
    dtstr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'[{dtstr}] --> {len(items)} (total: {total})')

    if total >= max:
        break

    time.sleep(step_ts)

exit(42)
