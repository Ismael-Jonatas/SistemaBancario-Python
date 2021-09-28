# Importando as funcoes
import func1
from datetime import date
from copy import deepcopy

# Listas
contas = []
movimentacao = []

# Cabecalhos dos arquivos 
cabecalho_csv_contas = ["numerConta","digito","descricao_da_conta","tipo","totcred","totdeb","saldo"]

cabecalho_csv_movimentacao = ["id","data","conta_deb","dig_deb","conta_cred","dig_cred","complemento","valor"]

# Acumulador
registro = 0

# Main
while True:

#  ==========  Print do menu  ==========

# chamando a funcao menu
  func1.menu()

  opcao = input("\nInsira a opcao desejada do menu acima: ").upper()

  while opcao not in ['C','D','A','P','I','X','B','S']:
    opcao = input("\nInsira corretamente a opcao desejada do menu acima: ").upper()

# ==========  Menu opcao "(c)"  ==========

  if opcao == 'C':
    while True: 
      tipo_conta_a_s = input("\nQual tipo de conta deseja, (A)analitica ou (S)sintetica: ").upper()

# Tratamentos de erros, variavel tipo_conta_a_s
      while tipo_conta_a_s not in ['A','S']:
        tipo_conta_a_s = input("\nInsira a opcao correta: ").upper()
      print("\n===  OBS: (de 0 a 9, com 11 caracteres, apenas numeros)  === ")

# Numero da conta nova
      numero_conta = input("\nNumero de conta: ")
      if len(numero_conta) != 1 and func1.buscaConta(func1.getSuperior(numero_conta), contas) == None:
        print("Essa conta nao tem superior!")
        break
      numero_conta = func1.complementadigitos(numero_conta)

# Tratamentos de erros, variavel numero_conta
      while True:
          contas_2 = []
          for i in range(len(contas)):
            contas_2.append(contas[i][1])

          if (numero_conta in contas_2):
            print("\n===  Erro!, Numrero de conta existente ===")
            numero_conta = input("\nInsira um numero de conta novo: ")
            numero_conta = func1.complementadigitos(numero_conta)

          elif not numero_conta.isnumeric():             
            print("\n===  Erro!, Numrero de conta Nao e Numerico ===")
            numero_conta = input("\nInsira um numero de conta novo: ")
            numero_conta = func1.complementadigitos(numero_conta)
          else: 
            break

# Descricao de conta 
      descricao_conta = input("Insira a descricao da conta: ")

# Tratamentos de erros, variavel descricao_conta
      while True:
        if descricao_conta == '':
          print("\nErro!, Campo obrigatorio.")
          descricao_conta = input("Insira a descricao da conta: ")

        elif descricao_conta.isnumeric():
          print("\nErro!, nao pode apenas so conter numeros nesse campo!")
          descricao_conta = input("Insira a descricao da conta: ")
        else:
           break
# DV da nova conta
      print('Digito verificador: ',func1.checkconta(numero_conta))

# Saldos, creditos e debitos
      saldo = 0
      credito = 0
      debito = 0

# Deseja cadastar
      deseja_cadastrar = input("Deseja cadastrar e salvar sua conta? (1)sim ou (2)nao: ")

# Tratamentos de erros, variavel deseja_cadastrar
      while deseja_cadastrar not in['1','2']:
        deseja_cadastrar = input("\nInsira a opcao correta: ")

      if deseja_cadastrar == '1':
# Matriz contas
        contas.append([tipo_conta_a_s,numero_conta,func1.checkconta(numero_conta),descricao_conta,credito,debito,saldo]) 
        print('\nTotais de Credito: 00.00\nTotais de Debito: 00.00\nTotais de Saldo: 00.00')

      elif deseja_cadastrar == '2':
        break

# Espia matriz contas !!!!!!!!!!!!!!!!
      print('\n',contas)

#  Deseja continuar
      continuar_cadastrar = input("\nDeseja cadastrar outra conta? (1)sim ou (2)nao: ")

# Tratamentos de erros, variavel continuar_cadastrar
      while continuar_cadastrar not in['1','2']:
        continuar_cadastrar = input("\nInsira a opcao correta: ")

      if continuar_cadastrar == '1':
        continue

      elif continuar_cadastrar == '2':
        break

#  ==========  Menu opao "(D)"  ==========

  elif opcao == 'D':   
    while True:
      
      print("\n===  OBS: dia da movimentacao deve conter dois digitos ex: 01 ... 31.  ===")

#  Dia 
      dia = input("\nInsira o dia da movimentacao: ")

# Tratamentos de erros, variavel dia
      while True:
        if len(dia) != 2:
          dia = input("Insira o dia corretamente: ")

        elif not dia.isnumeric():
          dia = input("Insira o dia corretamente: ")  
        else:
          break
# Tipo  de c
      tipo_c = input("Insira o tipo da movimentacao, (D)debitar, (C)creditar ou (A)ambas: ").upper()

# Tratamentos de erros, variavel tipo_conta_d_c_a
      while tipo_c not in ['D','C','A']:
        tipo_c = input("\nInsira a opcao correta: ").upper()

# Tipo de c
      if tipo_c == "C":
        conta_d_c = input("\nInsira o numero da conta credito:  ")
        conta_d_c = func1.complementadigitos(conta_d_c)

# tratamentos de erros, variavel conta_d_c
        while True:           
          if not conta_d_c.isnumeric():             
            print("\n===  Erro!, Numrero de conta Nao e Numerico ===")
            conta_d_c = input("\nInsira o numero da conta corretamente: ")
            conta_d_c = func1.complementadigitos(conta_d_c)          
          else: 
            break
 
 # DV da conta credito
        digito_verificador = input("Insira o DV da conta correspondente: ")

# Tratamentos de erros, variavel digito_verificador
        while True:
          if not digito_verificador.isnumeric():
            print("===  Erro!  ===")
            digito_verificador = input("Insira o DV da conta correspondente: ")
          else:
            break
# conta debito e seu DV
        conta_d_c_2 = ' '
        digito_verificador_2 = ' '

# Descricao da movimentacao
        descricao = input("Insira a descricao da movimentacao: ")

# Tratamentos de erros, variavel descricao
        while True:
          if descricao == '':
            print("\nErro!, Campo obrigatorio.")
            descricao = input("Insira a descricao da movimentacao: ")
          elif descricao.isnumeric():
            print("\nErro!, Nao pode conter so numeros nesse campo.")
            descricao = input("Insira a descricao da movimentacao: ") 
          else:
            break

# Valor creditado
        valor = input("Valor Credito: ")

# Deseja movimentar
        deseja_movimentar = input("Comfirma a movimentacao? (1)sim ou (2)nao: ")

# Tratamentos de erros, variavel deseja_movimentar
        while deseja_movimentar not in['1','2']:
          deseja_movimentar = input("\nInsira a opcao correta: ")

        if deseja_movimentar == '1':
          registro += 1 
# Matriz movimentacao
          movimentacao.append([registro,dia,tipo_c,conta_d_c,digito_verificador,conta_d_c_2,digito_verificador_2,descricao,valor])
          print("\nConcluido!.")

# Espia matriz c !!!!!!!!!!         
          print('\n',movimentacao)

        elif deseja_movimentar == '2':
          break

# Tipo de  movimentacao
      elif tipo_c == "D":
        conta_d_c = input("\nInsira o numero da conta debito:  ")
        conta_d_c = func1.complementadigitos(conta_d_c)

# Tratamentos de erros, variavel conta_d_c
        while True:         
          if not conta_d_c.isnumeric():             
            print("\n===  Erro!, Numrero de conta Nao e Numerico ===")
            conta_d_c = input("\nInsira o numero da conta corretamente: ")      
            conta_d_c = func1.complementadigitos(conta_d_c)      
          else: 
            break

#  DV da conta debito
        digito_verificador = input("Insira o DV da conta correspondente: ")

# Tratamentos de erros, variavel digito_verificador
        while True:
          if not digito_verificador.isnumeric():
            print("===  Erro!  ===")
            digito_verificador = input("Insira o DV da conta correspondente: ")
          else:
            break
# Conta credito e seu DV
        conta_d_c_2 = ' '
        digito_verificador_2 = ' '

# Descricao da conta debito
        descricao = input("Insira a descricao da movimentacao: ")

# Tratamentos de erros, variavel descricao
        while True:
          if descricao == '':
            print("\nErro!, Campo obrigatorio.")
            descricao = input("Insira a descricao da movimentacao: ")
          elif descricao.isnumeric():
            print("\nErro!, Nao pode conter so numeros nesse campo.")
            descricao = input("Insira a descricao da movimentacao: ")  
          else:
            break

# Valor debitado
        valor = input("Valor debito: ")

# Deseja movimentar
        deseja_movimentar = input("Comfirma a movimentacao? (1)sim ou (2)nao: ")

# Tratamentos de erros, variavel deseja_movimentar
        while deseja_movimentar not in['1','2']:
          deseja_movimentar = input("\nInsira a opcao correta: ")

        if deseja_movimentar == '1':
          registro += 1 
# Matriz c
          movimentacao.append([registro,dia,tipo_c,conta_d_c,digito_verificador,conta_d_c_2,digito_verificador_2,descricao,valor])
          print("\nConcluido!.")
          
# Espia matriz c !!!!!!!!!!         
          print('\n',movimentacao)

        elif deseja_movimentar == '2':
          break

# Tipo de movimentacao
      elif tipo_c == "A":

# Conta debito
        conta_d_c = input("\nInsira o numero da conta debito: ")
        conta_d_c = func1.complementadigitos(conta_d_c)

# Tratamentos de erros, variavel derivada_d_3
        while True:         
          if not conta_d_c.isnumeric():             
            print("\n===  Erro!, Numrero de conta Nao e Numerico ===")
            conta_d_c = input("\nInsira o numero da conta corretamente: ")
            conta_d_c = func1.complementadigitos(conta_d_c)
          else: 
            break

# DV da conta debito
        digito_verificador = input("Insira o DV da conta debito: ")

# Tratamentos de erros, variavel digito_verificador
        while True:
          if not digito_verificador.isnumeric():
            print("===  Erro! ===")
            digito_verificador = input("Insira o DV da conta correspondente: ")
          else:
            break

# Conta credito
        conta_d_c_2 = input("Insira o numero da conta credito: ")
        conta_d_c_2 = func1.complementadigitos(conta_d_c_2)

# Tratamentos de erros, variavel conta_d_c_2
        while True:
          if not conta_d_c_2.isnumeric():             
            print("\n===  Erro!, Numrero de conta Nao e Numerico ===")
            conta_d_c_2 = input("\nInsira o numero de conta corretamente: ")
            conta_d_c_2 = func1.complementadigitos(conta_d_c_2)
          else: 
            break

# DV da conta credito
        digito_verificador_2 = input("Insira o DV da conta credito: ")

# Tratamentos de erros, variavel digito_verificador_2
        while True:
          if not digito_verificador_2.isnumeric():
            print("===  Erro!  ===")
            digito_verificador_2 = input("Insira o DV da conta correspondente: ")
          else:
            break

# Descricao da movimentacao
        descricao = input("Insira a descricao da movimentacao: ")

# Tratamentos de erros, variavel descricao
        while True:
          if descricao == '':
            print("\nErro!, Campo obrigatorio.")
            descricao = input("Insira a descricao da movimentacao: ")
          elif descricao.isnumeric():
            print("\nErro!, Nao pode conter so numeros nesse campo.")
            descricao = input("Insira a descricao da movimentacao: ")
          else:
            break

# Valor creditado
        valor = input("Valor: ")
  
# Deseja movimentar
        deseja_movimentar = input("Comfirma a movimentacao? (1)sim ou (2)nao: ")

# Tratamentos de erros, variavel deseja_movimentar
        while deseja_movimentar not in['1','2']:
          deseja_movimentar = input("\nInsira a opcao correta: ")

        if deseja_movimentar == '1':
          registro += 1 
# Matriz c
          movimentacao.append([registro,dia,tipo_c,conta_d_c,digito_verificador,conta_d_c_2,digito_verificador_2,descricao,valor])
          print("\nConcluido!.")
          
# Espia matriz c !!!!!!!!!!         
          print('\n',movimentacao)

        elif deseja_movimentar == '2':
          break   

# Deseja continuar
      continuar_movimentar = input('\nDeseja fazer outra movimentacao?, (1)sim ou (2)nao: ') 

# Tratamentos  de erros, variavel continuar_movimentar
      while continuar_movimentar not in['1','2']:
        continuar_movimentar = input("\nInsira a opcao correta: ")

      if continuar_movimentar == '1':
        continue

      elif continuar_movimentar == '2':
        break

#  ==========  Menu opcao "(A)"  ==========

  elif opcao == 'A':

# chamando a funcao critica
    erros = func1.critica(contas, movimentacao)

# Deseja corrigir
    if len(erros) != 0:
      deseja_corrigir = input("\nDeseja corrigir?: (1)sim ou (2)nao: ")

# Tratamento de eros da variavel deseja_corrigir
      while deseja_corrigir not in ['1','2']:
        print('Insira a opcao correta!')
        deseja_corrigir = input("\nDeseja corrigir?: (1)sim ou (2)nao: ")

# Edicao dos erros na movimentacao
      if deseja_corrigir == '1':
        for s in range(len(erros)):
          print(movimentacao[int(erros[s][0])-1])
          if erros[s][1] == 1:            
            movimentacao[int(erros[s][0])-1][(erros[s][1])] = input("Insiria corretamente o dia: ")
          if erros[s][1] == 3:
            movimentacao[int(erros[s][0])-1][(erros[s][1])] = func1.complementadigitos(input("Insiria corretamente numero da conta: "))
          if erros[s][1] == 4:
            movimentacao[int(erros[s][0])-1][(erros[s][1])] = input("Insiria corretamente digito verificador: ")
          if erros[s][1] == 5:
            movimentacao[int(erros[s][0])-1][(erros[s][1])] = func1.complementadigitos(input("Insiria corretamente numero da conta: "))
          if erros[s][1] == 6:
            movimentacao[int(erros[s][0])-1][(erros[s][1])] = input("Insiria corretamente digito verificador da conta debito: ")
          if erros[s][1] == 8:
            movimentacao[int(erros[s][0])-1][(erros[s][1])] = input("Insiria corretamente o valor: ")

        print('\nConcluido!')
      else:
        continue

#  ==========  Menu opcao "(P)"  ==========

  elif opcao == 'P':
    
# Chamando a funcao critica 

    erros = func1.critica(contas, movimentacao) 

    if len(erros) == 1:
      print("\n\t======= Erro! a critica de movimentacao acusou erro(s), corrija os erro(s) para prosseguir! =======\n\t")

    if len(erros) == 0:
# Espia de antes de processar
      print(contas)

# Processamentos do tipo creditar
      for i in range(len(movimentacao)):
        indice = func1.buscaConta(movimentacao[i][3],contas)
        movimentacao[i][8] = int(movimentacao[i][8])
        if movimentacao[i][2] == 'C':
          contas[indice][4] += movimentacao[i][8]
          contas[indice][6] += movimentacao[i][8]
          superior = func1.getSuperior(movimentacao[i][3])
          while superior != None:
            indice = func1.buscaConta(superior,contas)
            contas[indice][4] += movimentacao[i][8]
            contas[indice][6] += movimentacao[i][8]
            superior = func1.getSuperior(superior)

# Processamentos do tipo debitar
        elif movimentacao[i][2] == 'D':
          contas[indice][5] += movimentacao[i][8]
          contas[indice][6] -= movimentacao[i][8]
          superior = func1.getSuperior(movimentacao[i][3])
          while superior != None:
            indice = func1.buscaConta(superior,contas)
            contas[indice][5] += movimentacao[i][8]
            contas[indice][6] -= movimentacao[i][8]
            superior = func1.getSuperior(superior)

# Processamentos do tipo ambas
        else:
          contas[indice][4] += movimentacao[i][8]
          contas[indice][6] += movimentacao[i][8]
          superior = func1.getSuperior(movimentacao[i][3])
          while superior != None:
            indice = func1.buscaConta(superior,contas)
            contas[indice][4] += movimentacao[i][8]
            contas[indice][6] += movimentacao[i][8]
            superior = func1.getSuperior(superior)

          indice = func1.buscaConta(movimentacao[i][5],contas)
          contas[indice][5] += movimentacao[i][8]
          contas[indice][6] -= movimentacao[i][8]
          superior = func1.getSuperior(movimentacao[i][5])
          while superior != None:
            indice = func1.buscaConta(superior,contas)
            contas[indice][5] += movimentacao[i][8]
            contas[indice][6] -= movimentacao[i][8]
            superior = func1.getSuperior(superior)
            

# Espia do resultado do processamento
      print('\n',contas)

#  ==========  Menu opcao "(I)"  ==========

  elif opcao == 'I':

# Tipo de importacao
    tipo_importacao = input("Escolha a importcao (1)contas (2)movimentacao (3)Ambas: ")

# Tratamento de erros da variavel tipo_importacao
    while tipo_importacao not in['1','2','3']:
      print("\n\t======== Erro! Insira corretamente ========\t\n")
      tipo_importacao = input("Escolha a importcao (1)contas (2)movimentacao (3)Ambas: ")

# Importacao de contas e ambas
    if tipo_importacao == '1' or tipo_importacao == '3':
      importacao = input("Insira o caminho ou o nome do arquivo de contas: ")
      while True:
        if importacao == '':
          importacao = input("Insira o caminho ou o nome do arquivo de contas: ")
        else:
          break 
      arq_contas = open( importacao ,'r')
      for linha in arq_contas:
        elemento_conta = linha.replace('\n','').split('\\t')
        if elemento_conta != cabecalho_csv_contas: 
          tipo_conta_2 = elemento_conta[3]
          del(elemento_conta[3])
          elemento_conta.insert(0,tipo_conta_2)
          elemento_conta[4], elemento_conta[5], elemento_conta[6] = int(elemento_conta[4]), int(elemento_conta[5]), int(elemento_conta[6])
          if(func1.buscaConta(elemento_conta[1], contas) == None):
            contas.append(elemento_conta) 
      arq_contas.close()

# Importacao das movimentacoes e ambas
    if tipo_importacao == '2' or tipo_importacao == '3':
      importacao = input("Insira o caminho ou o nome do arquivo de movimentacao: ")
      while True:
        if importacao == '':
          importacao = input("Insira o caminho ou o nome do arquivo de movimentacao: ")
        else:
          break
      arq_mov = open(importacao,'r')
      for linha in arq_mov:
        elemento_movimentacao = linha.replace('\n','').split('\\t')
        if elemento_movimentacao != cabecalho_csv_movimentacao:
          if elemento_movimentacao[2] == ' ':
            if elemento_movimentacao != cabecalho_csv_movimentacao: 
              elemento_movimentacao[2] = elemento_movimentacao[4]
              elemento_movimentacao[3] = elemento_movimentacao[5]
              elemento_movimentacao[4] = ' '
              elemento_movimentacao[5] = ' '
              elemento_movimentacao.insert(2, 'C')
              if(func1.buscaRegistro(elemento_movimentacao[0], movimentacao) == None):
                movimentacao.append(elemento_movimentacao)
                
          elif elemento_movimentacao[4] == ' ':
              elemento_movimentacao.insert(2, 'D')
              if(func1.buscaRegistro(elemento_movimentacao[0], movimentacao) == None):
                movimentacao.append(elemento_movimentacao)
              
          else:
              elemento_movimentacao.insert(2,'A')
              if(func1.buscaRegistro(elemento_movimentacao[0], movimentacao) == None):
                movimentacao.append(elemento_movimentacao)
              
      arq_mov.close()

    registro = len(movimentacao)
    print("\n\t======= Dados importados com sucesso! =======\t")

# Espia do resultado da importacao       
    print('\n',contas)
    print('\n',movimentacao)
   
#  ==========  Menu opcao "(X)"  ==========

  elif opcao == 'X':

    aux_contas = deepcopy(contas)
    aux_movimentacao = deepcopy(movimentacao)
# Tipo de exportacao
    tipo_exportacao = input("Escolha de exportcao (1)contas (2)movimentacao (3)Ambas: ")

# Tratamento de erros da variavel tipo_exportacao
    while tipo_exportacao not in['1','2','3']:
      print("\n\t======== Erro! Insira corretamente ========\t\n")
      tipo_exportacao = input("Escolha de exportacao (1)contas (2)movimentacao (3)Ambas: ")

# Exportacao das contas e ambas
    if tipo_exportacao == '1' or tipo_exportacao == '3':
      arq_contas_export = open( str(date.today())+'_Contas.csv','w')
      csv_formatado = ''
      csv_formatado += '\\t'.join(cabecalho_csv_contas) + '\n'
      for conta in aux_contas:
        tipo_conta_2 = conta[0]
        del(conta[0])
        conta.insert(3,tipo_conta_2)
        for i in range(len(conta)):
          conta[i] = str(conta[i])
        csv_formatado += '\\t'.join(conta) + '\n'
      arq_contas_export.write(csv_formatado)   
      arq_contas_export.close()

# Exportacao das movimentacoes e ambas
    if tipo_exportacao == '2' or tipo_exportacao == '3':   
      arq_mov_export = open(str(date.today())+'_Movimentacao.csv','w')
      csv_formatado = ''
      csv_formatado+='\\t'.join(cabecalho_csv_movimentacao)+'\n'
      for mov in aux_movimentacao:
          if  mov[2] == 'C':
              mov[5] = mov[3]
              mov[6] = mov[4]
              mov[3] = ' '
              mov[4] = ' '
              del(mov[2])
              for i in range(len(mov)):
                mov[i] = str(mov[i])         
              csv_formatado += '\\t'.join(mov) + '\n'
          elif mov[2] == 'D':
              del(mov[2])
              for i in range(len(mov)):
                mov[i] = str(mov[i])           
              csv_formatado += '\\t'.join(mov) + '\n'          
          else:
              del(mov[2])
              for i in range(len(mov)):
                mov[i] = str(mov[i])
              csv_formatado += '\\t'.join(mov) + '\n'
      arq_mov_export.write(csv_formatado)             
      arq_mov_export.close()              
  
    print("\n\t======= Exportacao concluida! =======\t\n")

#  ==========  Menu opcao "(B)"  ==========

  elif opcao == 'B':
    print("\n===== Imprimir balanco de contas =====\n")
    func1.balancete(contas)
    
#  ==========  Menu opcao "(S)"  ==========

  elif opcao == 'S':
    print("\nFim do programa ....")
    break
