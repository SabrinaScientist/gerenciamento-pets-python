# principal.py
from pet_funcoes import carregar_pets_csv, adicionar_novos_pets, buscar_pet

def main():
    lista_pets = carregar_pets_csv()

    adicionar_novos_pets(lista_pets)
    
    while True:
        print("\n" + "="*30)
        print("1 - Listar pets")
        print("2 - Buscar pet")
        print("3 - Encerrar sistema")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n--- Pets Cadastrados ---")
            for pet in lista_pets:
                print(pet.exibir_dados())
        elif opcao == '2':
            nome = input("Digite o nome do pet para buscar: ")
            buscar_pet(nome, lista_pets)
        elif opcao == '3':
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
