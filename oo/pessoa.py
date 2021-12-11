class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

if __name__ == '__main__':
    Junior = Pessoa(nome='Júnior', idade=39)
    Dilma = Pessoa(Junior, nome='Dilma', idade=60)
    Junior.olhos = 1
    print(Dilma.cumprimentar())
    print(Dilma.nome)
    print(Dilma.idade)
    for filho in Dilma.filhos:
        print(filho.nome)
        print(filho.idade)

    Dilma.sobrenome = "Menezes"
    print(Dilma.__dict__)
    print(Junior.__dict__)
    print(id(Pessoa.olhos), id(Dilma.olhos), id(Junior.olhos))
