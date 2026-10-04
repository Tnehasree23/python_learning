#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)                          ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#create same list with comprehension
a = [x for x in range(1, 11)]
print(a)                           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)                        ##[2, 4, 6, 8, 10]

#create same list with comprehension
a = [x for x in range(1, 11) if x % 2 == 0]
print(a)                       #[2, 4, 6, 8, 10]

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)

#create same list with comprehension
a = [(x, y) for x in range(1, 5) if x % 2 == 0
            for y in range(1, 4) if x + y == 0]
print(a)                          #[(2, 3), (4, 1)]

#set comprehension
l = [3,4,3,5,6,7,6]        #[]
#create list, set, dict comrehension with above list

#List comprehension
a = [x for x in l]
print(a)     #[3, 4, 3, 5, 6, 7, 6]

# set comprehension
b = {x for x in l}
print(b)     #{3, 4, 5, 6, 7}

#Dictionary comprehension
c = {x: x*x for x in l}
print(c)      #{3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

#function
def numbers():
    return 1 
    return 2 
n = numbers()
print(n)         #1
print(type(n))   #<class 'int'>

#generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)              # 1 2 3 4
print(type(n))
print(next(n))
print(next(n))
print(n.__next__())
print(n.__next__())
print(next(n))            #StopIteration

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))
print(n.__next__())
for x in n:
    print(x)                # 2 4 6 8

#write generator to generate odd numbers

def odd_numbers(n):
    for i in range(1, n + 1, 2):
        yield i


for num in odd_numbers(20):
    print(num)                      # 1 3 5 7 9 11 13 15 17 19

#write generator to generate even numbers

def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i


for num in even_numbers(20):
    print(num)                    # 2 4 6 8 10 12 14 16 18 20

#write generator to generate prime numbers

def prime_numbers(n):
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


for num in prime_numbers(20):
    print(num)                      # 2 3 5 7 11 13 17 19
