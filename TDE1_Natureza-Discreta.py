#Emmanuel Antonieti Ribeiro dos Santos
def obter_operacao(letra_operacao):
  operacoes = {
      'U': lista_uniao,
      'I': lista_interseccao,
      'D': lista_diferenca,
      'C': produto_cartesiano
  }
  return operacoes.get(letra_operacao.upper(), None)

def criar_lista(s):
  return [item.strip() for item in s.split(',')]

def lista_uniao(conjuntoA, conjuntoB):
  uniao = []
  for elemento in conjuntoA:
      if elemento not in uniao:
          uniao.append(elemento)
  for elemento in conjuntoB:
      if elemento not in uniao:
          uniao.append(elemento)
  return uniao

def lista_interseccao(conjuntoA, conjuntoB):
  interseccao = []
  for elemento in conjuntoA:
      if elemento in conjuntoB:
          interseccao.append(elemento)
  return interseccao

def lista_diferenca(conjuntoA, conjuntoB):
  diferenca = []
  for elemento in conjuntoA:
      if elemento not in conjuntoB:
          diferenca.append(elemento)
  return diferenca

def produto_cartesiano(conjuntoA, conjuntoB):
  return [(a, b) for a in conjuntoA for b in conjuntoB]

def ler_arquivo(arquivo):
  with open(arquivo, 'r') as f:
      linhas = f.readlines()

  num_operacoes = int(linhas[0].strip())
  operacoes = []
  linha_atual = 1
  for i in range(num_operacoes):
      operacao = linhas[linha_atual].strip()
      conjuntoA = criar_lista(linhas[linha_atual + 1].strip())
      conjuntoB = criar_lista(linhas[linha_atual + 2].strip())
      operacoes.append((operacao, conjuntoA, conjuntoB))
      linha_atual += 3

  return operacoes

def main():
  arquivo = 'arquivo.txt'

  operacoes = ler_arquivo(arquivo)

  for operacao, conjuntoA, conjuntoB in operacoes:
      operar = obter_operacao(operacao)

      if operar:
          resultado = operar(conjuntoA, conjuntoB)
          if operacao == "U":
              print(f"União: conjunto 1 {conjuntoA}, conjunto 2 {conjuntoB}. Resultado: {resultado} \n")
          if operacao == "I":
              print(f"Intersecção: conjunto 1 {conjuntoA}, conjunto 2 {conjuntoB}. Resultado: {resultado} \n")
          if operacao == "D":
              print(f"Diferença: conjunto 1 {conjuntoA}, conjunto 2 {conjuntoB}. Resultado: {resultado} \n")
          if operacao == "C":
              print(f"Produto Cartesiano: conjunto 1 {conjuntoA}, conjunto 2 {conjuntoB}. Resultado: {resultado} \n")
          else:
              None
      else:
          print(f"Operação {operacao} inválida")

if __name__ == "__main__":
  main()
