correct_height = 93

while True:
    user_input = input('Milyen magas a New-York-i Szabadság-szobor? (Írd be "exit" a kilépéshez): ')

    if user_input.lower() == 'exit':
        print('Kilépés... Köszönöm a játékot!')
        break

    if user_input.isdigit():
        guess = int(user_input)

        if guess == correct_height:
            print('Gratulálok, eltaláltad!')
            break
        elif guess < correct_height:
            print('Nem, ennél kicsit magasabb.')
        else:
            print('Nem, ennél kicsit alacsonyabb.')
    else:
        print('Kérlek, adj meg egy számot vagy írd be "exit" a kilépéshez.')



