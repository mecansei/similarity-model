# mecansei
## similarity-model
Este repositório realiza as ações de bootstrap do nosso modelo de similaridade e manipulação do nosso modelo.

## Ações
Em [main.py](./main.py) existem funções para manipulação do modelo, sendo elas:
- find_all_shoes(): função que seleciona todos os calçados cadastrados no nosso modelo, com seus nomes e propriedades.
- similarity(): função que recebe um id de um calçado (e.g.: _nike_casual_1_) e retornar todos os calçados que são similares a ele. Por hora, é analisado Cor (White, Red e Green) e Estilo (Casual, Social e Running).
- insert(): função que insere um calçado de teste no modelo. 
- insert_from_csv(): função que lê o csv [shoes.csv](./resources/samples/shoes.csv) e insere todas as linhas como calçado no modelo.

## Modelo
O modelo utilizado está disponível em [model-clean.ttl](./resources/models/model-clean.ttl).

## Tecnologias
Foi utilizado a ferramenta [Stardog Studio](https://www.stardog.com/studio/) para criação e manipulação do modelo.