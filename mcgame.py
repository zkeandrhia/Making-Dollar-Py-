'''gets the user to enter the number of coins required
to make exactly one dollar. 
The program should prompt the user to 
enter the number of pennies, nickels, dimes, 
and quarters. 

If the total value of the coins 
entered is equal to one dollar, the program should 
congratulate the user for winning the game. 
Otherwise, the program should display a message 
indicating whether the amount entered was more
than or less than one dollar.
'''

def coins():
    
    pennies = int(input('Enter number of pennies: '))
    nickels = int(input('Enter number of nickels: '))
    dimes = int(input('Enter number of dimes: '))
    quarters = int(input('Enter number of quarters: '))

    if pennies > 100:
       print(f'\nPennies: {pennies} is greater than the number to create a dollar.')
    elif pennies < 100:
       print(f'\nPennies: {pennies} is less than the number to create a dollar.')
       
    if nickels > 20:
       print(f'\nNickels: {nickels} is greater than the number to create a dollar.')
    elif nickels < 20:
       print(f'\nNickels: {nickels} is less than the number to create a dollar.')
    
    if dimes > 10:
       print(f'\nDimes: {dimes} is greater than the number to create a dollar.')
    elif dimes < 10:
       print(f'\nDimes: {dimes} is less than the number to create a dollar.')
    
    if quarters > 4:
       print(f'\nQuarter: {quarters} is greater than the number to create a dollar.')
    elif quarters < 4:
       print(f'\nQuarter: {quarters} is less than the number to create a dollar.')
       
    if pennies == 100 and nickels == 20 and dimes == 10 and quarters == 4:
        print('Congratulations you create a 1 Dollar!')
coins()
    