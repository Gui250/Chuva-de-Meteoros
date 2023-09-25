import math
import os
from time import sleep
#Lembrete: Se possível, colocar um indicador no menu quando uma função já está disponível ou não (Talvez um "X" do lado para quando não estiver disponível ou algo do tipo). Acho que ficaria bonitinho no resultado final.


#/\ COMENTÁRIOS DE LEMBRETE TEMPORÁRIOS ACIMA /\

#Variáveis globais, temporariamente?
xSup, ySup = 0, 0 #Coordenadas do canto superior esquerdo da fazenda
xInf, yInf = 0, 0 #Coordenadas do canto inferior direito da fazenda
xSed, ySed = 0, 0 #Coordenadas da sede UPMCC

def mostrarMenu():
  print("\n*****************") 
  print("Chuva de Meteoros")
  print("*****************")
  
  print('''
  Sistema para analíse de Meteoros
  Menu: 
  [1] Definir a localização da fazenda e da sede
  [2] Processar registros de chuvas de meteoros
  [3] Apresentar estatísticas
  [4] Sair
  ''') #Função para printar menu

def converterParaCoord(): #FALTA MEU PROCESSO DE OTIMIZAR (INCOMPLETO)
  pass
  
  
''' SALVANDO CÓDIGO
def converter(medida, angulo):
  # aplicando formula para converter coordenadas cartesianas em polares
  r = math.sqrt((medida ** 2) + (angulo ** 2))
  print(r)
'''

# Construindo um menu 
def main():
  mostrarMenu()
  
  opc = ''
  while opc != '4': #Enquanto o usuário já não tiver saído,
    print("Opção:", end=" ") #Pergunto a opção
    opc = input()
    
    if opc == '1':
      sleep(0.2)
      os.system('clear')
      print("Informe as coordenadas dos dois cantos opostos da área da sua fazenda.")
      while True: #Validando entrada do usuário
        try:
          print("\nDigite no seguinte formato: x, y")
          print("Canto superior esquerdo:", end=" ")
          xSup, ySup = map(float, input().split(", "))
          print("Canto inferior direito:", end=" ")
          xInf, yInf = map(float, input().split(", "))
          break
        except:
          print("Formato inválido, tente novamente.")

      print("\nInforme as coordenadas da localização da sede UPMCC.")
      while True:
        try:
          print("\nDigite no seguinte formato: x, y")
          print("Localização:", end=" ")
          xSed, ySed = map(float, input().split(", "))
          break
        except:
          print("Formato inválido, tente novamente.")

      print("\nVoltando ao menu...")
      sleep(1.5)
      os.system('clear')
      mostrarMenu()
      
    elif opc == '2':
      sleep(0.2)
      os.system('clear')
      print("Informe os registros de chuva de meteoros")
      
    elif opc == '3':
      sleep(0.2)
      os.system('clear')
      print("Apresente estatiscas: ") 
    elif opc == '4': 
      #A partir do momento que opc agora é igual a 4,
      #O Programa irá se encerrar automaticamente,
      #"break" não é necessário.
      print("Saindo...")
    else:
      print("Opção inválida, tente novamente.")


main()


  
  
