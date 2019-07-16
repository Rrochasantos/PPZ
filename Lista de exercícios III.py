#1. Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''nota = int(input('Digite uma nota entre 0 (zero) e 10 (dez): '))
while nota not in (0,1,2,3,4,5,6,7,8,9,10):
    print('Opa, você não leu o enunciado??? É entre 0 (zero) e 10 (dez)!!!')
    print ('Tente mais uma vez crânio.')
    nota = int(input('Digite uma nota entre 0 (zero) e 10 (dez): '))
print ('A nota digitada foi %i.' %nota)'''
    


#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.
'''usuario= input('USUÁRIO: ')
senha = input('SENHA: ')

while usuario == senha:
    print('Falha no processo: Erro de segurança 42')
    print('Usuario e senha devem ser diferentes')
    usuario= input('USUÁRIO: ')
    senha = input('SENHA: ')
    
if usuario == 'span' and senha == 'swordfish':
    print ('Acesso concedido: May de force be whith you')
else:
    print ('Acesso limitado para pessoas limitadas')'''
    


#3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que
#a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
'''populaçãoA = 80000
populaçãoB = 200000
anos = 0

while populaçãoA <= populaçãoB:
    populaçãoA = populaçãoA + populaçãoA * .03
    populaçãoB = populaçãoB + populaçãoB * .015
    anos += 1
    
print ('Em %i anos a população do país A será de %i e a do país B será de %i.' %(anos, int(populaçãoA), int(populaçãoB)))'''


#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
#Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

'''numero = int(input('Digite um número: '))
n=0
n1=1
n2=0
soma=0
while n != numero:
    soma = n1 + n2
    n1 = n2
    n2 = soma
    n += 1
    print ('O Fibonacci de %i é %i.' %(numero,n2))
    ou
    n1,n2 = n2,n1+n2
    n+=1
print ('O Fibonacci de %i é %i.' %(numero,n2))'''


#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
'''numeroA = int(input('Digite o primeiro número: '))
numeroB = int(input('Digite o segundo número: '))
print('O MDC entre %i e %i é igual a: '%(numeroA, numeroB,))
while numeroA-numeroB!=0 or numeroB-numeroA!= 0:
    if numeroA > numeroB:
        diferença = numeroA-numeroB
        numeroA = numeroB
        numeroB = diferença
    elif numeroB > numeroA:
        diferença = numeroB-numeroA
        numeroB = numeroA
        numeroA = diferença
print('"""%i"""' %diferença)'''
    
              
              
