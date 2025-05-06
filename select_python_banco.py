import pyodbc
import json

# Parâmetros de conexão
DB_CONFIG = {
    'server': r'localhost\SQLEXPRESS',
    'database': 'AdventureWorks2017',
    'username': 'bredinPython',
    'password': 'asdf1234!'
}

def get_connection(config):
    return pyodbc.connect(
        f"DRIVER={{SQL Server}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['username']};"
        f"PWD={config['password']}"
    )
def visualizar_produtos():
    query = """
        SELECT ProductID, Name, ListPrice, Color, Weight
        FROM Production.Product
        """
    with get_connection(DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Exibir JSON formatado no terminal
    json_output = json.dumps(results, indent=4, default=str)
    print(json_output)

    # Salvar em arquivo JSON
    with open('produtos.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, default=str, ensure_ascii=False)

    return(results)

def visualizar_produto(name, product_id):
    
    query = """
        SELECT ProductID, Name, ListPrice, Color, Weight
        FROM Production.Product
        WHERE Name LIKE ? or ProductID = ?
    """
    with get_connection(DB_CONFIG) as conn:
        cursor = conn.cursor()
        cursor.execute(query, (f'%{name}%', product_id))
        
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Exibir JSON formatado no terminal
    json_output = json.dumps(results, indent=4, default=str)
    print(json_output)

    # Salvar em arquivo JSON
    with open('produtos.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, default=str, ensure_ascii=False)

    return(results)
