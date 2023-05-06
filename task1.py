'''«100 спичек». Из кучки, первоначально содержащей 100 спичек, двое играющих поочередно
 берут по несколько спичек: не менее одной и не более десяти. Проигрывает взявший последнюю спичку.'''

n = 100

turn = 1

while n != 0:

    print('Sticks left: ', n)

    if turn % 2 == 1:
        turn_in = int(input(('Choose number from 1 to 10 (player 1) ')))

        if (turn_in > n) or (turn_in < 1) or (turn_in > 10):
            print('Wrong turn')

        else:
            n -= turn_in
            turn += 1

    else:
        turn_in = int(input(('Choose number from 1 to 10 (player 2) ')))

        if (turn_in > n) or (turn_in < 1) or (turn_in > 10):
            print('Wrong turn')

        else:
            n -= turn_in
            turn += 1


if turn % 2 == 1:
    print('Player 1 win!')

else:
    print('Player 1 win!')