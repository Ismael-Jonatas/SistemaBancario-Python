# Funcao para printar o menu
def menu ():
  print("\nSelecione a opcao desejada:\n(c) Cadastrar contas.\n(d) Digitar movimento financeiro.\n(a) Critica do movimento financeiro.\n(p) Processar movimento.\n(i) Importar arquivo CSV:\n    > contas.\n    > movimnentacao financeira.\n(x) Exportar dados:\n    > contas.\n    > movimentacao\n(b) Imprimir balancete.\n(s) Sair.")

# Funcao para completar os digitos que falta no numero da conta
def complementadigitos(conta):
    return conta + ('0'* (11-len(conta)))

# Funcao para encurtar o numero da conta
def obterContaCurta( conta ):
    for i in range(len(conta)-1,-1,-1):
        if( conta[i] != '0'):
            break

    contaCurta = conta[:i+1]

    size = len(contaCurta)
    numZeros = 0

    if (size == 3 or size == 5 or size == 8 or size == 10):
        numZeros = 1
    elif (size == 7):
        numZeros = 2
    contaCurta += ('0'* numZeros)
    return contaCurta

# Funcao para buscar as contas superiores
def getSuperior(conta):  
    cc = obterContaCurta(conta)
    tam = len(cc)
    if (tam == 1):
        return None
    
    tabela = [1,2,4,6,9,11]
    nivel = tabela.index(tam) - 1

    cc = cc[: tabela[nivel]]
    return complementadigitos(cc)

# Funcao para Calcular o digito verificador     
def checkconta(conta):
      pesos = '27654327654'
      somador = 0

      for i in range(0,11):
        somador += int(conta[i])*int(pesos[i])

      resto_divisao = somador % 11
      resto_divisao_1 = 11 - resto_divisao 

      if resto_divisao_1 == 10:
        resto_divisao_1 = 0

      elif resto_divisao_1 == 11:
        resto_divisao_1 = '&'

      return resto_divisao_1

# Funcao para mostra os erros da parte da movimentacao
def critica(contas, movimentacao):
  contas_3 = []
  contas_4 = []
  erros = []
  for i in range(len(movimentacao)):
    for j in range(1,len(movimentacao[i])):
      movimentacao[i][j] = str(movimentacao[i][j])

  for i in range(len(contas)):
    contas_3.append([contas[i][1],contas[i][0]])
    contas_4.append(contas[i][1])
    
  for i in range(len(movimentacao)):
# Critica na variavel  valor  
    if movimentacao[i][-1] == '' or movimentacao[i][-1].isnumeric() == False:
      print(f'Registro: {(movimentacao[i][0])}, O valor esta ausente!')
      erros.append([movimentacao[i][0], 8])
      
# Critica na variavel dia  
    if int(movimentacao[i][1]) > 31 or (movimentacao[i][1]) == '00':
      print(f'Registro: {(movimentacao[i][0])}, Dia invalido!')
      erros.append([movimentacao[i][0], 1])

# Tipo de movimentacao ambas
    if movimentacao[i][2] == 'A':

# Critica na variavel digito_verificador  
      if checkconta(movimentacao[i][3]) != int(movimentacao[i][4]):
        print(f'Registro: {(movimentacao[i][0])}, O digito nao corresponde na conta debito')
        erros.append([movimentacao[i][0], 4])

# Critica na variavel digito_verificador_2
      if checkconta(movimentacao[i][5]) != int(movimentacao[i][6]):
        print(f'Registro: {(movimentacao[i][0])}, O digito nao corresponde na conta credito')
        erros.append([movimentacao[i][0], 6])

# Verificador de conta  debito
      if (movimentacao[i][3]  not in contas_4):
        print(f'Registro: {(movimentacao[i][0])}, A conta de debito nao existe!')
        erros.append([movimentacao[i][0], 3])

# Verifivdor de conta credito
      if (movimentacao[i][5]  not in contas_4):
        print(f'Registro: {(movimentacao[i][0])}, A conta de credito nao existe!')
        erros.append([movimentacao[i][0], 5])

# Verificar de conta sintetica debito
      for l in range(len(contas_3)):
        if (movimentacao[i][3] in contas_3[l][0]) and (contas_3[l][1] == 'S'):
          print(f'Registro: {(movimentacao[i][0])}, A conta de debito e sintetica!')
          erros.append([movimentacao[i][0], 3])
# Verificar de conta sintetica credito
        if (movimentacao[i][5] in contas_3[l][0]) and (contas_3[l][1] == 'S'):
          print(f'Registro: {(movimentacao[i][0])}, A conta de credito e sintetica!')
          erros.append([movimentacao[i][0], 5])

# Tipo de movimetacao creditar e debitar
    else:

# Critica da variavel digito_verificador 
      if checkconta(movimentacao[i][3]) != int(movimentacao[i][4]):
        print(f'Registro: {(movimentacao[i][0])}, Tipo da conta: {(movimentacao[i][2])}, O digito nao corresponde')
        erros.append([movimentacao[i][0], 4])

# Verificafor de conta 
      if (movimentacao[i][3]  not in contas_4):
        print(f'Registro: {(movimentacao[i][0])}, Tipo da conta: {(movimentacao[i][2])}, Nao existe!')
        erros.append([movimentacao[i][0], 3])
# Verificador de conta sintetica 
      for l in range(len(contas_3)):
        if (movimentacao[i][3] in contas_3[l][0]) and (contas_3[l][1] == 'S'):
          print(f'Registro: {(movimentacao[i][0])}, Tipo da conta: {(movimentacao[i][2])}, A conta e sintetica!')
          erros.append([movimentacao[i][0], 3])
  return erros

# Funcao para busca o indece da conta passada no arrey de contas
def buscaConta(conta, contas):
  for c in contas:
    if c[1] == conta:
      return contas.index(c)
  return None

# Funcao para buscar o indice do registro 
def buscaRegistro(registro, movimentacao):
  for r in movimentacao:
    if r[0] == registro:
      return movimentacao.index(r)
  return None

# Funcao para organizar as contas
def sortContas(conta):
    return int(conta[1])

# Funcao para printar o balancete    
def balancete(contas):
  contas.sort(key=sortContas)
  print('''
  ------------------------------------------------------------------------------------------
  Contas
  ------------------------------------------------------------------------------------------
  ''')
  totDesp = 0
  totCred = 0
  totGeral = 0
  for conta in contas:
    if len(obterContaCurta(conta[1])) == 1:
      totCred+=conta[4]
      totDesp+=conta[5]
      totGeral+=conta[6]
    print(contaBalancete(conta))
  
  print(f'''
  ------------------------------------------------------------------------------------------
  Total de Receitas                      Total de Despesas                      Saldo
  ------------------------------------------------------------------------------------------
  R$ {str(totCred).ljust(36)}R$ {str(totDesp).ljust(36)}R$ {str(totGeral)}
  ''')
  return
  
def contaBalancete(conta):
  if len(obterContaCurta(conta[1])) == 1:
    return f'  {obterContaCurta(conta[1])}. {str(conta[3]).ljust(84-len(str(conta[6])))}R$ {conta[6]}'
  if len(obterContaCurta(conta[1])) == 2:
    return f'    {obterContaCurta(conta[1])}. {str(conta[3]).ljust(81-len(str(conta[6])))}R$ {conta[6]}'
  if len(obterContaCurta(conta[1])) == 3:
    return f'      {obterContaCurta(conta[1])}. {str(conta[3]).ljust(78-len(str(conta[6])))}R$ {conta[6]}'
  if len(obterContaCurta(conta[1])) == 4:
    return f'        {obterContaCurta(conta[1])}. {str(conta[3]).ljust(75-len(str(conta[6])))}R$ {conta[6]}'
  if len(obterContaCurta(conta[1])) == 5:
    return f'          {obterContaCurta(conta[1])}. {str(conta[3]).ljust(72-len(str(conta[6])))}R$ {conta[6]}'
  if len(obterContaCurta(conta[1])) == 6:
      return f'          {obterContaCurta(conta[1])}. {str(conta[3]).ljust(69-len(str(conta[6])))}R$ {conta[6]}'
