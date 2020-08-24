# -*- coding: utf-8 -*-

import questions as qt
import os



def main():
    menu = None
    while menu != '0':
        os.system('cls')
        print('1 - Distância média percorrida por viagens com no máximo 2 passageiros.')
        print('2 - 3 maiores vendors em quantidade total de dinheiro arrecadado.')
        print('3 - Histograma mensal de corridas pagas em dinheiro.')
        print('4 - Série temporal em relação à quantidade de gorjetas diárias nos 3 últimos meses de 2012.')
        print('5 - Tempo médio das corridas nos dias de sábado e domingo;.')
        print('0 - Sair da aplicação.')
        menu = input('\nDigite o número referente à análise desejada: ')

        if menu == '1':
            qt.question1() 
            input('\nAperte qualquer botão para continuar...')
        elif menu == '2':
            qt.question2() 
            input('\nAperte qualquer botão para continuar...')
        elif menu == '3':
            qt.question3() 
            input('\nAperte qualquer botão para continuar...')
        elif menu == '4':
            qt.question4() 
            input('\nAperte qualquer botão para continuar...')
        elif menu == '5':
            qt.question5() 
            input('\nAperte qualquer botão para continuar...')
        elif menu == '0':
            print('\nSaindo...')
        else:
            print('\nOpção inválida.')
            input('\nAperte qualquer botão para continuar...')


if __name__ == '__main__':
    main()