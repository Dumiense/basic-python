class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'nome: {self.nome} - {self.ano} - {self.likes} likes '

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
            return f'nome: {self.nome}, {self.duracao}m- {self.ano} - {self.likes} likes '

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
            return f'nome: {self.nome}, {self.temporadas}T - {self.ano} - {self.likes} likes '

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho (self):
        return len(self.programas)

vingadores = Filme('vingaroes', 2018, 160)
the_oficce = Serie('the oficce', 2003, 9)
tmep = Filme("td mundo em panico", 2002, 99)
mof = Serie('morden family', 2009, 12)
mib = Filme('man in black', 1999, 120)

tmep.dar_like()
mof.dar_like()
mof.dar_like()
mof.dar_like()
vingadores.dar_like()

titulos = [vingadores, the_oficce, mof, tmep]

fds = Playlist('fim de semana', titulos)

for programa in fds:
    print(programa)