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

def deletar_produto(product_id):
    query = """
        DELETE FROM Production.Product
        WHERE ProductID = ?
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (product_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"🗑️ Produto {product_id} deletado com sucesso!")
            return True
        else:
            print(f"⚠️ Produto {product_id} não encontrado. Nenhuma exclusão realizada.")
            return False


