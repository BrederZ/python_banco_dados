from flask import Flask, request, jsonify
from insert_python_banco import criar_produto
from select_python_banco import visualizar_produto, visualizar_produtos
from update_python_banco import alterar_preco
from delete_python_banco import deletar_produto

# Configuração da API Flask
app = Flask(__name__)

@app.route('/produto', methods=['GET'])
def visualizar_produto_request():
    name = request.args.get('name')
    product_id = request.args.get('product_id')
    if not name and not product_id:
        produto = visualizar_produtos()
        return jsonify({'data': produto, 'mensagem': 'Consulta realizada com sucesso.'}), 200
    produto = visualizar_produto(name, product_id)
    return jsonify({'data': produto, 'mensagem': 'Consulta realizada com sucesso.'}), 200


@app.route('/produto', methods=['PATCH'])
def update_produto():
    data = request.json
    product_id = data.get('product_id')
    novo_preco = data.get('novo_preco')
    
    if product_id is None or novo_preco is None:
        return jsonify({'error': 'Os parâmetros "product_id" e "novo_preco" são obrigatórios.'}), 400

    alterar_preco(product_id, novo_preco)
    return jsonify({'mensagem': f'Produto {product_id} atualizado com sucesso para o preço {novo_preco}.'}), 200

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
