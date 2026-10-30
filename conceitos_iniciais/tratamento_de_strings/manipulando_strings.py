fruta = "Te falar q gosto de melancia"

#Contando quantas letras tem na variavel fruta
print (len(fruta))

#Contando a partir do index 2
print (fruta [2:])

#Contando quantos "A" tem
contagema = fruta.count ('a')
print (contagema)

#Encontrando letra especifica
print (fruta.find('a'))

if 'melancia' in fruta:
    print ("Tem melancia na frase")
else:
    print ("Não tem melancia na frase")

#Posso trocar a frase para maiusculo ou minusculo com upper ou lower
#Posso usar "Capitalize" para deixar a primeira letra maiusculo
#Posso usar o "Strip" para cortar espaços a toa do lado da frase

#Replace atualiza uma letra por outra
print (fruta.replace ('a', 'x'))

#posso usar .title para tornar a primeira letra de toda palavra da frase em maiusculo