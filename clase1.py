notas = []

while True:
    entrada = input("ingresa un a nota (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print('Por avor, ingresa un numero valida.')

if len(notas) >0:
    promedio = sum(notas) / len(notas)
    print(f'El promedio de las notas es: {promedio:.2f}')
else:
    print('no se ingresaron las notas.')