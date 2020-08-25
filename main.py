# -*- coding: utf-8 -*-

import questions as qt
import os



def main():
    menu = None
    while menu != '0':
        os.system('cls')
        print('---------------------------------------------------------------------------------------')
        print('                                   NYC Taxi Trips')
        print('---------------------------------------------------------------------------------------\n\n')
        print('1 - Average distance traveled by trips with a maximum of 2 passengers per year.')
        print('2 - 3 biggest vendors in total amount of money raised.')
        print('3 - Monthly histogram of races paid in cash.')
        print('4 - Time series in relation to the amount of daily tips in the last 3 months of 2012.')
        print('5 - Average race time on Saturday and Sunday per year.')
        print('0 - Exit the application.')
        menu = input('\nEnter the number for the desired analysis: ')

        if menu == '1':
            print('\nWait while loading...')
            qt.question1() 
            input('\nPress ENTER to continue...')
        elif menu == '2':
            print('\nWait while loading...')
            qt.question2() 
            input('\nAPress ENTER to continue...')
        elif menu == '3':
            print('\nWait while loading...')
            qt.question3() 
            input('\nPress ENTER to continue...')
        elif menu == '4':
            print('\nWait while loading...')
            qt.question4() 
            input('\nPress ENTER to continue...')
        elif menu == '5':
            print('\nWait while loading...')
            qt.question5() 
            input('\nPress ENTER to continue...')
        elif menu == '0':
            print('\nSaindo...')
        else:
            print('\nInvalid option.')
            input('\nPress ENTER to continue...')


if __name__ == '__main__':
    main()