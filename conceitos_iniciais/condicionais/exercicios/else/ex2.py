valor_compra = float(input("Qual o valor de compra?"))
cadastro = input("Tem cadastro? (s/n)")

if valor_compra >= 100:
    print ("Você passou do valor mínimo para o frete grátis!")
    if cadastro == "s":
        print ("e é cadastrado! Parabéns, ganhou!!!")
    else:
        print ("mas não é cadastrado, droga...")
else:
    print ("O valor mínimo não deu...")