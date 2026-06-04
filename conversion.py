user_inp = input('''Press "C" to convert fahrenheit into celsius. 
Press "F" to convert celsius into fahrenheit. : ''')

if user_inp == 'C' or user_inp == 'c':
    fahrenheit = int(input('Enter temperature in fahrenheit: '))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f'{fahrenheit} degree fahrenheit = {celsius} degree celsius.')
elif user_inp == 'F' or user_inp == 'f':
    celsius = int(input('Enter temperature in celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    print(f'{celsius} degree celsius = {fahrenheit} degree fahrenheit.')
else:
    print("Wrong Keyword!!")