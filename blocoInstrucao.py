
num1 = int(input("digite um numero"))
if(num1 > 10):
    print("o valor é maior que 10")
    if(num1 <= 15):
        print("o valor é maior que 10, e menor que 15")
    else:
        if(num1 <= 50):
            print("o valor é maior do que 10. e menor que 15")
        else:
            print("o valor é maior que 50")
else:
    if(num1 > 5):
        print("o numero é maior que 10. mas: maior que 5")
        if(num1==7):
            print("o numero é igual a 7.")
    else:
            print("o numero é menor que 5")