

name = 'gift' #string variable
age = 17 # this is an integer
height = 6.1 # this is a decimal
is_online = True # booylean
# camelCase:  (e.g., firstName, calculateTotalAmount).
# PascalCase: (e.g., FirstName, CustomerRecord).
# snake_case:  (e.g., first_name, user_account_id).
# kebab-case:  (e.g., first-name, button-style).
# (MACRO_CASE):  (e.g., MAX_RETRIES, API_KEY). Used for global
# PRIMITIVE DATA_TYPES
name = "precious" #string variable
age = 20 # integer
height = 6.2 # float
is_online = True # boolean
# camelCase:  (e.g., firstName, calculateTotalAmount).
# PascalCase: (e.g., FirstName, CustomerRecord).
# snake_case:  (e.g., first_name, user_account_id).
# kebab-case:  (e.g., first-name, button-style).
# (MACRO_CASE):  (e.g., MAX_RETRIES, API_KEY). Used for global

# fundamental
# variable
# data types

# COMPLEX DATA_TYPE
user = {
    "name": "precious",
    "age": 20,
    "height": 6.2,
    "is_online": False
} # dictionaries (objects)


fruits = ["apple", "banana", "orange", "mango"]

# function
def great_user(person_name):
    return "hello " + person_name

# classes (oop - object oriented programming)
class person:
    def _init_(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

# syntax: a strict set of grammatical rules governing how code most be written
# control structures: logic blocks that dictate the code's execution flow
# functions: a block of reusable code, written to perform a single task

# principle of programming
# solid (single responsibility (SRP) open/close (DCP),liskov substitution (LSP), interface segregation principle(ISP), dependency inversion principle(DIP)
# KISS: (keep it simple and slow)
# DRY: (don't repeat yourself)
# YANGI (you aren't gonna need it)
# SOC (separation of concerns)
greetperson1 = great_user("moses")
greetperson2 = great_user("precious")
greetperson3 = great_user("gift")

print(greetperson1)
print(greetperson2)
print(greetperson3)