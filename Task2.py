the_new_numb = None
all_numbers = []
while the_new_numb != 0:
    print('Введите, пожалуйста, целое, не отрицательное число - ')
    the_new_numb = int(input())
    if the_new_numb == 0:
        break
    all_numbers.append(the_new_numb)

def make_calculation(all_numbers):
    digits_count = 0
    digits_sum = 0
    digits_multiply = 1
    digits_count_1 = 0
    digits_count_2 = 0
    max_digit = 0
    last_element = 0
    max_elements = 0
    for i, value in enumerate(all_numbers):
        digits_count += 1
        digits_sum += value
        digits_multiply *= value
        if value > max_digit:
            max_digit = value
            max_digit_index = 1
        if value < max_digit:
            second_max_digit = value
            second_max_index = 1
        if value % 2 == 0:
            digits_count_1 += 1
        if value + last_element == max_digit:
                max_elements += 1
        else:
            digits_count_2 += 1
        last_element = value

    digits_avg = digits_sum / digits_count
    return (digits_count, digits_sum, digits_multiply,
            digits_avg, max_digit_index, second_max_digit,
            second_max_index, digits_count_1, digits_count_2)

print(make_calculation(all_numbers))
