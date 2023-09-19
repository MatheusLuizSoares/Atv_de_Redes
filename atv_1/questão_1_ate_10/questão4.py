#Faça um programa que leia um valor inteiro correspondente a um ano e diga se o ano informado é bissexto ou não.
ano=input(int("Digite o ano"))
resto= ano %2
bissexto= (ano/4)/2
if 