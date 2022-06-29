a = 1
b = 2

def soma_num (var1, var2):
    s = var1+var2 #A
    return s      #A
def imprime (x_vezes):
    for i in range (x_vezes):#B
        print(i) #C          #B

print (soma_num (a, b))
imprime (5)
'''
as variaveis a e b estao declaradas no escopo global
1)todos, representam o primeiro escopo ou escopo global
A) representa o segundo escopo
B) representa o terceiro escopo
C) representa o quarto escopo
'''