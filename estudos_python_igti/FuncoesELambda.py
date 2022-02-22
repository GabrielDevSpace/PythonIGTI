# Funções
# Lambda funções anonimas em que nao damos um nome a ela


print("#################### CALCULO IMC ######################")

x = input(f"Digite seu Peso:")
y = input(f"Digite sua Altura:")
peso = float(x)
altura = float(y)

def imc(peso, altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        print("Seu IMC é:", round(imc, 2), "| Magreza")
    elif imc >= 18.5 and imc <= 24.9:
        print("Seu IMC é:", round(imc, 2), "| Normal")
    elif imc >= 25.0 and imc <= 29.9:
        print("Seu IMC é:", round(imc, 2), "| Sobrepeso")
    elif imc >= 30.0 and imc <= 39.0:
        print("Seu IMC é:", round(imc, 2), "| Obesidade")
    else:
        print("Seu IMC é:", round(imc, 2), "| Obesidade Grave")
    return
imc(peso, altura)


def peso_ideal(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        while imc <= 18.5:
            peso += 1
            imc = peso / (altura ** 2)
    elif imc > 24.0:
        while imc >= 24.9:
            peso -= 1
            imc = peso / (altura ** 2)
    print("Seu peso Ideal é: ", peso)
    return
peso_ideal(peso, altura)


# Função Lambda
x = 1000
y = 3500
soma = lambda x, y: x * y