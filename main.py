from flask import Flask, request, jsonify
from select_python_banco import visualizar_produto
from update_python_banco import alterar_preco
from delete_python_banco import deletar_produto

# Configuração da API Flask
app = Flask(__name__)

@app.route('/produto', methods=['GET'])
def visualizar_produto_request():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'O parâmetro "name" é obrigatório.'}), 400
    produto = visualizar_produto(name)
    return jsonify({'data': produto, 'mensagem': 'Consulta realizada com sucesso.'}), 200

@app.route('/produto/update', methods=['POST'])
def update_produto():
    data = request.json
    product_id = data.get('product_id')
    novo_preco = data.get('novo_preco')
    
    if product_id is None or novo_preco is None:
        return jsonify({'error': 'Os parâmetros "product_id" e "novo_preco" são obrigatórios.'}), 400

    alterar_preco(product_id, novo_preco)
    return jsonify({'mensagem': f'Produto {product_id} atualizado com sucesso para o preço {novo_preco}.'}), 200

@app.route('/produto/delete', methods=['DELETE'])
def delete_produto():
    data = request.json
    product_id = data.get('product_id')
    
    if product_id is None:
        return jsonify({'error': 'O parâmetro "product_id" é obrigatório.'}), 400

    sucesso = deletar_produto(product_id)
    if sucesso:
        return jsonify({'mensagem': f'Produto {product_id} deletado com sucesso!'}), 200
    else:
        return jsonify({'mensagem': f'Produto {product_id} não encontrado. Nenhuma exclusão realizada.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
