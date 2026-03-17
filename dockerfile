# 1. Imagem base leve (Python Slim) para performance e segurança
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Evita que o Python gere arquivos .pyc e permite logs em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Instala dependências do sistema (se necessário)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 5. Copia apenas o arquivo de requisitos primeiro (otimiza o cache do Docker)
COPY requirements.txt .

# 6. Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copia o restante do código da aplicação
COPY . .

# 8. Expõe a porta que o FastAPI usa
EXPOSE 8000

# 9. Comando para iniciar o servidor Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]