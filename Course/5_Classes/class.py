class Carro:
    def __init__(self, marca, modelo, ano):
        # ATRIBUTOS - Caracteristicas do OBJETO
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    # MÉTODOS - funções que um objeto pode ter
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("Você precisa ligar o carro antes de acelerar.")
            
    def printCarro(self):
        print(f"Marca do carro: {self.marca}\nModelo: {self.modelo} Ano: {self.ano}")


carro_1 = Carro("Honda", "Civic", "2024")
carro_1.printCarro()
carro_1.ligar()
carro_1.acelerar(20)
carro_1.desligar()
