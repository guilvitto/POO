class Pessoa():
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo=False
        self.falando=False

    def comer(self,x):
        if self.falando:
            print(f"{self.nome} não pode  comer falando.")
            return
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        print(f"{self.nome} está comendo um {x}")
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo=False

    def falar(self):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo.")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        print(f"{self.nome} está falando.")
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return
        print(f"{self.nome} parou de falar.")
        self.falando=False
