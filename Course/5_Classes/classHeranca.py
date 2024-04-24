class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O veículo está ligado.")
        else:
            print("O veículo já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O veículo está desligado.")
        else:
            print("O veículo já está desligado.")

    def acelerar(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O veículo acelerou para {self.velocidade} km/h.")
        else:
            print("Você precisa ligar o veículo antes de acelerar.")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Número de Portas: {self.num_portas}")


# Criando um carro
meu_carro = Carro("Toyota", "Corolla", 2020, 4)

# Exibindo informações do carro
meu_carro.exibir_informacoes()

# Ligando o carro
meu_carro.ligar()

# Acelerando o carro
meu_carro.acelerar(20)

# Desligando o carro
meu_carro.desligar()
