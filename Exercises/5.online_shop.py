
# 5.Online Shop
# Assume you have an online shop, and you have a list of orders.
# You don’t like that people order in small quantities, which is why you
# would like to add an additional CHF 10 to the total price, for all orders
# that are below CHF 100 in total.

# Write a short Python function compute_totals that returns a list of
# 2-tuples. Each tuple consists of the order number and the total price.
# The total price should be increased by CHF 10 if the total is less than
# CHF 100.

# TODO with filter()
def compute_totals(input_list):
    list_of_lists = []
    output_list = []

    # extract the id and multiple the value with quantity
    for _dict in input_list:
        list_of_lists.append([_dict['id'], _dict['quantity'] * _dict['price_per_item']])

    # check if the total price is under 100 CHF
    for _list in list_of_lists:
        if _list[1] < 100:
            _list[1] += 10

        output_list.append(tuple(_list))

    return output_list


orders = [

    {
        'id': 'order_001',
        'item': 'Introduction to Python',
        'quantity': 1,
        'price_per_item': 32,
    },
    {
        'id': 'order_002',
        'item': 'Advanced Python',
        'quantity': 3,
        'price_per_item': 40,
    },
    {
        'id': 'order_003',
        'item': 'Python web frameworks',
        'quantity': 2,
        'price_per_item': 51,
    },
]

totals = compute_totals(orders)
print(totals)
# totals is [('order_001', 42), ('order_002', 120), ('order_003', 102)]
