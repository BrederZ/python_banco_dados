from flask import Flask, request, jsonify
from select_python_banco import visualizar_produto

# Configuração da API Flask
app = Flask(__name__)

@app.route('/produto', methods=['GET'])
def visualizar_produto_request():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'O parâmetro "name" é obrigatório.'}), 400
    produto = visualizar_produto(name)
    return jsonify({'data': produto, 'mensagem': 'Consulta realizada com sucesso.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
