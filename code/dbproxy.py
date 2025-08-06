import sqlite3


class DBProxy:

    def __init__(self, db_name: str):
        # Variável para o nome do banco de dados
        self.db_name = db_name
        # Variável para realizar a conexão com o banco - se não existir, ele cria automaticamente
        self.connection = sqlite3.connect(db_name)
        # Se não existir a tabela, criamos com as respectivas colunas
        self.connection.execute('''
                                    CREATE TABLE IF NOT EXISTS dados(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    score INTEGER NOT NULL,
                                    date TEXT NOT NULL)
                                '''
                                )

    # Função para salvar o nome, pontuação e data no banco de dados
    def save(self, score_dict: dict):
        # Insere os dados na tabela do banco de dados
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        # Como é um INSERT, precisamos comitar para salvarmos efetivamente no banco de dados
        self.connection.commit()

    # Função para mostrar os TOP 10
    def retrieve_top10(self) -> list:
        # Apenas realiza um SELECT na tabela para mostrar os 10 maiores resultados em ordem decrescente
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    # Função para fechar a conexão
    def close(self):
        # Fecha a conexão com o banco de dados
        self.connection.close()