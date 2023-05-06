'''«Ипподром». Играющий выбирает одну из трех лошадей, состязающихся на багах, и выигрывает,
 если его лошадь приходит первой. Скорость передвижения лошадей на разных этапах выбирается
 программой с помощью датчика случайных чисел.'''

import random

n = 3 # Stage amount

time = [] # List with time for complete

time_horse = 0

horse = int(input('Choose horse (1, 2, 3): ')) - 1

route_length = 60

stages_length = [10, 30, 20]

for i in range(0, 3):
    for j in stages_length:
        time_horse += j / random.randint(1, 5) # time for stage

    time.append(time_horse)
    time_horse = 0

print(time)

if horse == time.index(min(time)):
    print('Player win!')

else:
    print('Player lose!')

