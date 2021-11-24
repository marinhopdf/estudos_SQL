import sqlite3

CREATE_ALUNOS_TABLE = """
CREATE TABLE IF NOT EXISTS alunos (id_aluno INTEGER PRIMARY KEY, first_name TEXT, surname TEXT);
"""

CREATE_DISCIPLINAS_TABLE = """
CREATE TABLE IF NOT EXISTS disciplinas (id_disciplina INTEGER PRIMARY KEY, nome_disciplina TEXT, professor TEXT);
"""

CREATE_MATRICULAS_TABLE = """
CREATE TABLE IF NOT EXISTS matriculas (
alunos_id INTEGER,
disciplinas_id INTEGER,
FOREIGN KEY (alunos_id) REFERENCES alunos(id_aluno)
FOREIGN KEY (disciplinas_id) REFERENCES disciplinas(id_disciplina)
);
"""

CREATE_ADD_STUDENT = """
INSERT INTO alunos (first_name, surname) VALUES (?,?);
"""

ADD_SUBJECTS = """
INSERT INTO disciplinas (id_disciplina, nome_disciplina, professor) VALUES (?,?,?);
"""

ADD_MATRICULAS = """
INSERT INTO matriculas (alunos_id, disciplinas_id) VALUES (?,?);
"""

SELECT_STUDENT = """
SELECT * FROM alunos;
"""

SELECT_DISCIPLINAS = """
SELECT * FROM disciplinas
"""

SELECT_MATRICULAS_ALUNOS = """
SELECT disciplinas.nome_disciplina, alunos.first_name
FROM disciplinas JOIN matriculas
ON matriculas.disciplinas_id = disciplinas.id_disciplina
JOIN alunos ON alunos.id_aluno = matriculas.alunos_id
WHERE alunos.id_aluno = ?
;
"""

SELECT_MATRICULAS_DISCIPLINAS = """
SELECT disciplinas.nome_disciplina, alunos.first_name
FROM disciplinas JOIN matriculas
ON matriculas.disciplinas_id = disciplinas.id_disciplina
JOIN alunos ON alunos.id_aluno = matriculas.alunos_id
WHERE disciplinas.id_disciplina = ?
;
"""

connection = sqlite3.connect('database.db')

def create_tables():
    with connection:
        connection.execute(CREATE_ALUNOS_TABLE)
        connection.execute(CREATE_DISCIPLINAS_TABLE)
        connection.execute(CREATE_MATRICULAS_TABLE)

def add_student(nome, surname):
    with connection:
        connection.execute(CREATE_ADD_STUDENT, (nome, surname))

def add_disciplinas(codigo_disciplina, nome_disc, prof):
    with connection:
        connection.execute(ADD_SUBJECTS, (codigo_disciplina, nome_disc, prof))

def do_subjects(matricula_aluno, codigo_disciplina):
    with connection:
        connection.execute(ADD_MATRICULAS, (matricula_aluno, codigo_disciplina))

def select_student():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_STUDENT)
        return cursor.fetchall()

def mostrar_disciplinas():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_DISCIPLINAS)
        return cursor.fetchall()

def mostrar_matriculas(escolha_matricula, pesquisa):
    with connection:
        if escolha_matricula == '1':
           cursor = connection.cursor()
           cursor.execute(SELECT_MATRICULAS_ALUNOS, (pesquisa,))
           return cursor.fetchall()
        elif escolha_matricula == '2':
            cursor = connection.cursor()
            cursor.execute(SELECT_MATRICULAS_DISCIPLINAS, (pesquisa,))
            return cursor.fetchall()