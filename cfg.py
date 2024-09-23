import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Carregar as variáveis de ambiente
load_dotenv('.cred')

# Configurações de conexão com o banco de dados
config = {
    'host': os.getenv('DB_HOST', 'localhost'), 
    'user': os.getenv('DB_USER'),  
    'password': os.getenv('DB_PASSWORD'),  
    'database': os.getenv('DB_NAME', 'db-revisao'),  
    'port': int(os.getenv('DB_PORT', 3306)),  
    'ssl_ca': os.getenv('SSL_CA_PATH')  
}

# Função para conectar ao banco de dados
def connect_db():
    """Estabelece a conexão com o banco de dados usando as configurações fornecidas."""
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            return conn
    except Error as err:
        print(f"Erro: {err}")
        return None