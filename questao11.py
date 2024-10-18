def conversao(temperatura, escala):
  if escala == 1:
    resultado = (temp * 9/5) + 32
    return resultado
  
  else:
    resultado = (temperatura - 32) * 5/9
    return resultado
 
escala = int(input("Digite '1' para converter de C° para F° ou '2' para coverter de F° para C°: "))

if escala != 1 and escala != 2:
  print("Valor inserido inválido!")
  exit()

if escala == 1:
    temperatura = float(input("Digite a temperatura em Celsius: "))
    resultado = conversao (temperatura, escala)
    print(f"A temperatura é: {resultado:.2f} F°")

else:
    temperatura = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = convesao(temperatura, escala)
    print(f"A temperatura é: {resultado:.2f} C°")
