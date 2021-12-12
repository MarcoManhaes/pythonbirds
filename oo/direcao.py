class Direcao:
    def __init__(self):
        self.posicoes = ("Norte", "Leste", "Sul", "Oeste")
        self.direcao_atual = 0

    def girar_a_direita(self):
        self.direcao_atual += 1
        self.direcao_atual = min(3, self.direcao_atual)

        #if self.direcao_atual > 3:
            #self.direcao_atual = 0

    def girar_a_esquerda(self):
        self.direcao_atual -= 1
        self.direcao_atual = max(-3, self.direcao_atual)

        ##if self.direcao_atual < -3:
            ##self.direcao_atual = 0


if __name__ == '__main__':
    d = Direcao()
    print(d.direcao_atual)

    d.girar_a_direita()
    print(d.direcao_atual)

    d.girar_a_direita()
    print(d.direcao_atual)

    d.girar_a_direita()
    print(d.direcao_atual)

    d.girar_a_direita()
    print(d.direcao_atual)

    d.girar_a_esquerda()
    print(d.direcao_atual)

    d.girar_a_esquerda()
    print(d.direcao_atual)

    d.girar_a_esquerda()
    print(d.direcao_atual)

    d.girar_a_esquerda()
    print(d.direcao_atual)
