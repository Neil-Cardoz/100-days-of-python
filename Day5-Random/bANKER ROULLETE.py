import random

name="Angela, Ben, Jenny, Michael, Chloe"
list=name.split(",")
print(list)
a=random.choice(list)
print(f"you love {a}")