# 2D List - a list of lists.
drinks=['coffee','tea','juice']
dinner=['rice','roti']
deserts=['ice cream','cake']

food=[drinks,dinner,deserts]
print(food)  #[['coffee', 'tea', 'juice'], ['rice', 'roti'], ['ice cream', 'cake']]

print(food[1][1])  #roti
# print(food[1][2])                   #IndexError: list index out of range
