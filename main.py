import random
import math
from typing_extensions import LiteralString

# random_num = random.randint(1, 10)
# print(random_num)

# random_float = random.random()

# x = math.floor(random_float * 10 +1)
# print(x)

# random_number = random.randint(0, 1)
# print(random_number)
# result = "Head" if random_number == 1 else "Tail"
# print(result)

# ********************
# Lists....

names = str(input("Please tell the names\n"))
names_split = names.split(", ")

random_person = random.randint(1, len(names_split)-1)
print(random_person)
print(f"{names_split[random_person]} is going to buy the meal today!")


