# Testando listas

'''familia = []
c = 0
while True:
    sozinho = input("Mora mais alguem com você? Sim (s) ou não (n): ")
    if sozinho != 'n':
        parente = input ("Quem mais mora com você: ")
        familia.append (parente)
        c = c + 1
    else:
        break
print (' ')
print ('=' * 20)
print ("Que legal, você mora com:")
print ('=' * 20)
print (' ')
n=0
while n < c:
    print(familia[n])
    print (' ')
    n=n+1'''

#Média de 5 notas com uso de lista

'''notas = [8.3,9.5,6.5,7,5.7]
soma  = 0
c = 0
while c < 5:
    soma += notas[c]
    print (soma)
    c += 1
print ('Média = %5.2f' %(soma/c))'''

#Crie um vetor com 10 posições e imprima o vetor na ordem inversa

'''vetor =[]
c1 = 1
while c1 <= 10:
    n = int(input("Digite um numero inteiro: "))
    vetor.append(n)
    c1 += 1
print (vetor)

c2 = 9
n = 0
while c2 >=5:
    estoque = vetor[n]
    vetor [n] = vetor [c2]
    vetor [c2] = estoque
    n += 1
    c2 -= 1
print (vetor)'''

#Faça um programa que leia quatro notas, faça a média e mostre as notras e a média

'''notas = []
c = 1
total = 0
media = 0
while c <= 4:
    n = float(input("Informe a nota: "))
    notas.append (n)
    total = total + n
    media = total / c
    c += 1
print ("Suas notas foram: ", notas)
print ("Sua média é: %5.2f" %media)'''


#Faça um vetor que leia 10 letras minuscula e conte quantas consoantes foram contadas.

'''vetor =[]
c = 1
consoantes = 0
while c <= 10:
    n = input("Digite uma letra: ")
    vetor.append(n)
    c += 1
    if n not in 'aeiou':
        consoantes = consoantes + 1
print (vetor)
print ("Número de consoantes do vetor: %d" %consoantes)'''

#Verifique se uma palavra é palindrome
'''while True:
    palavra = input('Digite uma palavra: ')
    if palavra != "":
        if palavra == palavra[::-1]:
            print ('---------------') 
            print(palavra.upper(),'é palíndrome.')
            print ('---------------') 
        else:
            print ('---------------') 
            print(palavra.upper(),'não é palíndrome')
            print ('---------------') 
    else:
        break'''

# Faça um programa que leia uma palavra e troque as vogais por "*"
'''while True:
    palavra = input('Digite uma palavra: ')
    palavra2 = ''
    if palavra != '':
        for l in palavra:
            if l in 'aeiou':
                palavra2 = palavra2 + '*'
            else:
                palavra2 = palavra2 + l
        print ('---------------')            
        print (palavra)
        print ('---------------')
        print (palavra2)
        print ('---------------')
    else:
        break'''

#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e
#imprima  com o nome do mês por extenso
'''while True:
    meses = ['janeiro', 'fevereiro', 'março',
           'abril', 'maio', 'junho',
           'julho', 'agosto', 'setembro',
           'outubro', 'novembro', 'dezembro']
    dia, mes, ano = input('Qual sua data de nascimento (dd/mm/aaaa): ').split('/')
    print('Você nasceu em %s de %s de %s' %(dia, meses [int(mes)-1], ano))
    sair = input('Deseja sair do programa (s/n)? ')
    if sair == 's':
        break'''


        
