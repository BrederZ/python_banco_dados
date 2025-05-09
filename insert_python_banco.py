import pyodbc
import random
import string
from conexao_banco import get_connection

def gerar_product_number(cursor):
    while True:
        # Gera algo do tipo: XX-XXXX-XX ou similar
        part1 = ''.join(random.choices(string.ascii_uppercase, k=2))
        part2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(3, 5)))
        part3 = ''.join(random.choices(string.digits, k=random.choice([0, 2])))
        
        if part3:
            numero = f"{part1}-{part2}-{part3}"
        else:
            numero = f"{part1}-{part2}"

        # Checa se já existe
        cursor.execute("""
            SELECT COUNT(*) FROM Production.Product WHERE ProductNumber = ?
        """, (numero,))
        (exists,) = cursor.fetchone()
        if exists == 0:
            return numero

def criar_produto(set_name, set_color, set_price, set_weight):
    query = """
        INSERT INTO Production.Product(
            Name,
            ProductNumber,
            MakeFlag,
            FinishedGoodsFlag,
            Color,
            SafetyStockLevel,
            ReorderPoint,
            StandardCost,
            ListPrice,
            Size,
            SizeUnitMeasureCode,
            WeightUnitMeasureCode,
            Weight,
            DaysToManufacture,
            ProductLine,
            Class,
            Style,
            ProductSubcategoryID,
            ProductModelID,
            SellStartDate,
            SellEndDate,
            DiscontinuedDate,
            rowguid,
            ModifiedDate
        )
        VALUES (
            ?, ?, 1, 1, ?, 500, 250, 1200.50, ?, 'L', 'CM', 'KG', ?, 
            3, 'M', 'H', 'U', 4, 12, GETDATE(), NULL, NULL, NEWID(), GETDATE()
        )
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            product_number = gerar_product_number(cursor)
            cursor.execute(query, (
                set_name, product_number, set_color, set_price, set_weight
            ))
            conn.commit()
            print("\n🎉✨ Novo produto criado com sucesso! ✨🎉")
            print(f"🆕 Nome: {set_name}")
            print(f"🔢 ProductNumber: {product_number}")
            print(f"🎨 Cor: {set_color}")
            print(f"💰 Preço: ${set_price}")
            print(f"⚖️ Peso: {set_weight} kg")
            print("\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Seu item já está disponível no banco de dados!\n")

if __name__ == "__main__":
    set_name = 'Seu Jorge'
    set_color = 'Preto'
    set_price = 77.77
    set_weight = 70.0

    criar_produto(set_name, set_color, set_price, set_weight)
