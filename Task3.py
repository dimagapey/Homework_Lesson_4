#3. Даны два целых числа `A` и `В`.
# Выведите все числа от `A` до `B` включительно,
# в порядке возрастания, если `A < B`,
# или в порядке убывания в противном случае.

a = int(input('Введите какое-либо число "A": '))
b = int(input('Введите какое-либо число "B": '))

def s_list1(a, b):
    some_list = []
    for i in range(a, b + 1, 1):
        some_list.append(i)
    return some_list

def s_list2(a, b):
    some_list2 = []
    for x in reversed(range(b, a + 1, 1)):
        some_list2.append(x)
    return some_list2

if a <= b:
    print(s_list1(a, b))
else:
    print(s_list2(a, b))