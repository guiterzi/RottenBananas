CREATE TABLE Usuario(
UsuarioId SERIAL PRIMARY KEY,
Nome VARCHAR(50) NOT NULL CHECK(Nome <> '')
);

CREATE TABLE Diretor(
DiretorId SERIAL PRIMARY KEY,
Nome VARCHAR(50) NOT NULL CHECK (Nome <> '')
);

CREATE TABLE Genero(
GeneroId SERIAL PRIMARY KEY,
Genero VARCHAR(50) NOT NULL CHECK (Genero <> '')
);

CREATE TABLE Elenco(
ElencoId SERIAL PRIMARY KEY,
Nome VARCHAR(50) NOT NULL CHECK (Nome <> '')
);

CREATE TABLE Filme(
FilmeId SERIAL PRIMARY KEY,
Nome VARCHAR(50) NOT NULL CHECK (Nome <> ''),
Ano INT NOT NULL,
Duracao INT NOT NULL,
DiretorId INT NOT NULL,
FOREIGN KEY (DiretorId) REFERENCES Diretor(DiretorId)
);

CREATE TABLE Avaliacao(
UsuarioId INT,
FilmeId INT,
Nota INT NOT NULL,
Comentario VARCHAR(200) NOT NULL CHECK (Comentario <> ''),
PRIMARY KEY (UsuarioId,FilmeId),
FOREIGN KEY (UsuarioId) REFERENCES Usuario(UsuarioId),
FOREIGN KEY (FilmeId) REFERENCES Filme(FilmeId)
);

CREATE TABLE Elenco_Filme(
ElencoId INT,
FilmeId INT,
PRIMARY KEY (ElencoId,FilmeId),
FOREIGN KEY (ElencoId) REFERENCES Elenco(ElencoId),
FOREIGN KEY (FilmeId) REFERENCES Filme(FilmeId)
);

CREATE TABLE Filme_Genero(
FilmeId INT,
GeneroId INT,
PRIMARY KEY (FilmeId,GeneroId),
FOREIGN KEY (FilmeId) REFERENCES Filme(FilmeId),
FOREIGN KEY (GeneroId) REFERENCES Genero(GeneroId)
);


INSERT INTO Diretor (Nome) VALUES ('DiretorTeste1');
INSERT INTO Diretor (Nome) VALUES ('JOAO SILVA');

INSERT INTO Filme (Nome, Ano, Duracao, DiretorId) VALUES ('Didi', 2000, 120, 1);
INSERT INTO Filme (Nome, Ano, Duracao, DiretorId) VALUES ('TITANIC', 2000, 120, 1);
INSERT INTO Usuario (Nome) VALUES ('UsuarioTeste1');
INSERT INTO Usuario (Nome) VALUES ('UsuarioTeste2');
INSERT INTO Usuario (Nome) VALUES ('UsuarioTeste5');
INSERT INTO Usuario (Nome) VALUES ('UsuarioTeste3');
INSERT INTO Avaliacao (UsuarioId, FilmeId, Nota, Comentario) VALUES (1, 1, 10, 'Filme Otimo');
INSERT INTO Avaliacao (UsuarioId, FilmeId, Nota, Comentario) VALUES (1, 2, 7, 'Gostei do filme adsfghadfgasdfg');
INSERT INTO Avaliacao (UsuarioId, FilmeId, Nota, Comentario) VALUES (2, 2, 2, 'Muito ruim');

