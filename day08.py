# #FOR LOOP PROBLEMS
# #important problems

#1. print numbers from 1 to 10 in one line
for n in range(1, 11):
    print(n, end=' ')
print()    #1 2 3 4 5 6 7 8 9 10


# #2. print even numbers from 5 to 30 in one line
for n in range(5, 31):
     if n % 2 == 0:
         print(n, end=' ')
print()   #6 8 10 12 14 16 18 20 22 24 26 28 30


 #3. print odd numbers from 5 to 30 in one line
for n in range(5, 31):
     if n % 2 != 0:
       print(n, end=' ')
print()    #5 7 9 11 13 15 17 19 21 23 25 27 29


#4. print numbers divisible by 5 from 1 to 30 in one line
for n in range(1, 31):
    if n % 5 == 0:
        print(n, end=' ')
print()   #5 10 15 20 25 30


#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for n in range(1, 101):
    if n % 5 == 0 and n % 7 == 0:
        print(n, end=' ')
print() #35 70


# #6. sum of numbers from 10 to 25 
sum = 0 
for n in range(10, 26):
    sum += n 
print(f'Sum of numbers from 10 and 25 is {sum}')   #Sum of numbers from 10 to 25 is 280


#7. sum of numbers in list [4,3,2,5,6,7] 
numbers = [4, 3, 2, 5, 6, 7]

total = 0

for n in numbers:
    total += n

print('Sum is', total)  #Sum is 27


 #8. multiplication table of a number 
n = int(input('Enter a number: '))

for i in range(1, 11):
    print(n, 'x', i, '=', n * i) #5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50


 #9. factorial 
n = int(input('Enter a number: '))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print('Factorial is', factorial) #Enter a number: 5  #Factorial is 120


#10. fibonacci 
a = 0
b = 1 
n = 10 
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b 
print()   #0 1 1 2 3 5 8 13 21 34

#11. reverse a string
        # 012345
string = 'neha'
rev = ''
for i in range(len(string)-1, -1, -1):
    rev = rev + string[i]
print(f'Revers of {string} is {rev}')   #Reverse of neha is ahen


#12. count vowels in a string
string = input('Enter a string: ')

count = 0

for ch in string:
    if ch in 'aeiouAEIOU':
        count += 1

print('Number of vowels:', count) #neha = Number of vowels: 2

#13. count z's and y's in a string
string = input('Enter a string: ')

z_count = 0
y_count = 0

for ch in string:
    if ch == 'z':
        z_count += 1
    elif ch == 'y':
        y_count += 1

print('Number of z:', z_count) #Enter a string: 7 #Number of z: 0
print('Number of y:', y_count)   #Number of y: 0


#14. check whether a number is prime number or not 
n = int(input('Enter a number: '))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print('Prime number')
else:
    print('Not a prime number')  #Enter a number: 7   #Prime number







#WHILE LOOP PROBLEMS


#1.print 1 to 10 with while loop
x = 1
while x <= 10:
    print(x, end=' ')
    x += 1   #1 2 3 4 5 6 7 8 9 10


#2.print even numbers from 1 to 10
x = 1
while x <= 10:
    if x % 2 == 0:
        print(x, end=' ')
    x += 1  #2 4 6 8 10


#3.print numbers divisible by both 5 and 7 from 1 to 500 
x = 1
while x <= 500:
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')
    x += 1   #35 70 105 140 175 210 245 280 315 350 385 420 455 490


#4.count digits
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)  #Enter a number: 12345  #Number of digits: 5


#5.reverse a number
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reverse:", reverse) #Enter a number: 12345  #Reverse: 54321

#6.palindrome number 
n = int(input("Enter a number: "))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")  #Enter a number: 121  #Palindrome number


#7.palindrome string without slicing, without built in function
s = input("Enter a string: ")
i = 0
j = len(s) - 1
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("Palindrome string")
else:
    print("Not a palindrome string")  #Enter a string: neha #Not a palindrome string

#8.armstrong number
n = int(input("Enter a number: "))
original = n
digits = 0
temp = n
while temp > 0:
    temp = temp // 10
    digits += 1
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10
if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")  #Enter a number: 153  #Armstrong number
