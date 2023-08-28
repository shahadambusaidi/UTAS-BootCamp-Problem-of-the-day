#Prob12
 
def alternate_positive_negative(input_array):
    positive_numbers = []
    negative_numbers = []

    for number in input_array:
        if number > 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)

    result = []
    p_index, n_index = 0, 0
    p_len, n_len = len(positive_numbers), len(negative_numbers)

    while p_index < p_len and n_index < n_len:
        result.append(positive_numbers[p_index])
        result.append(negative_numbers[n_index])
        p_index += 1
        n_index += 1

    while p_index < p_len:
        result.append(positive_numbers[p_index])
        p_index += 1

    while n_index < n_len:
        result.append(negative_numbers[n_index])
        n_index += 1

    return result

# Example input array
input_array = [1, -2, 3, -4, 5, -6]
result = alternate_positive_negative(input_array)
print("Alternate positive & negative array:", result)