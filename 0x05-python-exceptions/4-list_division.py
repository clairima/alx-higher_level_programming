#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")

                value_1 = my_list_1[i]
                value_2 = my_list_2[i]

                if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                    raise TypeError("wrong type")

                result = value_1 / value_2
                result_list.append(result)

            except ZeroDivisionError:
                result_list.append(0)
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
                break
    finally:
        return result_list
