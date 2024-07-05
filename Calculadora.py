import os
import time



x = 1


def apagar_tela():
  os.system('cls')
  
def congelar_tela():
	time.sleep(5)
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


def somar(a, b):
  apagar_tela()
  print("Essa é a sua soma: ", a+b)
  congelar_tela()
  Calculadora()

def subtrair(a, b):
  apagar_tela()
  print("Essa é a sua subtração: ", a-b)
  congelar_tela()
  Calculadora()

def multiplicar(a, b):
  apagar_tela()
  print("Essa é a sua multiplicação: ", a*b)
  congelar_tela()
  Calculadora()

def dividir(a, b):
  apagar_tela()
  print("Essa é a sua divisão: ", a/b)
  congelar_tela()
  Calculadora()

def pergunta_numeros():
	a = float(input("Me diga um numero: "))
	b = float(input("Me diga outro numero: "))



def Calculadora():
	os.system('title My calculator')
	tela_init()

	resposta = int(input("Resposta:"))

	if resposta == 0:
		return
	elif resposta == 1:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		somar(a, b)
	elif resposta == 2:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		subtrair(a, b)
	elif resposta == 3:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		multiplicar(a, b)
	elif resposta == 4:
		Calculadora()
    
Calculadora()
