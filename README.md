📊 DADOS_RFB_

Repositório para extração, tratamento e integração dos Dados Abertos da Receita Federal do Brasil (RFB), com foco na base de CNPJ (Cadastro Nacional da Pessoa Jurídica). // Trabalho relacionado à Fatec Barueri

Este projeto contém scripts para baixar, processar e inserir grandes volumes de dados CSV da RFB em um banco de dados relacional, permitindo análises detalhadas de empresas, sócios e outras informações públicas liberadas pela Receita. 
Serviços e Informações do Brasil
+1

🧠 Visão Geral

A Receita Federal do Brasil disponibiliza conjuntos de dados abertos em formatos estruturados (CSV, JSON, XML, etc.) acessíveis para download direto ou via portal de dados abertos. 
Serviços e Informações do Brasil

Este repositório realiza o processo de:

📥 Baixar os arquivos públicos da RFB

📤 Descompactar e organizar os dados

🧹 Ler e tratar registros brutos

🗃️ Inserir tudo em um banco de dados relacional (ex.: MariaDB/MySQL)

📊 Gerar estrutura de tabelas pronta para análise

🚀 Funcionalidades

✔ Download automatizado dos dados públicos
✔ Extração e transformação para banco de dados
✔ Estrutura de tabelas com índices
✔ Suporte a grandes volumes (GBs de dados)
✔ Compatível com análises econômicas, mercadológicas e fiscais

🧩 Estrutura de Tabelas Geradas

Ao final do processo de ETL, as seguintes tabelas serão criadas (com base nos dados públicos da RFB):

Tabela	Conteúdo
empresa	Dados cadastrais da matriz
estabelecimento	Informações por unidade (endereço, telefone etc.)
socios	Sócios das empresas
simples	Informações sobre Simples Nacional e MEI
cnae	Códigos e descrições de atividades econômicas
quals	Qualificação dos sócios
natju	Natureza jurídica
moti	Motivos de situação cadastral
pais	Países de origem
munic	Municípios do Brasil

🔎 As tabelas que contêm grande volume têm índices criados para a coluna cnpj_basico para performance. 
GitHub

🛠️ Pré-requisitos

Certifique-se de ter o seguinte instalado:

🐍 Python 3.x

🗄️ Banco de dados relacional (recomendado MariaDB / MySQL)

📦 Bibliotecas Python (via requirements.txt)

📦 Instalação

Clone este repositório:

```bash

git clone https://github.com/MauricioSaleMachine/DADOS_RFB_.git
cd DADOS_RFB_

```


Instale dependências:
```bash

pip install -r requirements.txt

```
Configure seu banco de dados:

Inicie sua instância do MariaDB/MySQL

Crie um banco para receber os dados

Tenha um .env com variáveis de conexão (ex.: DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

Execute o script principal do ETL:

python ETL_coletar_dados_e_gravar_BD.py


ℹ️ Os arquivos da base podem ser enormes — em projetos similares, downloads chegam a dezenas de GB compactados. 
GitHub

🗂️ Organização de Arquivos

```bash 
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── NOVOLAYOUTDOSDADOSABERTOSDOCNPJ.pdf    # Layout oficial dos CSVs
├── Dados_RFB_ERD.png                       # Diagrama entidade-relacionamento
├── DADOS_RFB.log                           # Log de execução (exemplo)
└── ETL_coletar_dados_e_gravar_BD.py        # Script principal de ETL 

```

❓ Como Contribuir

Este projeto é open-source e aceitamos contribuições!
Você pode:

🛠️ Abrir issues com sugestões ou bugs

🚀 Enviar pull requests com melhorias

📚 Atualizar documentação ou adicionar exemplos

📄 Licença

Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais detalhes.

📌 Referências

Dados abertos da Receita Federal do Brasil — formatos estruturados para download. 
Serviços e Informações do Brasil

Portal de Dados Abertos da RFB com diversas bases públicas disponíveis. 
Serviços e Informações do Brasil
