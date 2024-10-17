def square_digits(num):
    num_str = str(num)
    result_str = ""

    for digit in num_str:
        square = int(digit) ** 2
        result_str += str(square)

    transformed_number = int(result_str)
    return transformed_number
