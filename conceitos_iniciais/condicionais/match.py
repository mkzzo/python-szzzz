opcao = int(input("Escolha de 1 a 3"))

match opcao:
    case 1:
        print ("Escolheu a opcao 1!")
    case 2:
        print ("Escolheu a opcao 2!")
    case 3:
        print ("Escolheu a opcao 3")
    case _:
        print ("Escolhe uma válida")