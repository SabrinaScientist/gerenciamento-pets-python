# pet_funcoes.py
from pet_modelo import Pet

def carregar_pets_csv():
    lista_pets = []
    try:
        with open("pets.csv", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            linhas = conteudo.strip().split('\n')
            
            for linha in linhas[1:]:
                if linha:
                    dados = linha.split(',')
                    novo_pet = Pet(
                        nome=dados[0],
                        especie=dados[1],
                        idade=int(dados[2]),
                        peso=float(dados[3]),
                        dono=dados[4]
                    )
                    lista_pets.append(novo_pet)
    except FileNotFoundError:
        print("Arquivo 'pets.csv' não encontrado.")
        
    return lista_pets

def adicionar_novos_pets(lista_pets):
    pet_estrela = Pet("Estrela", "Cachorro", 4, 10.2, "Fernanda")
    pet_bob = Pet("Bob", "Cachorro", 1, 6.5, "Ricardo")
    
    lista_pets.append(pet_estrela)
    lista_pets.append(pet_bob)

def buscar_pet(nome_busca, lista_pets):
    encontrado = False
    for pet in lista_pets:
        if pet.nome.strip().lower() == nome_busca.strip().lower():
            print(pet.exibir_dados())
            encontrado = True
            break
            
    if not encontrado:
        print("Pet não localizado.")