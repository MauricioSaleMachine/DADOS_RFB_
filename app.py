import pymysql.cursors
import os
import datetime
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- Configurações do Banco de Dados Lidas do .env ---
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', '127.0.0.1'),
    'port': int(os.environ.get('DB_PORT', 3306)),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'db': os.environ.get('DB_NAME', 'dados_barueri'), 
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    """Função que estabelece a conexão com o MySQL."""
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_cnpj', methods=['GET'])
def buscar_cnpj():
    cnpj_completo_input = request.args.get('cnpj', '')
    
    # Limpa a entrada IMEDIATAMENTE no backend, caso o frontend falhe
    cnpj_limpo = cnpj_completo_input.replace('.', '').replace('/', '').replace('-', '')

    if len(cnpj_limpo) != 14 or not cnpj_limpo.isdigit():
        # Retorno de erro consistente com o frontend (chave 'erro' minúscula)
        return jsonify({"erro": "CNPJ inválido. Digite 14 dígitos numéricos."}), 400
    
    cnpj_basico = cnpj_limpo[:8]
    cnpj_ordem = cnpj_limpo[8:12]
    cnpj_dv = cnpj_limpo[12:14]

    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            # Query com todos os campos solicitados
            sql = """
            SELECT 
                e.cnpj_basico, e.razao_social, e.natureza_juridica, e.qualificacao_responsavel, e.capital_social, e.porte_empresa,
                est.cnpj_ordem, est.cnpj_dv, est.identificador_matriz_filial, est.nome_fantasia, est.situacao_cadastral, 
                est.data_situacao_cadastral, est.motivo_situacao_cadastral, est.data_inicio_atividade, est.cnae_fiscal_principal, 
                est.tipo_logradouro, est.logradouro, est.numero, est.complemento, est.bairro, est.cep, est.ddd_1, 
                est.telefone_1, est.correio_eletronico,
                n.nome AS nome_natureza_juridica,
                c.nome AS nome_cnae_principal,
                CONCAT(est.cnpj_basico, est.cnpj_ordem, est.cnpj_dv) AS cnpj_completo 
            FROM estabelecimento est
            JOIN empresa e ON est.cnpj_basico = e.cnpj_basico
            LEFT JOIN cnae c ON est.cnae_fiscal_principal = c.codigo
            LEFT JOIN natju n ON e.natureza_juridica = n.codigo
            WHERE est.cnpj_basico = %s 
              AND est.cnpj_ordem = %s
              AND est.cnpj_dv = %s
            """

            cursor.execute(sql, (cnpj_basico, cnpj_ordem, cnpj_dv))
            resultado = cursor.fetchone()

            if resultado:
                for key, value in resultado.items():
                    if isinstance(value, datetime.date):
                        resultado[key] = value.strftime('%Y-%m-%d')
                return jsonify(resultado)
            else:
                # Retorno de mensagem consistente com o frontend (chave 'mensagem' minúscula)
                return jsonify({"mensagem": "Empresa não encontrada no banco de dados"}), 404
        
    except Exception as e:
        # Retorno de erro consistente com o frontend (chave 'erro' minúscula)
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
