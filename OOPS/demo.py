# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

# class Student(Person):
#     def __init__(self, name, age, major):
#         super().__init__(name, age)
#         self.major = major
    
#     def introduce(self):
#         super().introduce()
#         print(f"I am majoring in {self.major}.")

# def main():
#     student = Student("Alice", 20, "Computer Science")
#     student.introduce()

# if __name__ == "__main__":
#     main()




# class Employee:
#     def __init__(self, name, title, hourly_pay,x):
#         self.name=name
#         self.title=title
#         self.hourly_pay=hourly_pay
#         self.hours_per_week=x
    
#     def getName(self):
#         return self.name
    
#     def getTitle(self):
#         return self.title
    
#     def payPerYear(self):
#         return self.hourly_pay*self.hours_per_week*52
# class Manager(Employee):
#     def __init__(self, name, title, salary, bonus, reports=None):
#         super().__init__(name, title,0,0)
#         self.salary=salary
#         self.bonus=bonus
#         self.reports=reports if reports else []
    
#     def payPerYear(self):
#         return self.salary+self.bonus
    
#     def getReports(self):
#         return self.reports

# def main():
#     employee=Employee("John", "Developer", 50,30)
#     manager=Manager("Alice", "Engineer", 120000, 15000, ["XYZ", "ABC"])
#     employees=[employee, manager]
    
#     for emp in employees:
#         print(f"Name: {emp.getName()}, Annual Pay: {emp.payPerYear()}")
#         if isinstance(emp, Manager):
#             print(f"Reports: {', '.join(emp.getReports())}")

# if __name__ == "__main__":
#     main()



# class BankAccount:
#     def __init__(self,account_number,initial_balance=0.0):
#         self.account_number=account_number
#         self.balance=initial_balance

#     def deposit(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#         else:
#             print("Insufficient balance.")

#     def get_balance(self):
#         return self.balance

# class SavingsAccount(BankAccount):
#     def __init__(self,account_number,initial_balance,interest_rate):
#         super().__init__(account_number,initial_balance)
#         self.interest_rate=interest_rate

#     def add_interest(self):
#         self.balance+=self.balance*self.interest_rate

# class CheckingAccount(BankAccount):
#     def __init__(self, account_number, initial_balance, transaction_fee):
#         super().__init__(account_number, initial_balance)
#         self.transaction_fee = transaction_fee

#     def withdraw(self, amount):
#         total_amount=amount+self.transaction_fee
#         if self.balance>=total_amount:
#             self.balance-=total_amount
#         else:
#             print("Insufficient balance.")
            
# def main():
#     savings=SavingsAccount("12345", 1000, 0.02)
#     savings.deposit(500)
#     savings.add_interest()
#     print(f"Balance:{savings.get_balance()}")
#     checking=CheckingAccount("67890",2000,2.50)
#     checking.withdraw(100)
#     print(f"Checking Account Balance:{checking.get_balance()}")

# if __name__ == "__main__":
#     main()


# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         print("Hello from B")

# class C(A):
#     def greet(self):
#         print("Hello from C")

# class D(B,C):
#     pass

# def main():
#     d=D()
#     d.greet()
    
# if __name__=="__main__":
#     main()



# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
    
#     def area(self):
#         return self.width*self.height
    
#     def perimeter(self):
#         return 2*(self.width+self.height)

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
    
#     def area(self):
#         return 3.1416*self.radius**2
    
#     def perimeter(self):
#         return 2*3.1416*self.radius

# def main():
#     shapes=[Rectangle(3,4),Circle(5)]
#     for shape in shapes:
#         print(f"{shape.__class__.__name__}: Area = {shape.area()}, Perimeter = {shape.perimeter()}")

# if __name__ == "__main__":
#     main()



# from abc import ABC,abstractmethod
# class Flyer(ABC):
#     @abstractmethod
#     def fly(self):
#         pass

# class Swimmer(ABC):
#     @abstractmethod
#     def swim(self):
#         pass

# class Duck(Flyer,Swimmer):
#     def fly(self):
#         print("Flying with wings.")
    
#     def swim(self):
#         print("Swimming with webbed feet.")

# def main():
#     duck=Duck()
#     duck.fly()
#     duck.swim()

# if __name__=="__main__":
#     main()
    
    
# Mini-Project
from abc import ABC, abstractmethod
import random


class Animals(ABC):
    def __init__(self,name,health_level,hunger,habitat_type,):
        self._name = name
        self._health = health_level
        self._hunger = hunger
        self._habitat_type = habitat_type

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food_amount):
        pass

    def get_health(self):
        return self._health

    def get_hunger(self):
        return self._hunger

    def get_habitat_type(self):
        return self._habitat_type

    def decrease_health(self, amount):
        self._health = max(self._health - amount, 0)

    def decrease_hunger(self, amount):
        self._hunger = max(self._hunger - amount, 0)

    def increase_health(self, amount):
        self._health = min(self._health + amount, 100)

    def increase_hunger(self, amount):
        self._hunger = min(self._hunger + amount, 100)


class Lion(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Roar!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 2)
        self.increase_health(food_amount * 0.5)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")


class Elephant(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Trumpet!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 1.5)
        self.increase_health(food_amount * 0.3)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")


class Parrot(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Squawk!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 0.5)
        self.increase_health(food_amount * 0.2)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")


class Habitat(ABC):
    def __init__(self, type, condition, animals=None):
        self._type = type
        self._condition = condition
        self._animals = animals if animals is not None else []

    @abstractmethod
    def affect_animal(self, animal):
        pass

    def add_animal(self, animal: Animals):
        if animal.get_habitat_type() == self._type:
            self._animals.append(animal)
        else:
            print(f"{animal._name} doesn't belong to {self._type}")

    def get_condition(self):
        return self._condition

    def degrade(self, amount):
        self._condition = max(self._condition - amount, 0)


class Savanna(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__("Savanna", condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 50:
            animal.increase_health(5)
        else:
            animal.decrease_health(5)


class Jungle(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__("Jungle", condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 60:
            animal.increase_health(3)
        else:
            animal.decrease_health(3)


class Aviary(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__("Aviary", condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 70:
            animal.increase_health(2)
        else:
            animal.decrease_health(2)


class Staff(ABC):
    def __init__(self, name, energy):
        self._name = name
        self._energy = energy

    @abstractmethod
    def perform_task(self, target):
        pass

    def get_energy(self):
        return self._energy

    def use_energy(self, amount):
        self._energy = max(self._energy - amount, 0)


class Caretaker(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Habitat):
            target._condition = min(100, target._condition + 20)
            self.use_energy(10)
        else:
            print("Caretaker can only maintain habitats.")


class Veterinarian(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Animals):
            target.increase_health(15)
            self.use_energy(15)
        else:
            print("Veterinarian can only treat animals.")


class Sanctuary:
    def __init__(self, animals=None, habitats=None, staff=None):
        self.animals = animals if animals is not None else []
        self.habitats = habitats if habitats is not None else []
        self.staff = staff if staff is not None else []

    def add_animal(self, animal: Animals, habitat: Habitat):
        if animal.get_habitat_type() == habitat._type:
            self.animals.append(animal)

    def add_habitat(self, habitat):
        self.habitats.append(habitat)

    def add_staff(self, staff):
        self.staff.append(staff)

    def simulate_day(self):
        for animal in self.animals:
            animal.make_sound()
            animal.increase_hunger(10)

        for habitat in self.habitats:
            habitat.degrade(10)

        print()
        print()

        for person in self.staff:
            if isinstance(person, Caretaker):
                habitat = random.choice(self.habitats)
                person.perform_task(habitat)
                print(f"Caretaker maintaining {type(habitat).__name__}")
            elif isinstance(person, Veterinarian):
                animal = random.choice(self.animals)
                if animal.get_health() < 50:
                    person.perform_task(animal)
                    print(
                        f"Veterinarian treating {type(animal).__name__} (health < 50)"
                    )

        print()
        print()

        for animal in self.animals:
            if animal.get_hunger() > 50:
                animal.feed(20)

        print()
        print()

        print("Animal Status: ")
        for animal in self.animals:
            print(
                f"{type(animal).__name__} ({animal.get_habitat_type()}): Health {animal.get_health()}, Hunger {animal.get_hunger()}"
            )

        print()
        print()

        print("Habitat Status: ")
        for habitat in self.habitats:
            print(f"{type(habitat).__name__}: Condition {habitat.get_condition()}")


def main():
    animals = [
        Lion("Leo", 10, 20, "Savanna"),
        Elephant("Mirchi", 90, 20, "Jungle"),
        Parrot("Chichi", 70, 45, "Aviary"),
    ]
    habitats = [
        Savanna(50),
        Jungle(75),
        Aviary(100),
    ]
    staff = [Caretaker("Shek", 50), Veterinarian("Harry", 85)]

    sanctuary = Sanctuary(animals, habitats, staff)
    # Add animals to their habitats
    for animal in animals:
        for habitat in habitats:
            if animal.get_habitat_type() == habitat._type:
                habitat.add_animal(animal)
    
    print("--- Day 1 ---")
    sanctuary.simulate_day()


if __name__ == "__main__":
    main()