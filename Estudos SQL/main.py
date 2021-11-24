import db

menu = """
1. Cadastrar Aluno
2. Cadastrar Disciplina
3. Consultar Aluno
4. Consultar Disciplina
5. Fazer Matrícula
6. Exibir Matrículas

Escolha uma das opções: 
"""

def cadastro_a():
    nome_aluno = input('Digite o nome completo do aluno que será cadastrado: ').split()
    nome = nome_aluno[0]
    surname = nome_aluno[1]
    db.add_student(nome, surname)

def cadastro_d():
    codigo_disciplina = input('Digite o código da nova disciplina a ser cadastrada: ')
    nome_disciplina = input('Digite o nome da nova disciplina: ')
    professor = input('Digite a matrícula do professor da nova disciplina: ')
    db.add_disciplinas(codigo_disciplina, nome_disciplina, professor)

def consulta_a():
    retorno = db.select_student()
    print('ID | Nome | Sobrenome')
    for i in retorno:
        print(f'{i[0]} | {i[1]} | {i[2]}\n')

def consulta_d():
    retorno = db.mostrar_disciplinas()
    print('Cd. | Nome | Matricula Professor')
    for i in retorno:
        print(f'{i[0]} | {i[1]} | {i[2]}\n')

def matricular():
    matricula_aluno = input('Digite a matrícula do aluno: ')
    codigo_disciplina = input('Digite o código da discplina: ')
    db.do_subjects(matricula_aluno, codigo_disciplina)

def exibir_matriculas():
    while True:
        escolha_matricula = input('Digite 1 para exibir as disciplinas cursadas por um alunos.'
                                  '\n Digite 2 para exibir os alunos cursando determinada disciplina.')
        if escolha_matricula == '1':
            pesquisa = input('Digite a matrícula do aluno: ')
            break
        elif escolha_matricula == '2':
            pesquisa = input('Digite o código da disciplina: ')
            break
        else:
            print('Entrada inválida.')

    retorno = db.mostrar_matriculas(escolha_matricula, pesquisa)
    print('Disciplina. | Aluno |')
    for i in retorno:
        print(f'{i[0]} | {i[1]}\n')


db.create_tables()

while True:
    print(menu)
    nav = str(input())
    if nav == '1':
        cadastro_a()
    elif nav == '2':
        cadastro_d()
    elif nav == '3':
        consulta_a()
    elif nav == '4':
        consulta_d()
    elif nav == '5':
        matricular()
    elif nav == '6':
        exibir_matriculas()

