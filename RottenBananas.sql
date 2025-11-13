CREATE TABLE Pessoa (
    PessoaId INT PRIMARY KEY,
    Nome VARCHAR(100),
    DataNascimento DATE,
    Nacionalidade VARCHAR(100)
);

CREATE TABLE Ator (
    PessoaId INT PRIMARY KEY,
    FOREIGN KEY (PessoaId) REFERENCES Pessoa(PessoaId)
);

CREATE TABLE Diretor (
    PessoaId INT PRIMARY KEY,
    FOREIGN KEY (PessoaId) REFERENCES Pessoa(PessoaId)
);

CREATE TABLE Usuario (
    UsuarioId INT PRIMARY KEY,
    Nome VARCHAR(100),
    Login VARCHAR(50) UNIQUE,
    Senha VARCHAR(50)
);

CREATE TABLE Filme (
    FilmeId INT PRIMARY KEY,
    Nome VARCHAR(100),
    Ano INT,
    Duracao INT,
    Sinopse VARCHAR(255),
    DiretorId INT,
    FOREIGN KEY (DiretorId) REFERENCES Diretor(PessoaId)
);

CREATE TABLE Avaliacao (
    UsuarioId INT,
    FilmeId INT,
    Nota INT,
    Comentario VARCHAR(255),
    PRIMARY KEY (UsuarioId, FilmeId),
    FOREIGN KEY (UsuarioId) REFERENCES Usuario(UsuarioId),
    FOREIGN KEY (FilmeId) REFERENCES Filme(FilmeId)
);

CREATE TABLE Genero (
    GeneroId INT PRIMARY KEY,
    Classificacao VARCHAR(50)
);

CREATE TABLE Genero_Filme (
    GeneroId INT,
    FilmeId INT,
    PRIMARY KEY (GeneroId, FilmeId),
    FOREIGN KEY (GeneroId) REFERENCES Genero(GeneroId),
    FOREIGN KEY (FilmeId) REFERENCES Filme(FilmeId)
);

CREATE TABLE Ator_Filme (
    AtorId INT,
    FilmeId INT,
    Papel VARCHAR(100),
    PRIMARY KEY (AtorId, FilmeId),
    FOREIGN KEY (AtorId) REFERENCES Ator(PessoaId),
    FOREIGN KEY (FilmeId) REFERENCES Filme(FilmeId)
);
