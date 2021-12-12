class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade <= 2
        self.velocidade = max(0, self.velocidade)




if __name__ == '__main__':
    m = Motor()
    print(m.velocidade)

    m.acelerar()
    print(m.velocidade)

    m.acelerar()
    print(m.velocidade)

    m.acelerar()
    print(m.velocidade)

    m.frear()
    print(m.velocidade)

    m.frear()
    print(m.velocidade)