#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    total = 0
    for number in my_list:
        if number not in unique_list:
            unique_list.append(number)
            total += number
    return total
