print('Vasco da Gama')

def func(qtd_notas):
    soma_notas = 0
    i = 1
    while(i <= qtd_notas):
        notas = input(f'Insira o valor da nota {i}: ')
        soma_notas += int(notas)
        i = i + 1

    return (float)(soma_notas/qtd_notas)

media = func(3);
print(media)