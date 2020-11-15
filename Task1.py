#1. В первый день спортсмен пробежал `x` километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу `y` определите номер дня, на который пробег спортсмена составит не менее `y` километров.
# Программа получает на вход числа `x` и `y` и должна вывести одно число - номер дня.


some_distance = int(input('Insert - '))
some_distance1 = int(input('Insert - '))
number_of_day = 1
while some_distance < some_distance1:
    some_distance *= 1.1
    number_of_day += 1
print(number_of_day)
