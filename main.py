import math
import os
from time import sleep

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

def converterParaCoord(dist, ang): #FALTA MEU PROCESSO DE OTIMIZAR (INCOMPLETO)
  print("AAAAAAAAAAAAAAAAAAAAAAAA")
  print("COSSENO DE", ang, ":", math.cos(ang))
  print("SENO DE", ang, ":", math.sin(ang))
  x = dist * math.cos(ang)
  y = dist * math.sin(ang)
  print("\n(x, y):", x, y)
  print("Ok então essas são as refs sem considerar pos da sede")

  #x e y são o TAMANHO do "quadrado" para marcar as coordenadas, mas não são as COORDENADAS em si
  #então agora eu SOMO X e Y nas coordenadas da sede???? (isso!)
  #então se a coordenada da sede for negativa, seja no seu ySed ou xSed por exemplo, a soma do negativo já vai se tornar subtração, então automaticamente dá tudo certinho
  #dessa maneira:

  print("\nCoordenadas da sede:", -2, 2)
  print("\"Distância\" x da sede:", x)
  print("\"Distância\" y da sede:", y)

  x = x + -2 #se xSed for negativo, vai subtrair
  y = y + 2 #se xSed for negativo, vai subtrair
  
  print("\nPor favor esteja certo")
  print("x real como uma coordenada:", x)
  print("y real como uma coordenada:", y)
  

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

      print("\nTESTANDO CONVERSAO DE COORDENADAS")
      converterParaCoord(8, 45)
      
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


