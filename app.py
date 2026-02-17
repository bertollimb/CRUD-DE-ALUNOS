from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# 1 Conectar com DB
def conecta_db():
    conexao = sqlite3.connect('banco.db')
    return conexao

# 2 Inserir Dados
def inserir_dados(nome, idade, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO alunos(nome, idade, nota)

            VALUES (?, ?, ?)
        """, (nome, idade, nota)
    )

    conexao.commit()
    conexao.close()

# 3 Listagem de Dados
def obter_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
    conexao.close()
    return dados

# 4 Atualizar
def atualizar_dados_parcial(id, nome=None, idade=None, nota=None):
    conexao = conecta_db()
    cursor = conexao.cursor()

    campos = []
    valores = []

    if nome is not None and nome != "":
        campos.append("nome = ?")
        valores.append(nome)

    if idade is not None:
        campos.append("idade = ?")
        valores.append(idade)

    if nota is not None:
        campos.append("nota = ?")
        valores.append(nota)

    # Se não houver campos para atualizar, só retorna
    if not campos:
        conexao.close()
        print("Nada para atualizar")
        return

    query = f"UPDATE alunos SET {', '.join(campos)} WHERE id = ?"
    valores.append(id)

    cursor.execute(query, valores)
    conexao.commit()
    conexao.close()
    print("Dados atualizados")


# 5 Excluir Dados
def excluir_dados(id):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
            DELETE FROM alunos
            WHERE id = ?
        """, (id,)
    )
    conexao.commit()
    conexao.close()
    print("Dados excluidos")

# -------------------------------
# ROTAS GET - exibir páginas
# -------------------------------

@app.route('/')
def home():
    alunos = obter_dados()
    return render_template('index.html', alunos=alunos)

@app.route('/adicionar')
def form_adicionar():
    return render_template('adicionar.html')

@app.route('/atualizar')
def form_atualizar():
    alunos = obter_dados()
    return render_template('atualizar.html', alunos=alunos)

@app.route('/excluir')
def form_excluir():
    alunos = obter_dados()
    return render_template('excluir.html', alunos=alunos)

#------- ROTAS POST - processar dados -------------


@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    idade = int(request.form.get('idade'))
    nota = float(request.form.get('nota'))
    inserir_dados(nome, idade, nota)
    alunos = obter_dados()
    return render_template('index.html', alunos=alunos)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    id = int(request.form['id'])
    nome = request.form.get('nome', '')
    idade = request.form.get('idade', '')
    nota = request.form.get('nota', '')

    idade = int(idade) if idade else None
    nota = float(nota) if nota else None

    atualizar_dados_parcial(id, nome, idade, nota)
    alunos = obter_dados()
    return render_template('atualizar.html', alunos=alunos)

@app.route('/excluir', methods=['POST'])
def excluir():
    id = int(request.form['id'])
    excluir_dados(id)                                                                   
    alunos = obter_dados()
    return render_template('excluir.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)