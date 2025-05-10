rows=int(input("How many rows?"))
cols=int(input("How many columns?"))
symbol=input("Enter a symbol to use:")

for i in range(rows):
    for j in range(cols):
        print(symbol,end="")            #end="",prevents new line.
    print()

#Output:
# How many rows?3
# How many columns?4
# Enter a symbol to use:$
# $$$$
# $$$$
# $$$$