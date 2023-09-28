from math import cos
from math import sin
from math import radians

'''
Bruna Gonçalves Corte David
TIA: 42307831

Guilherme Soares Moreno
TIA: 42333288

Gabriel
TIA:
'''

xFazSup, yFazSup = 0, 0 #Coordenadas do canto superior esquerdo da fazenda
xFazInf, yFazInf = 0, 0 #Coordenadas do canto inferior direito da fazenda
xSedSup, ySedSup = 0, 0 #Coordenadas do canto superior esquerdo da sede
xSedInf, ySedInf = 0, 0 #Coordenadas do canto inferior direito da sede
xUpm, yUpm = 0, 0 #Coordenadas da UPMCC

xMet, yMet = 0, 0 #variáveis para guardar e calcular coordenadas dos meteoros
quedasTotal = 0 #Total de quedas registradas
quedasFaz = 0 #Total de quedas dentro da propriedade
qNE = 0 #Total de quedas no quadrante NE
qNO = 0 #Total de quedas no quadrante NO
qSO = 0 #Total de quedas no quadrante SO
qSE = 0 #Total de quedas no quadrante SE
sedeAtingida = False #Variável booleana para saber se sede foi atingida

#Porcentagens calculadas dos registros
porcFaz = 0.0 #Porcentagem de quedas na fazenda em relação ao total de quedas
porcNE = 0.0 #Porcentagem de quedas nos quadrantes em relação ao total de quedas
porcNO = 0.0
porcSO = 0.0
porcSE = 0.0

perimetroDefinido = False #Bool para habilitação de próximas funções 
sistemaUnificado = False #Bool para habilitação de próximas funções
processado = False #Bool para habilitação de próximas funções

# Construindo um menu
while True:
  print("\n*****************") 
  print("Chuva de Meteoros")
  print("*****************")
  
  print('''
  Sistema para analíse de Meteoros
  Menu: 
  [1] Definir perímetro da propriedade e da edificação de interesse
  [2] Unificar sistemas de coordenadas de referência
  [3] Processar registros de chuva de meteoros
  [4] Apresentar estatísticas
  [5] Apresentar configuração atual de coordenadas
  [6] Sair
  ''')

  opc = ''
  print("Opção:", end=" ") #Pergunto a opção
  opc = input()
  
  if opc == '1':
    print("\nInforme as coordenadas dos dois cantos opostos do perímetro da sua fazenda.")

    print("\nCanto superior esquerdo:")
    print("Coordenada x:", end=" ")
    xFazSup = float(input())
    print("Coordenada y:", end=" ")
    yFazSup = float(input())
    print("\nCanto inferior direito:")
    print("Coordenada x:", end=" ")
    xFazInf = float(input())
    print("Coordenada y:", end=" ")
    yFazInf = float(input())

    print("\nInforme as coordenadas dos dois cantos opostos do perímetro da  edificação de interesse.")

    print("\nCanto superior esquerdo:")
    print("Coordenada x:", end=" ")
    xSedSup = float(input())
    print("Coordenada y:", end=" ")
    ySedSup = float(input())
    print("\nCanto inferior direito:")
    print("Coordenada x:", end=" ")
    xSedInf = float(input())
    print("Coordenada y:", end=" ")
    ySedInf = float(input())

    perimetroDefinido = True

  elif opc == '2':
    print("\nInforme as coordenadas da localização da sede UPMCC")

    print("\nLocalização:")
    print("Coordenada x:", end=" ")
    xUpm = float(input())
    print("Coordenada y:", end=" ")
    yUpm = float(input())

    sistemaUnificado = True
    
  elif opc == '3':
    #Primeiramente, verificando se a função já pode ser chamada.
    if perimetroDefinido == False:
      print("\nImpossível processar qualquer registro de queda no momento:")
      print("localização da propriedade ainda não informada.")

    elif sistemaUnificado == False:
      print("\nImpossível processar qualquer registro de queda no momento:")
      print("não foi feita a unificação dos sistemas referenciais usados nos cálculos.")
      
    else: #Se ela pode ser chamada, começo ela abaixo
      print("\nInforme os registros de chuva de meteoros")
      print("Digite -1 para finalizar os registros.")

      #Reiniciando registros
      quedasTotal = 0 #Total de quedas registradas
      quedasFaz = 0 #Total de quedas dentro da propriedade
      qNE = 0 #Total de quedas no quadrante NE
      qNO = 0 #Total de quedas no quadrante NO
      qSO = 0 #Total de quedas no quadrante SO
      qSE = 0 #Total de quedas no quadrante SE
      sedeAtingida = False
      
      #Calculando posição do ponto divisor dos 4 quadrantes
      xMeio = xFazSup+((xFazInf - xFazSup)/2)
      yMeio = yFazInf+((yFazSup - yFazInf)/2)
    
      dist = 0
      ang = 0
      cont = 0
      while True:
        cont+=1
        print("Registro #"+str(cont))
        print("-> Distância:", end=" ")
        dist = float(input())
        if dist == -1:
          break
        print("-> Ângulo:", end=" ")
        ang = float(input())
        if ang == -1:
          break

        #Cálculos a seguir
        #Convertendo coordenadas polares do meteoro para coordenadas cartesianas
        xMet = round((dist * cos(radians(ang))) + xUpm)
        yMet = round((dist * sin(radians(ang))) + yUpm)

        #Verificando se este meteoro atingiu dentro do perímetro da fazenda
        if (xMet>=xFazSup) and (yMet<=yFazSup) and (xMet<=xFazInf) and (yMet>=yFazInf):
          quedasFaz += 1
          
          #Se ele caiu dentro do perímetro da fazenda, posso descobrir em qual quadrante está
          #Verificando em qual quadrante este meteoro atingiu
          if (xMet>=xMeio) and (yMet>=yMeio):
            qNE += 1
          elif (xMet<=xMeio) and (yMet>=yMeio):
            qNO += 1
          elif (xMet<=xMeio) and (yMet<=yMeio):
            qSO += 1
          elif (xMet>=xMeio) and (yMet<=yMeio):
            qSE += 1

        #Verificando se este meteoro atingiu dentro do perímetro da sede
        if (xMet>=xSedSup) and (yMet<=ySedSup) and (xMet<=xSedInf) and (yMet>=ySedInf):
          sedeAtingida = True

      quedasTotal = cont-1 #Menos 1 porque não deve contabilizar o momento da saída dos registros
      print("Fim da coleta de registros:", quedasTotal, "queda(s) informada(s).")
      processado = True #Será possível acessar as estastísticas agora
      
  elif opc == '4':
    #Primeiramente, verificando se a função já pode ser chamada.
    if processado == False:
      print("\nImpossível apresentar quaisquer estatísticas no momento:")
      print("Nenhuma queda de meteoros foi registrada.")
    else: #Se ela pode ser chamada, começo ela abaixo
      
      #Calculando porcentagens
      if quedasTotal>0:
        porcFaz = (quedasFaz*100)/quedasTotal
      if quedasFaz>0:
        porcNE = (qNE*100)/quedasFaz
        porcNO = (qNO*100)/quedasFaz
        porcSO = (qSO*100)/quedasFaz
        porcSE = (qSE*100)/quedasFaz
      
      print("\nTotal de quedas registradas:", quedasTotal, "(100%)")
      print("Quedas dentro da propriedade:", quedasFaz, "({:.2f})%".format(porcFaz)) #AJEITAR
      print("-> Quadrante NE:", qNE, "({:.2f})%".format(porcNE)) #AJEITAR
      print("-> Quadrante NO:", qNO, "({:.2f})%".format(porcNO)) #AJEITAR
      print("-> Quadrante SO:", qSO, "({:.2f})%".format(porcSO)) #AJEITAR
      print("-> Quadrante SE:", qSE, "({:.2f})%".format(porcSE)) #AJEITAR
      
      if sedeAtingida == True:
        print("A edificação principal foi atingida? SIM")
      else:
        print("A edificação principal foi atingida? NÃO")

      print("\nAperte enter para continuar...")
      input()

  elif opc == '5': #Mostrar coordenadas configuradas atuais pro usuário
    print("\nCoordenadas do perímetro da propriedade:")
    print("x superior:", xFazSup, "y superior:", yFazSup)
    print("x inferior:", xFazInf, "y inferior:", yFazInf)
    print("\nCoordenadas do perímetro da edificação de interesse:")
    print("x superior:", xSedSup, "y superior:", ySedSup)
    print("x inferior:", xSedInf, "y inferior:", ySedInf)
    print("\nCoordenadas da localização do sistema de referência:")
    print("x:", xUpm, "y:", yUpm)

  elif opc == '6': 
    print("Saindo...")
    break

  else:
    print("\nA opção escolhida é inválida, tente novamente.")
