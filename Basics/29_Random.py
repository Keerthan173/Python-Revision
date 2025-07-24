import random

# Random integer between 1 and 6
x = random.randint(1, 6)
print(x)


# Random float between 0 and 1
y = random.random()
print(f"{y:.2f}") # 0.85/0.99/0.12

# Random choice from a list
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)  # rock/paper/scissors


# Shuffle a list
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
random.shuffle(cards)
print(cards)
# ['10', 'King', '5', '4', 'Jack', '8', 'Queen', 'Ace', '3', '9', '7', '2', '6']
# ['8', 'King', '4', 'Ace', 'Jack', '10', '3', '6', '9', 'Queen', '7', '2', '5']