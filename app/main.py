import os
from fastapi import FastAPI
import boto3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AWS Local")

# Configuração para conectar no LocalStack ou AWS Real
DYNAMODB_URL = os.getenv("DYNAMODB_URL", None)

def get_dynamo_resource():
    # Se houver uma URL de ambiente (LocalStack), usamos ela
    if DYNAMODB_URL:
        return boto3.resource('dynamodb', endpoint_url=DYNAMODB_URL, region_name="us-east-1")
    return boto3.resource('dynamodb')

@app.get("/")
def home():
    return {"status": "Online", "contexto": "Backend/DevOps Project"}

@app.post("/criar-tabela")
def criar_tabela():
    dynamo = get_dynamo_resource()
    try:
        table = dynamo.create_table(
            TableName='Leads',
            KeySchema=[{'AttributeName': 'email', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'email', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        return {"mensagem": "Tabela Leads criada com sucesso no DynamoDB!"}
    except Exception as e:
        return {"erro": str(e)}
    
# ... (abaixo do app = FastAPI())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que sua Landing Page acesse a API
    allow_methods=["*"],
    allow_headers=["*"],
)