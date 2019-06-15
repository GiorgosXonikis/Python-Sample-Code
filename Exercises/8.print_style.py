
# 8.Print Style
# Write a small script that will print numbers 1-10 in a way that if
# the number is even it prints the number, if the number is odd it print
# underscore _:

# _2_4_6_8_10
list_1_10 = list(range(1, 11))

output_string = ''
for num in list_1_10:
    if num % 2 != 0:
        output_string += '_'
    else:
        output_string += str(num)

print(output_string)
