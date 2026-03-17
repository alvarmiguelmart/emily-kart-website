# Backend Lead Capture - AWS LocalStack Integration

Este projeto consiste em uma infraestrutura de backend para captura de dados, integrando uma interface frontend a uma API RESTful conteinerizada que utiliza serviços de nuvem simulados.

## Especificações Técnicas
- Linguagem: Python 3.11
- Framework: FastAPI
- SDK: Boto3 (AWS SDK para Python)
- Containerização: Docker e Docker Compose
- Infraestrutura Local: LocalStack (Simulação de AWS DynamoDB)
- Frontend: Integração via Fetch API

## Arquitetura e Implementação
O projeto demonstra o ciclo completo de uma requisição backend:
1. Interface: O frontend captura dados via formulário e realiza uma chamada assíncrona.
2. API: O servidor FastAPI processa os dados, gerencia as políticas de CORS e estabelece conexão com a camada de persistência.
3. Persistência: Os dados são armazenados em uma tabela NoSQL no DynamoDB.
4. DevOps: Toda a stack é orquestrada via Docker Compose, permitindo que a infraestrutura de banco de dados seja provisionada localmente através do LocalStack, eliminando custos de nuvem durante a fase de desenvolvimento e testes.

## Procedimentos de Execução

1. Requisitos: Possuir o Docker Desktop instalado e ativo.
2. Inicialização: Executar o comando no diretório raiz:
   docker-compose up --build
3. Configuração do Banco: Com os containers em execução, acessar http://localhost:8000/docs e utilizar o endpoint /criar-tabela para inicializar a estrutura do DynamoDB.
4. Interface: Abrir o arquivo index.html no navegador para realizar os testes de integração.

## Endpoints Principais
- GET /: Verificação de status da API.
- POST /criar-tabela: Provisionamento da tabela no DynamoDB local.
- POST /salvar-lead: Persistência de dados enviados pelo frontend.
