#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        msg = 0
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            msg = "division by 0"
            new_list.append(0)
        except (ValueError, TypeError):
            msg = "wrong type"
            new_list.append(0)
        except IndexError:
            msg = "out of range"
            new_list.append(0)
        finally:
            if msg:
                print(msg)
    return (new_list)
