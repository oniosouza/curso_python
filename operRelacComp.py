
'''idade = int(input("informe sua idade"))
if(idade<=0):
    print("sua idade mao pode ser zero ou menor que zero")
else:
    if(idade>150):
        print("a sua idade nao pode ser superior a 150 anos")
    else:
        if(idade<18):
            print("voce precisa ter mais que 18 anos")'''
#com elif
idade = int(input("informe sua idade"))
if(idade<=0):
    print("sua idade mao pode ser zero ou menor que zero")
elif(idade>150):
    print("a sua idade nao pode ser superior a 150 anos")
elif(idade<18):
    print("voce precisa ter mais que 18 anos")
