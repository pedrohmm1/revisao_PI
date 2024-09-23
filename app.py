from cfg import *

app = Flask(__name__)


##### ROTAS PARA CLIENTES #####

@app.route('/clientes', methods=['POST'])
def cadastra_cliente():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    entrada_dados = request.json
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO `tbl_clientes` (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)'
        values = (entrada_dados['nome'], entrada_dados['email'], entrada_dados['cpf'], entrada_dados['senha'])
        cursor.execute(sql, values)
        conn.commit()
        cliente_id = cursor.lastrowid
        resp = {'message': "Cliente cadastrado com sucesso!", 'cliente_id': cliente_id}
        return jsonify(resp), 201

    except Error as err:
        return jsonify({'error': f"Erro ao inserir cliente: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/clientes', methods=['GET'])
def lista_clientes():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = 'SELECT * FROM tbl_clientes'
        cursor.execute(sql)
        clientes = cursor.fetchall()
        return jsonify(clientes), 200

    except Error as err:
        return jsonify({'error': f"Erro ao listar clientes: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/clientes/<int:id>', methods=['GET'])
def busca_cliente_id(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tbl_clientes WHERE id = %s"
        cursor.execute(sql, (id,))
        cliente = cursor.fetchone()
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({'message': 'Cliente não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao buscar cliente: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/clientes/<int:id>', methods=['PUT'])
def atualiza_cliente(id):
    entrada_dados = request.json
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = "UPDATE tbl_clientes SET nome = %s, email = %s, cpf = %s, senha = %s WHERE id = %s"
        values = (entrada_dados['nome'], entrada_dados['email'], entrada_dados['cpf'], entrada_dados['senha'], id)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Cliente atualizado com sucesso'}), 200
        else:
            return jsonify({'message': 'Cliente não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao atualizar cliente: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/clientes/<int:id>', methods=['DELETE'])
def deleta_cliente(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = 'DELETE FROM tbl_clientes WHERE id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Cliente deletado com sucesso'}), 200
        else:
            return jsonify({'message': 'Cliente não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao deletar cliente: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


##### ROTAS PARA FORNECEDORES #####

@app.route('/fornecedores', methods=['POST'])
def cadastra_fornecedor():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    entrada_dados = request.json
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO `tbl_fornecedores` (nome, email, cnpj) VALUES (%s, %s, %s)'
        values = (entrada_dados['nome'], entrada_dados['email'], entrada_dados['cnpj'])
        cursor.execute(sql, values)
        conn.commit()
        fornecedor_id = cursor.lastrowid
        resp = {'message': "Fornecedor cadastrado com sucesso!", 'fornecedor_id': fornecedor_id}
        return jsonify(resp), 201

    except Error as err:
        return jsonify({'error': f"Erro ao inserir fornecedor: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/fornecedores', methods=['GET'])
def lista_fornecedores():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = 'SELECT * FROM tbl_fornecedores'
        cursor.execute(sql)
        fornecedores = cursor.fetchall()
        return jsonify(fornecedores), 200

    except Error as err:
        return jsonify({'error': f"Erro ao listar fornecedores: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/fornecedores/<int:id>', methods=['GET'])
def busca_fornecedor_id(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tbl_fornecedores WHERE id = %s"
        cursor.execute(sql, (id,))
        fornecedor = cursor.fetchone()
        if fornecedor:
            return jsonify(fornecedor), 200
        else:
            return jsonify({'message': 'Fornecedor não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao buscar fornecedor: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/fornecedores/<int:id>', methods=['PUT'])
def atualiza_fornecedor(id):
    entrada_dados = request.json
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = "UPDATE tbl_fornecedores SET nome = %s, email = %s, cnpj = %s WHERE id = %s"
        values = (entrada_dados['nome'], entrada_dados['email'], entrada_dados['cnpj'], id)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Fornecedor atualizado com sucesso'}), 200
        else:
            return jsonify({'message': 'Fornecedor não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao atualizar fornecedor: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/fornecedores/<int:id>', methods=['DELETE'])
def deleta_fornecedor(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = 'DELETE FROM tbl_fornecedores WHERE id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Fornecedor deletado com sucesso'}), 200
        else:
            return jsonify({'message': 'Fornecedor não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao deletar fornecedor: {err}"}), 400

    finally:
        cursor.close()
        conn.close()

###### ROTAS PARA PRODUTOS ########## 

@app.route('/produtos', methods=['POST'])
def cadastra_produtos():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    entrada_dados = request.json
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO `tbl_produtos` (nome, descricao, preco, qtd_em_estoque, fornecedor_id, custo_no_fornecedor) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (
            entrada_dados['nome'],
            entrada_dados['descricao'],
            entrada_dados['preco'],
            entrada_dados['qtd_em_estoque'],
            entrada_dados['fornecedor_id'],
            entrada_dados['custo_no_fornecedor']
        )
        cursor.execute(sql, values)
        conn.commit()
        produto_id = cursor.lastrowid
        resp = {'message': "Produto cadastrado com sucesso!", 'produto_id': produto_id}
        return jsonify(resp), 201

    except Error as err:
        return jsonify({'error': f"Erro ao inserir produto: {err}"}), 400

    finally:
        cursor.close()
        conn.close()

@app.route('/produtos', methods=['GET'])
def lista_produtos():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = 'SELECT * FROM tbl_produtos'
        cursor.execute(sql)
        produtos = cursor.fetchall()
        return jsonify(produtos), 200

    except Error as err:
        return jsonify({'error': f"Erro ao listar produtos: {err}"}), 400

    finally:
        cursor.close()
        conn.close()

@app.route('/produtos/<int:id>', methods=['GET'])
def busca_produto_id(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tbl_produtos WHERE id = %s"
        cursor.execute(sql, (id,))
        produto = cursor.fetchone()
        if produto:
            return jsonify(produto), 200
        else:
            return jsonify({'message': 'Produto não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao buscar produto: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/produtos/<int:id>', methods=['PUT'])
def atualiza_produtos(id):
    entrada_dados = request.json
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = "UPDATE tbl_produtos SET nome = %s, descricao = %s, preco = %s, qtd_em_estoque = %s, fornecedor_id = %s, custo_no_fornecedor = %s WHERE id = %s"
        values = (
            entrada_dados['nome'],
            entrada_dados['descricao'],
            entrada_dados['preco'],
            entrada_dados['qtd_em_estoque'],
            entrada_dados['fornecedor_id'],
            entrada_dados['custo_no_fornecedor'], 
            id
            )
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Produto atualizado com sucesso'}), 200
        else:
            return jsonify({'message': 'Produto não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao atualizar produtos: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/produtos/<int:id>', methods=['DELETE'])
def deleta_produtos(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = 'DELETE FROM tbl_produtos WHERE id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Produto deletado com sucesso'}), 200
        else:
            return jsonify({'message': 'Produto não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao deletar produto: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


###### ROTAS PARA CARRINHO ########

@app.route('/carrinhos', methods=['POST'])
def cadastra_carrinho():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    entrada_dados = request.json
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO `tbl_carrinho` (produto_id, quantidade) VALUES (%s, %s)'
        values = (entrada_dados['produto_id'], entrada_dados['quantidade'])
        cursor.execute(sql, values)
        conn.commit()
        carrinho_id = cursor.lastrowid
        resp = {'message': "Item adicionado no carrinho com sucesso!", 'carrinho_id': carrinho_id}
        return jsonify(resp), 201

    except Error as err:
        return jsonify({'error': f"Erro ao inserir item no carrinho: {err}"}), 400

    finally:
        cursor.close()
        conn.close()

@app.route('/carrinhos', methods=['GET'])
def lista_carrinhos():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = 'SELECT * FROM tbl_carrinho'
        cursor.execute(sql)
        carrinhos = cursor.fetchall()
        return jsonify(carrinhos), 200

    except Error as err:
        return jsonify({'error': f"Erro ao listar carrinhos: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/carrinhos/<int:id>', methods=['GET'])
def busca_carrinho_id(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tbl_carrinho WHERE id = %s"
        cursor.execute(sql, (id,))
        carrinho = cursor.fetchone()
        if carrinho:
            return jsonify(carrinho), 200
        else:
            return jsonify({'message': 'Carrinho não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao buscar carrinho: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/carrinhos/<int:id>', methods=['PUT'])
def atualiza_carrinho(id):
    entrada_dados = request.json
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = "UPDATE tbl_carrinho SET produto_id = %s, quantidade = %s WHERE id = %s"
        values = (entrada_dados['produto_id'], entrada_dados['quantidade'], id)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Carrinho atualizado com sucesso'}), 200
        else:
            return jsonify({'message': 'Carrinho não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao atualizar carrinho: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/carrinhos/<int:id>', methods=['DELETE'])
def deleta_carrinho(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor()
        sql = 'DELETE FROM tbl_carrinho WHERE id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount:
            return jsonify({'message': 'Carrinho deletado com sucesso'}), 200
        else:
            return jsonify({'message': 'Carrinho não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao deletar carrinho: {err}"}), 400

    finally:
        cursor.close()
        conn.close()

@app.route('/carrinhos/cliente/<int:cliente_id>', methods=['GET'])
def lista_carrinhos_por_cliente(cliente_id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        SELECT tbl_carrinho.id, tbl_carrinho.produto_id, tbl_carrinho.quantidade
        FROM tbl_carrinho
        INNER JOIN tbl_pedido ON tbl_carrinho.id = tbl_pedido.carrinho_id
        WHERE tbl_pedido.cliente_id = %s
        """
        cursor.execute(sql, (cliente_id,))
        carrinhos = cursor.fetchall()

        if carrinhos:
            return jsonify(carrinhos), 200
        else:
            return jsonify({'message': 'Nenhum carrinho encontrado para este cliente'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao listar carrinhos: {err}"}), 400

    finally:
        cursor.close()
        conn.close()

##### ROTAS PARA PEDIDOS #####

@app.route('/pedidos', methods=['POST'])
def cadastra_pedido():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    entrada_dados = request.json
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO `tbl_pedido` (cliente_id, carrinho_id, status) VALUES (%s, %s, %s)'
        values = (entrada_dados['cliente_id'], entrada_dados['carrinho_id'], entrada_dados['status'])
        cursor.execute(sql, values)
        conn.commit()
        pedido_id = cursor.lastrowid
        return jsonify({'message': "Pedido cadastrado com sucesso!", 'pedido_id': pedido_id}), 201

    except Error as err:
        return jsonify({'error': f"Erro ao inserir pedido: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/pedidos', methods=['GET'])
def lista_pedidos():
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = 'SELECT * FROM tbl_pedido'
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        return jsonify(pedidos), 200

    except Error as err:
        return jsonify({'error': f"Erro ao listar pedidos: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/pedidos/<int:id>', methods=['GET'])
def busca_pedido_id(id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tbl_pedido WHERE id = %s"
        cursor.execute(sql, (id,))
        pedido = cursor.fetchone()
        if pedido:
            return jsonify(pedido), 200
        else:
            return jsonify({'message': 'Pedido não encontrado'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao buscar pedido: {err}"}), 400

    finally:
        cursor.close()
        conn.close()


@app.route('/pedidos/cliente/<int:cliente_id>', methods=['GET'])
def busca_pedidos_por_cliente(cliente_id):
    conn = connect_db()
    if not conn:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM tbl_pedido WHERE cliente_id = %s"
        cursor.execute(sql, (cliente_id,))
        pedidos = cursor.fetchall()

        if pedidos:
            return jsonify(pedidos), 200
        else:
            return jsonify({'message': 'Nenhum pedido encontrado para este cliente'}), 404

    except Error as err:
        return jsonify({'error': f"Erro ao buscar pedidos: {err}"}), 400

    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    app.run(debug=True)

        
        
