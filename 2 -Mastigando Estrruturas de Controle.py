#Mostrar na tela de 1 até 3
"""x=1
while x<=3:
    print (x)
    x=x+1"""
#Mostrar na tela de 1 até um número digitado
'''n=int(input("Digite um número: "))
x=1      
while x<=n:
    print (x)
    x=x+1'''
#Mostrar na tela os números pares de 0 até um número digitado.
'''fim=int(input("Digite um número: "))
x=0
while x<=fim:
    if x%2==0:
        print(x)
    x=x+1'''
#Mostrar na tela os números pares de 0 até um número digitado.
'''n=int(input("Digite um número: "))
x=0      
while x<=n:
    print (x)
    x=x+2'''
#Mostrar na tela os números impares de 0 até um número digitado.    
'''fim=int(input("Digite um número: "))
x=0
while x<=fim:
    if x%2!=0:
        print(x)
    x=x+1'''
#Mostrar na tela os 10 primeiros múltiplos de 3.
'''x=1
while x<=10:
    print (x*3)
    x=x+1'''
#Mostrar na tela a soma de 10 números inteiros solicitados ao usuário
'''c=1
a=0
while c<=10:
    x=int(input("Digite o %i número: " %c))
    a=a+x
    c=c+1
print("A soma dos números digitados é %i." %a)'''

#Mostrar na tela a média de 10 números inteiros solicitados ao usuário
'''c=1
a=0
while c<=10:
    x=int(input("Digite um número: "))
    a=a+x
    c=c+1
print("A média dos números digitados é %i." %(a/10))'''
    
#Mostrar na tela o fatorial de 10 (!10)
'''c=1
a=1
while c<=10:
    print("%i X %i =" %(a,c)) 
    a=a*c
    c=c+1
    print(a)
print("O fatorial de 10 é igual a %i." %a)'''

#Mostrar na tela o fatorial de um numero qualquer
'''c=1
a=1
n=int(input("Digite um número: "))
while c<=n:
    print("%i X %i =" %(a,c)) 
    a=a*c
    c=c+1
    print(a)
print("O fatorial de %i é igual a %i." %(n,a))'''

#Soma de números inteiros até ser digitado "0"
'''a=0
while True:
    c=int(input("Digite um número ou 0 (zero) para sair: "))
    if c==0:
          break
    a=a+c
print("A soma dos números digitados é igual a %i" %a)'''

#TABUADA DE 1 A 10
'''tabuada = 1
while tabuada <= 10:
    c = 1
    print (" ")
    print ("#" * 20)
    print (" ")
    print("Tabuada do %5.2d" %tabuada)
    while c <= 10:
        print ("%5.2d x %5.2d = %5.2d" %(tabuada, c, tabuada * c))
        c = c + 1
    tabuada = tabuada + 1'''
    

