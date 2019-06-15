# 1.Even Numbers
# Write a program which can filter even numbers in a list by using filter
# function. The list is: [1,2,3,4,5,6,7,8,9,10].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))

print(even_numbers)
print(even_numbers_filter)
