
# 2.Square Elements
#Write a program that accepts a list and returns the square of each element.
# The list is: [1,2,3,4,5,6,7,8,9,10].


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = [num ** 2 for num in numbers]
square_numbers_map = list(map(lambda num: num ** 2, numbers))

print(square_numbers)
print(square_numbers_map)
