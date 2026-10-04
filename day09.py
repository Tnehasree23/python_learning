# 1. Function with return

def add(a, b):
    print("add function")    #add function
    c = a + b
    return c
    
def sub(a, b):
    print("sub function")    #sub function
    c = a - b
    return c

def div(a, b):
    print("div function")    #div function
    c = a / b
    return c
x = add(10, 15)
y = sub(20, 10)
z = div(25, 10)
print(x)                # 25
print(y)                # 10
print(z)                # 2.5
print()

# 2. Types of Arguments

def detail(name, age, rollno):
    print(f"My name is {name}")               # My name is neha
    print(f"My age is {age}")                 # My age is 20
    print(f"My rollno is {rollno}")           # My rollno is A101
detail("neha", 20, "A101")
detail(age=20, rollno="A101", name="neha")
detail(rollno="A101", age=20, name="neha")

# 3. Default Arguments

def add_numbers(a, b=10, c=20):
    return a + b + c
print(add_numbers(1))                   # 31
print(add_numbers(1, 2))                # 23
print(add_numbers(1, 2, 3))             # 6
print(add_numbers(c=3, a=1, b=2))       # 6

# 4. Order of Arguments

def sub_numbers(a, b, c=10):
    return a - b - c
print(sub_numbers(20, 5))           #5
print(sub_numbers(20, 5, 2))        #13

# 5. Order in Function Call

print(add_numbers(10, b=20, c=30))    #25

# 6. Variable Length Arguments

def f1(*a):
    print(a)
    print(type(a))    # (1, 2, 3, 4)
                      # <class 'tuple'>
f1(1, 2, 3, 4)

# 7. Variable Length Keyword Arguments

def f2(**a):
    print(a)             
    print(type(a))         # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
f2(a=1, b=2, c=3, d=4)     # <class 'dict'>
                           
                           
