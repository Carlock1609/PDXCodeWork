#! python3

import string, random

def get_lower():
    # Lower loop
    pass_length_lower = (int(input("Please enter in how many lower_case letters you want: ")) - 1)

    lower_case_gen = string.ascii_lowercase
    lower_case = []

    while len(lower_case) <= pass_length_lower:
        rand_lower_letter = random.choice(lower_case_gen)
        lower_case.append(rand_lower_letter)
    return "".join(lower_case)

def get_upper():
    # Upper loop
    pass_length_upper = (int(input("Please enter in how many upper_case letters you want: ")) - 1)

    upper_case_gen = string.ascii_uppercase
    upper_case = []

    while len(upper_case) <= pass_length_upper:
        rand_length_upper = random.choice(upper_case_gen)
        upper_case.append(rand_length_upper)
    return "".join(upper_case)

def get_nums():
    # Nums loop
    pass_length_nums = (int(input("Please enter in how many numbers do you want: ")) - 1)

    number_list_gen = string.digits
    numbers_list = []

    while len(numbers_list) <= pass_length_nums:
        rand_length_nums = random.choice(number_list_gen)
        numbers_list.append(rand_length_nums)
    return "".join(numbers_list)

def get_chars():
    # Special char loop
    pass_length_special = (int(input("Please enter in how many special characters do you want: ")) - 1)

    special_char_list = "!@#$%^&*"
    special_chars = []

    while len(special_chars) <= pass_length_special:
        rand_length_special = random.choice(special_char_list)
        special_chars.append(rand_length_special)
    return "".join(special_chars)

def main():
    password = [get_lower(), get_upper(), get_nums(), get_chars()]
    print("".join(password))

main()
