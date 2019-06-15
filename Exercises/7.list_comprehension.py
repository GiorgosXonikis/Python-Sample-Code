
# 7.List Comprehension
# Using List comprehension generate a list where the values are the
# squares of 1 to 20 (both included). Then print the last 5 elements
# in the list.

original_list = list(range(1,21))
sqrs_list = [num ** 2 for num in original_list][-5:]

print(sqrs_list)
