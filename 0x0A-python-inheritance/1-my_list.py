#!/usr/bin/python3
"""Module 1-my_list.
Creates a class that inherits from list
"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Prints list in ascending order"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
