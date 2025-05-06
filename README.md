Purpose of the Repository
This repository appears to be focused on implementing a Python-based system for interacting with a SQL Server database, specifically the "AdventureWorks2017" database. It provides functionality to create, read, update, and delete (CRUD) product records using Python and Flask for API endpoints. Although the README file is unavailable, the repository structure and code suggest its purpose is to demonstrate or facilitate database operations programmatically.

Features and Technologies Used
Technologies: The repository predominantly uses Python (100%) and integrates with SQL Server using pyodbc. Flask is employed to expose APIs for database operations.
Features:
Database Connectivity: Functions establish connections to the SQL Server using credentials stored in a dictionary (DB_CONFIG).
CRUD Operations:
Insert: insert_python_banco.py provides methods to add new products, including generating unique product numbers.
Select: select_python_banco.py retrieves product details and exports them to JSON.
Update: update_python_banco.py allows updates to product pricing.
Delete: delete_python_banco.py enables product removal.
API Endpoints: A Flask application (main.py) exposes RESTful endpoints for each CRUD operation, making the system accessible via HTTP requests.
This repository is a practical example of combining Python, Flask, and SQL Server for database management and API development.
____________________________________________________________________________________________________________________________________
Propósito do Repositório
Este repositório tem como objetivo implementar um sistema em Python para interação com um banco de dados SQL Server, especificamente o "AdventureWorks2017". Ele oferece funcionalidades para realizar operações CRUD (criar, ler, atualizar e deletar) em registros de produtos, utilizando APIs RESTful desenvolvidas com Flask. Embora o arquivo README não esteja disponível, a análise do código sugere que o repositório é voltado para aprendizado ou automação de operações em bancos de dados.

Recursos e Tecnologias Utilizadas
Tecnologias: O repositório utiliza Python (100%) e a biblioteca pyodbc para conexão com o SQL Server. O Flask é empregado para criar a API REST.
Recursos:
Conexão com Banco de Dados: O código configura conexões com o SQL Server utilizando credenciais armazenadas em um dicionário (DB_CONFIG).
Operações CRUD:
Inserção: O arquivo insert_python_banco.py contém métodos para adicionar novos produtos, incluindo a geração de números únicos para cada produto.
Consulta: O arquivo select_python_banco.py permite visualizar produtos e exportar os dados em formato JSON.
Atualização: O arquivo update_python_banco.py permite modificar o preço dos produtos.
Exclusão: O arquivo delete_python_banco.py possibilita a remoção de produtos do banco.
API REST: O código no arquivo main.py expõe endpoints REST para cada operação CRUD, permitindo a interação via HTTP.
Este repositório é um exemplo prático de como combinar Python, Flask e SQL Server para gerenciar bancos de dados e criar APIs.
