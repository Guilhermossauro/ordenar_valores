lista = []
for n in range(5):
    n = int(input(f'\nEntre com o valor para N{n+1}: '))   
    lista.append(n)
    lista.sort(reverse=True)
    print (lista)
input("\nPressione qualquer tecla para fin1alizar")