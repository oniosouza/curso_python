'''
Atribuicao condicional ou(if ternario em outras liguagens)
é uma estrutura utilizada para simplificar o codigo, onde
o valor a ser atribuido será aquele que satisfizer a condicao.

<variavel> = <valor1> if (true) else <valor2>

var = 10 if (true) else 20


'''
'''x = 10
texto = "sim" if x == 10 else "nao"
print(texto)

x = 9
texto = "sim" if x == 10 else "nao"
print(texto)'''
num1 = int(input("digite um numero"))
s = "par" if num1 % 2 == 0 else "impar"
print(s)