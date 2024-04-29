import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.generator import my_generator



def bubble_sort(come_list: list[int]) -> list[int]:
    length_list = len(come_list)

    for count in range(length_list - 1):
        for index in range(length_list - 1 - count):
            if come_list[index] > come_list[index + 1]:
                come_list[index], come_list[index + 1] = come_list[index + 1], come_list[index]
    return come_list            



if __name__ == "__main__":
    result = bubble_sort(my_generator())
    print(result)



