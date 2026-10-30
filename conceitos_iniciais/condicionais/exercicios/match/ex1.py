opcao = int(input("Escolha uma opção do cardápio!\n 1 - Pizza \n 2 - Sushi \n 3 - Salada\n "))

match opcao:
    case 1:
        print ("Já já trago sua pizza chefe!")
    case 2:
        print ("Já já trago teu sushi oriental")
    case 3:
        print ("Já já trago tua salada caba mole")
    case _:
        print ("Opção inválida")