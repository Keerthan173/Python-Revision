# tuple - collection which is ordered and immutable.
# ()

student1=("Bro",21,"male")
print(student1.count(21))  #1
print(student1.index("male"))  #2

for x in student1:
    print(x,end=" ")
# Bro 21 male

if "Bro" in student1:
    print("Bro is male")