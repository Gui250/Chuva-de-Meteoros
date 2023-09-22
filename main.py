import math 
#Lembrete: Se possível, colocar um indicador no menu quando uma função já está disponível ou não (Talvez um "X" do lado para quando não estiver disponível ou algo do tipo). Acho que ficaria bonitinho no resultado final.

#/\ COMENTÁRIOS DE LEMBRETE TEMPORÁRIOS ACIMA /\


def coordenadas(): #FALTA MEU PROCESSO DE OTIMIZAR (INCOMPLETO)
  print("Informe as coordenadas dos dois cantos opostos da área da sua fazenda.")
  print("Canto superior esquerdo:", end=" ")
  print("Canto inferior direito:", end=" ")
  

def converter(medida, angulo):
  # aplicando formula para converter coordenadas cartesianas em polares
  r = math.sqrt((medida ** 2) + (angulo ** 2))
  print(r)
  
# Construindo um menu 
def main():
  print("\n*****************") 
  print("Chuva de Meteoros")
  print("*****************")
  
  print('''
  Sistema para analíse de Meteoros
  Menu: 
  [1] Definir perímetro da propriedade e da edificação de interesse
  [2] Unificar sistemas de coordenadas de referência
  [3] Processar registros de chuvas de meteoros
  [4] Apresentar estatísticas
  [5] Sair
  ''')
  
  opc = ''
  while opc != '5': #Enquanto o usuário já não tiver saído,
    print("Opção:", end=" ") #Pergunto a opção
    opc = input()
    
    if opc == '1':
      #coordenadas()
      print("Medida:", end=" ")
      m = float(input())
      print("Ângulo:", end=" ")
      a = float(input())
      converter(m, a)
    elif opc == '2': 
      pass
    elif opc == '3': 
      pass
    elif opc == '4':
      pass
    elif opc == '5': 
      #A partir do momento que opc agora é igual a 5,
      #O Programa irá se encerrar automaticamente,
      #"break" não é necessário.
      print("Saindo...")
    else:
      print("Opção inválida, tente novamente.")


main()
