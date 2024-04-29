import random


def my_generator():
    new_list = []
    for _ in range(200):
        random_number = random.randint(-19, 50)
        new_list.append(random_number)
    return new_list

if __name__ == "__main__":
    result = my_generator()
    print(result)




