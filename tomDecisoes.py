#TOMADA DE DECIOSOES

nota1 = float(input("digite a primeira nota:"))
print("a primeira nota é:", nota1, "\n")

nota2 = float(input("digite a segunda nota:"))
print("a segunda nota é:", nota2, "\n")

nota3 = float(input("digite a terceira nota:"))
soma = nota1 + nota2 + nota3
print("a terceira nota é:", nota3, "\n")
print("a soma entre as notas é; "(nota1+nota2+nota3, soma))



media = (nota1 + nota2 + nota3)/3

if(media >= 6):
    print("aluno aprovado")
else:
    print("aluno reprovado")
