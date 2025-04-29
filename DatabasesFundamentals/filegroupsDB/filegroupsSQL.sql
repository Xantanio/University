-- Criação do banco de dados
CREATE DATABASE Universidade
ON PRIMARY
(
    NAME = 'universidade',
    FILENAME = 'C:\FBD\universidade.mdf',
    SIZE = 5120KB,
    FILEGROWTH = 1024KB
),
FILEGROUP fg_cursos
(
    NAME = 'cursos',
    FILENAME = 'C:\FBD\cursos.ndf',
    SIZE = 1024KB,
    FILEGROWTH = 10%
),
FILEGROUP fg_alunos
(
    NAME = 'alunos',
    FILENAME = 'C:\FBD\alunos.ndf',
    SIZE = 2048KB,
    FILEGROWTH = 15%
),
FILEGROUP fg_professores
(
    NAME = 'professores',
    FILENAME = 'C:\FBD\professores.ndf',
    SIZE = 1024KB,
    FILEGROWTH = 10%
),
FILEGROUP fg_disciplinas
(
    NAME = 'disciplinas',
    FILENAME = 'C:\FBD\disciplinas.ndf',
    SIZE = 2048KB,
    FILEGROWTH = 15%
),
FILEGROUP fg_turmas
(
    NAME = 'turmas',
    FILENAME = 'C:\FBD\turmas.ndf',
    SIZE = 3072KB,
    FILEGROWTH = 20%
)
LOG ON
(
    NAME = 'universidade_log',
    FILENAME = 'C:\FBD\universidade_log.ldf',
    SIZE = 1024KB,
    FILEGROWTH = 10%
);
GO

-- Usa o banco de dados criado
USE Universidade;
GO

-- Criação das tabelas
CREATE TABLE Curso (
    id INT PRIMARY KEY,
    nome NVARCHAR(100) NOT NULL,
    regime NVARCHAR(20) NOT NULL,
    duracao INT NOT NULL
) ON fg_cursos;

CREATE TABLE Aluno (
    id INT PRIMARY KEY,
    nome NVARCHAR(100) NOT NULL,
    curso_id INT REFERENCES Curso(id),
    semestre INT NOT NULL
) ON fg_alunos;

CREATE TABLE Professor (
    id INT PRIMARY KEY,
    nome NVARCHAR(100) NOT NULL,
    area_especializacao NVARCHAR(100) NOT NULL,
    contato NVARCHAR(100) NOT NULL,
    curso_id INT REFERENCES Curso(id)
) ON fg_professores;

CREATE TABLE Disciplina (
    id INT PRIMARY KEY,
    codigo NVARCHAR(10) UNIQUE NOT NULL,
    nome NVARCHAR(100) NOT NULL,
    area_especializacao NVARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL,
    curso_id INT REFERENCES Curso(id)
) ON fg_disciplinas;

CREATE TABLE Turma (
    id INT PRIMARY KEY,
    codigo NVARCHAR(10) UNIQUE NOT NULL,
    disciplina_id INT REFERENCES Disciplina(id),
    semestre NVARCHAR(20) NOT NULL,
    capacidade_maxima INT NOT NULL,
    estado NVARCHAR(20) NOT NULL,
    prof_id INT REFERENCES Professor(id)
) ON fg_turmas;

CREATE TABLE Aluno_Turma (
    aluno_id INT REFERENCES Aluno(id),
    turma_id INT REFERENCES Turma(id),
    PRIMARY KEY (aluno_id, turma_id)
) ON fg_turmas;
GO