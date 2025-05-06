from flask import Flask, request, jsonify
from insert_python_banco import criar_produto
from select_python_banco import buscar_produto_dinamico, visualizar_produtos
from update_python_banco import alterar_preco
from delete_python_banco import deletar_produto

# Configuração da API Flask
app = Flask(__name__)

# Rota para visualizar produtos
@app.route('/produto', methods=['GET'])
def visualizar_produto_request():
    termo = request.args.get('termo')

    if not termo:
        # Se não passar termo, retorna todos os produtos
        produto = visualizar_produtos()
        return jsonify({'data': produto, 'mensagem': 'Consulta geral: todos os produtos.'}), 200
    
    # Se passar termo, faz busca inteligente
    produto = buscar_produto_dinamico(termo)
    return jsonify({'data': produto, 'mensagem': f'Consulta realizada com o termo: "{termo}".'}), 200

# Rota para atualizar o preço de um produto
@app.route('/produto', methods=['PATCH'])
def update_produto():
    data = request.json
    product_id = data.get('product_id')
    novo_preco = data.get('novo_preco')
    
    if product_id is None or novo_preco is None:
        return jsonify({'error': 'Os parâmetros "product_id" e "novo_preco" são obrigatórios.'}), 400

    alterar_preco(product_id, novo_preco)
    return jsonify({'mensagem': f'Produto {product_id} atualizado com sucesso para o preço {novo_preco}.'}), 200

# Rota para criar um novo produto
@app.route('/produto', methods=['POST'])
def create_produto():
    data = request.json
    set_name = data.get('name')
    set_color = data.get('color')
    set_price = data.get('price')
    set_weight = data.get('weight')

    if not all([set_name, set_color, set_price, set_weight]):
        return jsonify({'error': 'Todos os parâmetros são obrigatórios.'}), 400

    criar_produto(set_name, set_color, set_price, set_weight)
    return jsonify({'mensagem': 'Produto criado com sucesso!'}), 201

# Rota para deletar um produto
@app.route('/produto', methods=['DELETE'])
def delete_produto():
    data = request.json
    product_id = data.get('product_id')
    
    if product_id is None:
        return jsonify({'error': 'O parâmetro "product_id" é obrigatório.'}), 400

    sucesso = deletar_produto(product_id)
    if not sucesso:
        return jsonify({'mensagem': f'Produto {product_id} não encontrado ou já excluido anteriomente. Nenhuma exclusão realizada.'}), 404
    return jsonify({'mensagem': f'Produto {product_id} deletado com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
