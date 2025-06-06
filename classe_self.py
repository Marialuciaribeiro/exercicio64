class Pessoa:
    def _int_(self, nome , idade):
        self.nome = nome
        self.idade = idade

    def apresentar (self):
        print(f"olá , meu nome é {self.nome} e eu tenho{self.idade} anos.")


pessoa1 = Pessoa("Fellipe", 36)
pessoa2 = Pessoa("Maria" 25)


pessoa1.apresentar()
pessoa2.apresentar()
