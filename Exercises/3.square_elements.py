
# 3.Squared Even Numbers
#Write a program which uses map() and filter() to make a list of elements
# that are the squares of the even numbers in [1,2,3,4,5,6,7,8,9,10].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_even_numbers = list(filter(lambda x: x % 2 == 0, map(lambda y: y ** 2, numbers)))
# or the other way around
square_even_numbers2 = list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(square_even_numbers)
print(square_even_numbers2)
