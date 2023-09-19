import main as menu

def main():
    nomePet = input("Qual o nome do seu pet: ")
    pet = menu.PetF(nomePet)

    while True:
        print("\n-----------------------")
        pet.mostrarStatus()
        print("\nO que você gostaria de fazer?")
        print("1: Alimentar")
        print("2: Brincar")
        print("3: Descansar")
        print("4: Procurar emprego")
        print("5: Sair")
        escolha = input("> ")

        if escolha == "1":
            pet.alimentar()
        elif escolha == "2":
            pet.brincar()
        elif escolha == "3":
            pet.descansar()
        elif escolha == "4":
            pet.escolherEmprego()
        elif escolha == "5":
            print(f"Tchau! Cuide bem de {nomePet}!")
            break
        else:
            print("Opção inválida!")
        
        pet.passarTempo()

if __name__ == "__main__":
    main()