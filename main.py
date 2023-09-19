# Python | Calculadora

import sys

# 1. Apresentação inicial da funcionalidade do script.
print("==================CALCULADORA PYTHON========================")
nome = input("Qual seu nome? ")

print("Seja bem vindo Sr. {}.\n".format(nome))
print("Pronto, pode brincar a vontade com o programa.")

# 2. O usuário vai informar o número para que seja realizado o cálculo.

print('''
      DICAS:
      Para realizar o cálculo você terá que primeiramente informar o operador, e após os dois números.
      Os operadores pode redigir os símbolos(+, -, *, /)
      ''')

# Funções:

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

# print("Maravilha, você quer {}".format)
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
operador = input("Quer usar qual operador? ")

def resultado(operador,num1,num2):
    if operador == "+": 
        return somar(num1,num2)
    elif operador == "-":
        return subtrair(num1,num2)
    elif operador == "*":
        return multiplicar(num1,num2)
    elif operador == "/":
        return dividir(num1,num2)
    else: sys.exit()
    
# print("Acho que você digitou algo que não seja o símbolo fornecido acima. Tente novamente:")

# 3. Resultado.
print("O resultado da operação é {}.".format(resultado(operador, num1, num2)))