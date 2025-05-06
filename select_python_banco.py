import json
from conexao_banco import get_connection  # ajuste se o nome do arquivo de conexão for diferente

def visualizar_produtos():
    query = """
        SELECT ProductID, Name, ListPrice, Color, Weight
        FROM Production.Product
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def buscar_produto_dinamico(termo):
    query = """
        SELECT ProductID, Name, ListPrice, Color, Weight
        FROM Production.Product
        WHERE
            CAST(ProductID AS NVARCHAR) LIKE ?
            OR Name LIKE ?
            OR Color LIKE ?
            OR CAST(ListPrice AS NVARCHAR) LIKE ?
            OR CAST(Weight AS NVARCHAR) LIKE ?
    """
    like_term = f"%{termo}%"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (like_term, like_term, like_term, like_term, like_term))
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Salvar em arquivo JSON
    with open('produtos.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, default=str, ensure_ascii=False)

    return(results)
