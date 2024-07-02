import os


x = 1

def apagar_tela():
  os.system('cls')
  
def congelar_tela():
	os.system('timeout /t 60')

def tela_init():
  apagar_tela()

  print("------------------------------------------------")
  print("|                Calculadora                   |")
  print("------------------------------------------------")
  print(" 1 - Para somar")
  print(" 2 - Para subtrair")
  print(" 3 - Para Multiplicar")
  print(" 4 - Para dividir")
  print("------------------------------------------------")
  print("Aperte 0 para sair")

def op1():
  apagar_tela()
  num1 = int(input("Primeiro numero:"))
  num2 = int(input("Segundo numero:"))
  print("Essa é a sua soma: ", num1+num2)
  congelar_tela()

def op2():
  apagar_tela()
  num1 = int(input("Primeiro numero:"))
  num2 = int(input("Segundo numero:"))
  print("Essa é a sua subtração: ", num1-num2)
  congelar_tela()

def op3():
  apagar_tela()
  num1 = int(input("Primeiro numero:"))
  num2 = int(input("Segundo numero:"))
  print("Essa é a sua multiplicação: ", num1*num2)
  congelar_tela()


def op4():
  apagar_tela()
  num1 = int(input("Primeiro numero:"))
  num2 = int(input("Segundo numero:"))
  print("Essa é a sua divisão: ", num1/num2)
  congelar_tela()


while x == 1:
  os.system('title My calculator')
  tela_init()

  resposta = int(input("Resposta:"))

  if resposta == 0:
    x = 0
  elif resposta == 1:
    op1()
  elif resposta == 2:
    op2()
  elif resposta == 3:
    op3()
  elif resposta == 4:
    op4()
    
