import sqlite3 as lite

def criar():
    #criando banca de dado
    ban = lite.connect("dado.db")
    curso = ban.cursor()
    curso.execute("CREATE TABLE IF NOT EXISTS usuarios(ID INTEGER PRIMARY KEY,nome TEXT,email TEXT)")
    ban.close()


def adicionar(nome="sem nome ",email = "sem email"):
    ban = lite.connect("dado.db")
    curso = ban.cursor()
    curso.execute("INSERT INTO usuarios(nome,email)VALUES(?,?)",(nome,email))
    ban.commit()
    ban.close()
    print("cadastro feito com sucessor")


def vertabela():
    ban = lite.connect("dado.db")
    curso = ban.cursor()
    curso.execute("SELECT * FROM usuarios")
    dado = curso.fetchall()
    for c in range(0,len(dado)):
        print(f"{dado[c][0]} - {dado[c][1]} - {dado[c][2]}")

    ban.close()

def excluir(tabela,codicao):
    ban = lite.connect("dado.db")
    curso = ban.cursor()
    curso.execute(f"DELETE FROM {tabela} WHERE ID = ?",(codicao,))
    ban.commit()
    ban.close()


criar()
while True:
    print("=" * 30)
    print("""opções
    (1)adicionar
    (2)remover
    (3)ver
    (4)sair""")
    print("=" * 30)
    opcao = int(input("digite uma opção: "))
    print("=" * 30)
    match opcao:

        case 1:
            nome = str(input("digite o nome: "))
            email = str(input("digite o email: "))
            adicionar(nome,email)

        case 2:
            escolha = int(input("digite o id que deseja apagar: "))
            excluir("usuarios",escolha)

        case 3:
            vertabela()

        case 4:
            print("saindo...")
            break
        case _:
            print("ERRO.OPÇÃO INVALIDA")