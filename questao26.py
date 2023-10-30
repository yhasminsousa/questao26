# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

# Solicita o primeiro termo e a razão da PoA ao usuário
a1 = int(input("Digite o primeiro termo da PoA: "))
r = int(input("Digite a razão da PoA: "))

# Calcula e imprima os 10 primeiros termos da PoA
for i in range(10):
    print(i)
    termo = a1 + i * r
    print(f'Termo {i+1}: {termo}')