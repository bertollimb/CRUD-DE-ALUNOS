import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
cursor.execute(
    """
        CREATE TABLE alunos(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        nota REAL NOT NULL
        )
    """
)

conexao.close()
print('Tabela criada')
