import sqlite3
from sqlite3 import Error
#Função para conectar no banco de dados
def conecta():
    try:
        con = sqlite3.connect('banco.db')
        return con
    except Error as er:
        print('Erro durante a conexão.')

def get():
    sql = 'SELECT * FROM usuario;'
    'Estabelecer a conexão com o banco de dados'
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    con.close()
    return resultado

def inserir(objeto):
    sql = f"INSERT INTO usuario VALUES (NULL, '{objeto.nome}', '{objeto.email}', '{objeto.senha}');"
    'Passos: conexão, usar a conexão, executar a instrução, fechar a conexão'
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

def atualizar(objeto):
    sql = f"UPDATE usuario SET nome='{objeto.nome}', email='{objeto.email}', senha='{objeto.senha}' WHERE id={objeto.id};"
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

def remover(id):
    sql= f'DELETE FROM usuario WHERE id={id};'
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
