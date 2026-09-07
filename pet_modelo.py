import csv

class Pet:
    def __init__(self, nome, especie, idade, peso, dono):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.dono = dono
        
    def exibir_dados(self):
        return f"Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade} | Peso: {self.peso} | Dono: {self.dono}"


with open("pets.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    
    next(leitor) 
    
    for linha in leitor:
        
        Pets = Pet(
            nome = linha[0],
            especie = linha[1],
            idade = int(linha[2]),
            peso = float(linha[3]),
            dono = linha[4],
            
        )
        
        print(Pets.exibir_dados())
        
