import motor
import direcao

class Carro:
    def __init__(self, motor=None, direcao=None):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def calcular_direcao(self):
        print(self.direcao.posicoes[self.direcao.direcao_atual])

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


if __name__ == '__main__':
    m = motor.Motor()
    print(m.velocidade)

    m.acelerar()
    m.velocidade

    m.acelerar()
    m.velocidade

    m.acelerar()
    m.velocidade

    m.frear()
    m.velocidade

    m.frear()
    m.velocidade

    d = direcao.Direcao()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_direita()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_direita()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_direita()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_direita()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_esquerda()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_esquerda()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_esquerda()
    print(d.posicoes[d.direcao_atual])

    d.girar_a_esquerda()
    print(d.posicoes[d.direcao_atual])

    c = Carro(m, d)
    c.calcular_velocidade()

    c.acelerar()
    c.calcular_velocidade()

    c.acelerar()
    c.calcular_velocidade()

    c.frear()
    c.calcular_velocidade()

    c.calcular_direcao()

    c.girar_a_direita()
    c.calcular_direcao()

    c.girar_a_esquerda()
    c.calcular_direcao()

    c.girar_a_esquerda()
    c.calcular_direcao()