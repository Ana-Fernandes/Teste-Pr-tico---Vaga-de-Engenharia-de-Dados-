# Coleta de Dados Climáticos com Python e PostgreSQL

Este projeto tem como objetivo coletar dados climáticos da API **OpenWeatherMap**, realizar um tratamento básico desses dados (como limpeza e normalização), e armazená-los em um banco de dados **PostgreSQL**. A aplicação é implementada em **Python**, utilizando bibliotecas como `requests`, `pandas`, e `SQLAlchemy`.

## 💡 Descrição

- O script realiza uma requisição à API do OpenWeatherMap usando uma chave de API.
- Os dados coletados incluem: nome da cidade, temperatura, umidade, descrição do clima, velocidade do vento e a data e hora da coleta.
- Esses dados são então processados, padronizados e armazenados em um banco de dados **PostgreSQL**.
- A tabela no banco de dados tem a seguinte estrutura: `cidade`, `temperatura`, `umidade`, `descricao`, `velocidade_vento`, e `data_coleta`.

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **OpenWeatherMap API**: Fonte de dados climáticos.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados.
- **SQLAlchemy**: ORM para interagir com o PostgreSQL.
- **Pandas**: Para processamento e manipulação dos dados.
- **python-dotenv**: Para carregar variáveis de ambiente como a chave da API.

## 🛠️ Instalação e Uso

Siga os passos abaixo para rodar este projeto em sua máquina local:

1. Clone o repositório e entre no diretório:

```bash
git clone https://github.com/Ana-Fernandes/Teste-Pr-tico---Vaga-de-Engenharia-de-Dados-.git
cd clima_api

2. Edite o arquivo .env
Edite um arquivo chamado .env no mesmo diretório do projeto e adicione a chave da sua API OpenWeatherMap e o URL do banco de dados PostgreSQL:

API_KEY=sua_chave_openweathermap
DB_URL=postgresql://postgres:senha@localhost:5432/nome_do_banco
3. Instale as dependências
Com o pip (gerenciador de pacotes do Python), instale as dependências listadas no requirements.txt:


pip install -r requirements.txt

4. Crie a tabela no PostgreSQL
No seu banco de dados PostgreSQL, crie a tabela clima_atual com a seguinte estrutura:

sql

CREATE TABLE clima_atual (
    cidade VARCHAR(100),
    temperatura FLOAT,
    umidade INT,
    descricao TEXT,
    velocidade_vento FLOAT,
    data_coleta TIMESTAMP
);
Você pode fazer isso usando o PgAdmin ou rodando o comando no psql.

5. Execute o script
Agora, basta rodar o script Python para coletar os dados e armazená-los no banco de dados:


python main.py
O script irá gerar uma saída similar a esta:


      cidade  temperatura  umidade         descricao  velocidade_vento         data_coleta
0  São Paulo        25.76       53  scattered c![Captura de tela 2025-05-07 145332](https://github.com/user-attachments/assets/2079e2bf-8efe-48a4-927e-0b8b4304d9ca)
![Captura de tela 2025-05-07 143730](https://github.com/user-attachments/assets/ad25c21a-016a-4169-82e4-0ad0d60bf90b)
louds              2.68 2025-05-07 14:12:04
Dados salvos com sucesso no banco de dados.

