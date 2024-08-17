numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
else:
  print("Número inválido. Digite um número entre 1 e 10.")



numeros = []
for i in range(10):
  numero = int(input(f"Digite o {i+1}º número inteiro: "))
  numeros.append(numero)

maior_valor = numeros[0]
posicao = 0
for i in range(1, len(numeros)):
  if numeros[i] > maior_valor:
    maior_valor = numeros[i]
    posicao = i

print(f"O maior valor é {maior_valor} e está na posição {posicao}.")



n = int(input())

a = 0
b = 1

for i in range(n):
  print(a, end=" ")
  a, b = b, a + b