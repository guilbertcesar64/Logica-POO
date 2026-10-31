class Carro:
    def __init__(self, marca, modelo, ano):
        # Os atributos guardam as características de cada carro.
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibirInfo(self):
        # TODO 1: substitua pass por um print() que mostre marca, modelo e ano.
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")


# TODO 2: crie DOIS objetos usando a classe Carro.
carro1 = Carro("Chevrolet", "Onix plus", 2024)
carro2 = Carro("Fiat", "Fastback", 2024)


# TODO 3: chame exibirInfo() para os DOIS objetos criados.
carro1.exibirInfo()
carro2.exibirInfo()
