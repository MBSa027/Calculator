import os
import time

x = 1
historico_operações_resultado = []
historico_operações_a = []
historico_operações_b = []
resultado = 0
a = 0
b = 0


def apagar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
  
def congelar_tela():
	time.sleep(5)
	os.system('timeout /t 60')

def registrar():
	historico_operações_resultado.append(resultado)
	historico_operações_a.append(a)
	historico_operações_b.append(b)
	
def ver_historico():
	print("seu historico é")
	print(historico_operações_a, historico_operações_b, " = ", historico_operações_resultado)


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
  resultado = a+b
  registrar()
  print("------------------------------------------------")
  print("          Essa é a sua soma: ", " | ", a+b, " |")
  print("------------------------------------------------")
  congelar_tela()
  Calculadora()

def subtrair(a, b):
  apagar_tela()
  resultado = a-b
  registrar()
  print("------------------------------------------------")
  print("      Essa é a sua subtração: ", " | ", a-b, " |")
  print("------------------------------------------------")
  congelar_tela()
  Calculadora()

def multiplicar(a, b):
  apagar_tela()
  resultado = a*b
  registrar()
  print("------------------------------------------------")
  print("  Essa é a sua multiplicação: ", " | ", a*b, " |")
  print("------------------------------------------------")
  congelar_tela()
  Calculadora()

def dividir(a, b):
  apagar_tela()
  resultado = a/b
  registrar()
  print("------------------------------------------------")
  print("        Essa é a sua divisão: ", " | ", a/b, " |")
  print("------------------------------------------------")
  congelar_tela()
  Calculadora()

def pergunta_numeros():
	apagar_tela()
	a = float(input("Me diga um numero: "))
	b = float(input("Me diga outro numero: "))



def Calculadora():
	os.system('Title My calculator')
	apagar_tela()
	tela_init()
	

	resposta = int(input("Resposta:"))
	apagar_tela()
	Entrada_de_usuario.validacao_da_entrada(resposta)

	if resposta == 0:
		return
	elif resposta == 1:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		somar(a, b)
		registrar()
	elif resposta == 2:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		subtrair(a, b)
	elif resposta == 3:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		multiplicar(a, b)
	elif resposta == 4:
		a = float(input("Me diga um numero: "))
		b = float(input("Me diga outro numero: "))
		dividir(a, b)
		Calculadora()
	elif resposta == 5:
		ver_historico()	
	
    
class Entrada_de_usuario():
	
	def validacao_da_entrada(resposta):
		possibilidades_de_resposta = (0,1,2,3,4,5)
		if resposta not in possibilidades_de_resposta:
			apagar_tela()
			print("Erro, voce inseriu um valor errado")
			congelar_tela()
			Calculadora()


    
Calculadora()
