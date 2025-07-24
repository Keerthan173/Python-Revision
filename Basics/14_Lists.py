# list - used to store multiple items in a single variable.
# 1. []
# 2. Index is present for each item in a list.
# 3. Mutable - can update.

food=["pizza","rice","juice"]
print(food)  #['pizza', 'rice', 'juice']
print(food[0])  #pizza

food[0]="ragi"
print(food[0])  #ragi

for x in food:
    print(x)
# ragi
# rice
# juice

food.append("Ice Cream")
print(food)  #['ragi', 'rice', 'juice', 'Ice Cream']

food.remove("juice")
print(food)  #['ragi', 'rice', 'Ice Cream']
# food.remove("Chapathi")     #ValueError: list.remove(x): x not in list

food.pop()
print(food)  #['ragi', 'rice']

food.insert(1,"cake")
print(food)  #['ragi', 'cake', 'rice']

food.sort()
print(food)  #['cake', 'ragi', 'rice']

print(food.index("ragi"))  #1
# print(food.index("Chapathi"))           #ValueError: 'Chapathi' is not in list

food.clear()
print(food)  #[]



# Python lists are heterogeneous, meaning they can contain items of different data types.
mixed_list = [1, "apple", 3.14, True]
print(mixed_list)  # [1, 'apple', 3.14, True]