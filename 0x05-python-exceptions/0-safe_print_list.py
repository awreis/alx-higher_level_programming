#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print('{}\n'.format(i))
        if x > my_list:
            return x
    except:
        print('An error occured')

