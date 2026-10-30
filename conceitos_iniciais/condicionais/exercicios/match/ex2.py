meiotransporte = input("Digite um meio de transporte! (Só com Minúscula)")

match meiotransporte:
    case "carro":
        print ("Veículo terrestre")
    case "barco":
        print ("Veículo Aquático")
    case "avião":
        print ("Veículo aéreo")
    case _:
        print ("Veículo desconhecido")