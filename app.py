# projeto impar ou par
try:
    valor = int(input('digite um valor'))
    if valor % 2 ==0:
        print('numero par')
    else:
         print('numero impar')

except:
    print('Digite apenas números')