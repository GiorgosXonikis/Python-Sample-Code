
# 6.Input and Range
# Given an integer n, write a program that generates a dictionary with
# entries from 1 to n. For each key i, the corresponding value should
# be i*i.


def range_dict(_max):
    my_dict = {}
    for i in range(1, _max + 1):
        my_dict[i] = i ** 2

    return my_dict

# or with dictionary Comprehension
def range_dict2(_max):
    return  {i: i ** 2 for i in range(1, _max + 1)}


print(range_dict(10))
print(range_dict2(10))

# for n=10:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
