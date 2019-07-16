#1. Faça um Programa que peça os três lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
3

'''lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))

while lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3> lado1 + lado2:
    print ("Isso não é um triângulo amigão, tente outra vez!!!")
    lado1 = int(input("Digite o primeiro lado do triângulo: "))
    lado2 = int(input("Digite o segundo lado do triângulo: "))
    lado3 = int(input("Digite o terceiro lado do triângulo: "))
if lado1 == lado2 == lado3:
    print ("Trata-se de um triângulo Equilátero com os seguintes lados: %d , %d e %d" %(lado1, lado2, lado3))
elif lado1 == lado2 or lado1==lado3:
    print ("Trata-se de um triângulo Isóceles com os seguintes lados: %d , %d e %d" %(lado1, lado2, lado3))
else:
    print ("Trata-se de um triângulo Escalerno com os seguintes lados: %d , %d e %d" %(lado1, lado2, lado3))'''




#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

'''ano=0
while True:
    ano = int(input("Digite o ano: "))
    if ano%4 == 0 and (ano%100!=0 or ano%400==0):
        print(" O ano %d É bisexto" %ano)
    else:
        print(" O ano %d NÂO É bisexto" %ano)
    continuar = input("Deseja verificar outro ano sim (s) ou não (n)? ")
    if continuar == "n":
        break'''



#3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
#Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
#Caso contrário mostrar tais variáveis com o conteúdo ZERO.

'''peso = float(input( "Quantos quilos de peixe você pescou hoje? "))
excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print ("Você excedeu a cota em %d quilos." %excesso)
    print ("Conforme a lei vigente deverá pagar uma multa de R$ %5.2f." %multa)
else:
    print ("Excedente = ZERO.")
    print ("Multa = ZERO")'''




#4. Faça um Programa que leia três números e mostre o maior deles.

'''if n1==n2==n3:
    print ("Todos os números são iguais, não há memhum maior que os outros")
elif n1 >= n2 and n1 >= n3:
    print ("O primeiro número (%d) é o maior" %n1)
elif n2 >= n3:
    print ("O segundo número (%d) é o maior" %n2)
else:
    print ("O terceiro número (%d) é o maior" %n3)'''





#5. Faça um Programa que leia três números e mostre o maior e o menor deles.

'''n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))

if n1==n2==n3:
    print ("Todos os números são iguais, não há memhum maior que os outros")
elif n1 >= n2 and n1 >= n3:
    print ("O primeiro número (%d) é o maior" %n1)
elif n2 >= n3:
    print ("O segundo número (%d) é o maior" %n2)
else:
    print ("O terceiro número (%d) é o maior" %n3)
    
if n1==n2==n3:
    print ("Todos os números são iguais, não há memhum menor que os outros")    
elif n1 <= n2 and n1 <= n3:
    print ("O primeiro número (%d) é o menor" %n1)
elif n2 <= n3:
    print ("O segundo número (%d) é o menor" %n2)
else:
    print ("O terceiro número (%d) é o menor" %n3)'''





#6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
#Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

'''valorHora = float(input("Qual o valor da sua hora trabalhada? R$ "))
horaMes = float(input("Quantas horas trabalhadas no mês? "))
sBruto = valorHora * horaMes
ir= sBruto * 0.11
inss = sBruto * 0.08
sindicato = sBruto * 0.05
sLiquido = sBruto - ir - inss - sindicato
print ("+ Salário Bruto..: R$ %10.2f" %sBruto)
print ("- IR.............: R$ %10.2f" %ir)
print ("- INSS...........: R$ %10.2f" %inss)
print ("- Sindicato......: R$ %10.2f" %sindicato)
print ("= Salário Liquido: R$ %10.2f" %sLiquido)'''




#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.'''

'''print ("Bem vindo ao programa para auxílio na compra de suas tintas!")
metragem = float(input("Qual a quantidade de m² receberá a pintura? "))
litros = metragem / 3                 
if litros % 18 == 0:
    latas = litros / 18
else:
    latas = litros // 18 + 1
valor = latas * 80
print ("Para pintar %.2f m² serão necessários %.2f L de tinta" %(metragem, litros))
print ("Como nossas latas são de 18 L, será necessário adquirir %d latas" %latas)
print ("O valor a ser pago por %d latas de tinta é R$ %6.2f" %(latas, valor))'''












                


