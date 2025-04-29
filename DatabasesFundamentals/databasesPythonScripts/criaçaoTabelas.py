import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.execute("""
                CREATE TABLE IF NOT EXISTS Curso (
                    id integer PRIMARY KEY,
                    nome varchar(100),
                    regime varchar(20),
                    duracao integer)
                """)
        
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Aluno (
                    id integer PRIMARY KEY,
                    nome varchar(100),
                    curso_id integer REFERENCES Curso(id),
                    semestre integer)
                """)
        
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Professor (
                    id integer PRIMARY KEY,
                    nome varchar(100),
                    area_especializacao varchar(100),
                    contato varchar(100),
                    curso_id integer REFERENCES Curso(id))
                """)
        
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Disciplina (
                    id integer PRIMARY KEY,
                    codigo varchar(10) UNIQUE,
                    nome varchar(100),
                    area_especializacao varchar(100),
                    carga_horaria integer,
                    curso_id integer REFERENCES Curso(id))
                """)
        
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Turma (
                    id integer PRIMARY KEY,
                    codigo varchar(10) UNIQUE,
                    disciplina_id integer REFERENCES Disciplina(id),
                    semestre varchar(20),
                    capacidade_maxima integer,
                    estado varchar(20),
                    prof_id integer REFERENCES Professor(id))
                """)
        
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Aluno_Turma (
                    aluno_id integer REFERENCES Aluno(id),
                    turma_id integer REFERENCES Turma(id),
                    PRIMARY KEY (aluno_id, turma_id))
                """)
        
        conn.commit()