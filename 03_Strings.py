name="Bro Code"
print(len(name))            #8
print(name.find("B"))           #0
print(name.find("b"))           #-1
print(name.upper())         #BRO CODE
print(name.split(" "))          #['Bro', 'Code']
print(name.count("o"))          #2
print(name.replace("o","abc"))          #Brabc Cabcde
print(name.isalnum())           #False
print(name.isdigit())           #False


y="BroCode"
print(y.isalnum())          #True

x="123"
print(x.isdigit())          #True

