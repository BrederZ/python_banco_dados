import pyodbc
from conexao_banco import get_connection

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


