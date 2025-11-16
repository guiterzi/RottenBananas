-- Limpar tabelas existentes (em ordem para não quebrar FK)
DROP TABLE IF EXISTS "Ator_Filme" CASCADE;
DROP TABLE IF EXISTS "Genero_Filme" CASCADE;
DROP TABLE IF EXISTS "Avaliacao" CASCADE;
DROP TABLE IF EXISTS "Filme" CASCADE;
DROP TABLE IF EXISTS "Usuario" CASCADE;
DROP TABLE IF EXISTS "Ator" CASCADE;
DROP TABLE IF EXISTS "Diretor" CASCADE;
DROP TABLE IF EXISTS "Genero" CASCADE;
DROP TABLE IF EXISTS "Pessoa" CASCADE;
BEGIN;

CREATE TABLE "Pessoa" (
    pessoa_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    nacionalidade VARCHAR(50)
);

CREATE TABLE "Diretor" (
    pessoa_id INT PRIMARY KEY,
    FOREIGN KEY (pessoa_id) REFERENCES "Pessoa"(pessoa_id)
);

CREATE TABLE "Ator" (
    pessoa_id INT PRIMARY KEY,
    FOREIGN KEY (pessoa_id) REFERENCES "Pessoa"(pessoa_id)
);

CREATE TABLE "Usuario" (
    usuario_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL
);


CREATE TABLE "Filme" (
    filme_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ano INT,
    duracao INT,
    sinopse TEXT,
    diretor_id INT,
    FOREIGN KEY (diretor_id) REFERENCES "Diretor"(pessoa_id)
);

CREATE TABLE "Avaliacao" (
    usuario_id INT,
    filme_id INT,
    nota INT,
    comentario TEXT,
    PRIMARY KEY (usuario_id, filme_id),
    FOREIGN KEY (usuario_id) REFERENCES "Usuario"(usuario_id),
    FOREIGN KEY (filme_id) REFERENCES "Filme"(filme_id)
);

CREATE TABLE "Genero" (
    genero_id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    classificacao VARCHAR(50)
);

CREATE TABLE "Genero_Filme" (
    genero_id INT,
    filme_id INT,
    PRIMARY KEY (genero_id, filme_id),
    FOREIGN KEY (genero_id) REFERENCES "Genero"(genero_id),
    FOREIGN KEY (filme_id) REFERENCES "Filme"(filme_id)
);

CREATE TABLE "Ator_Filme" (
    ator_id INT,
    filme_id INT,
    papel VARCHAR(100),
    PRIMARY KEY (ator_id, filme_id),
    FOREIGN KEY (ator_id) REFERENCES "Ator"(pessoa_id),
    FOREIGN KEY (filme_id) REFERENCES "Filme"(filme_id)
);

COMMIT;
