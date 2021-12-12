class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_super = super().cumprimentar()
        return f'{cumprimentar_super}. Aperto de mão.'

if __name__ == '__main__':
    Junior = Homem(nome='Júnior', idade=39)
    Dilma = Pessoa(Junior, nome='Dilma', idade=60)
    Junior.olhos = 1
    print(Dilma.cumprimentar())
    print(Dilma.nome)
    print(Dilma.idade)
    for filho in Dilma.filhos:
        print(filho.cumprimentar())
        print(filho.nome)
        print(filho.idade)

    Dilma.sobrenome = "Menezes"
    print(Dilma.__dict__)
    print(Junior.__dict__)
    print(id(Pessoa.olhos), id(Dilma.olhos), id(Junior.olhos))
    print(Pessoa.metodo_estatico(), Dilma.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), Dilma.nome_e_atributos_de_classes())

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Junior, Homem))
