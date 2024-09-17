from app.models.superadm import SuperAdmin

admin = SuperAdmin('app/controllers/db/users.json', 'app/controllers/db/cadastropet.json')

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar usuário")
    print("2. Remover usuário")
    print("3. Adicionar pet")
    print("4. Remover pet")
    print("5. Sair")
    
    choice = input("\nSua escolha: ")

    if choice == '1':
        username = input("Digite o nome de usuário: ")
        email = input("Digite o email: ")
        password = input("Digite a senha: ")
        admin.add_user(username, email, password)

    elif choice == '2':
        username = input("Digite o nome de usuário a ser removido: ")
        admin.remove_user(username)

    elif choice == '3':
        pet_data = {
            "name": input("Nome do pet: "),
            "type": input("Tipo do pet: "),
            "breed": input("Raça do pet: "),
            "age": input("Idade do pet: "),
            "description": input("Descrição do pet: "),
            "responsible": input("Nome do responsável: "),
            "cellphone": input("Telefone: "),
            "gender": input("Gênero do pet: ")
        }
        admin.add_pet(pet_data)

    elif choice == '4':
        pet_name = input("Digite o nome do pet a ser removido: ")
        admin.remove_pet(pet_name)

    elif choice == '5':
        print("Saindo...")
        break

    else:
        print("Escolha inválida. Tente novamente.")