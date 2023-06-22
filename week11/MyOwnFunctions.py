def check_int(number):
    if type(number) == int:
        return number
    else:
        return


def check_list_empty(num_list):
    if not num_list:
        return num_list


def remove_none(value: None, list_of_number):
    while value in list_of_number:
        list_of_number.remove(value)
    return list_of_number


def check_float(number):
    if type(number) == float:
        return number


def split_type(num_list):
    check_list_empty(num_list)
    list_of_int = remove_none(None, [check_int(each) for each in num_list])
    list_of_float = remove_none(None, [check_float(each) for each in num_list])
    return list_of_int, list_of_float


def list_of_odd(num_list, list_of_odd_num):
    if not num_list:
        return list_of_odd_num
    if num_list[0] % 2 == 1:
        list_of_odd_num.append(num_list[0])
    return list_of_odd(num_list[1:], list_of_odd_num)


def keep_two_dup(num_list):
    result = []

    for num in num_list:
        if result.count(num) < 2:
            result.append(num)
        else:
            continue

    return result
