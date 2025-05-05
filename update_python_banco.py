import pyodbc

# Configuração da conexão
DB_CONFIG = {
    'server': r'localhost\SQLEXPRESS',
    'database': 'AdventureWorks2017',
    'username': 'bredinPython',
    'password': 'asdf1234!'
}

def get_connection():
    return pyodbc.connect(
        f"DRIVER={{SQL Server}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']}"
    )

def alterar_preco(product_id, novo_preco):
    query = """
        UPDATE Production.Product
        SET ListPrice = ?
        WHERE ProductID = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (novo_preco, product_id))
        conn.commit()
        print(f"Produto {product_id} atualizado com sucesso para o preço {novo_preco}.")

if __name__ == "__main__":
    # Exemplo de uso
    product_id = 680
    novo_preco = 12.00
    alterar_preco(product_id, novo_preco)
