#While loop
# x = 1 
# while x <= 10:
#     print(x, end=' ')
# print()                  #1 1 1 1 1 1...
x = 1 
while x <= 10:
    print(x, end=' ')
    x += 2
print()                 #1 3 5 7 9
x = 1
while x <= 10:
    print(x, end=' ')
    x *= 2
print()                   #1 2 4 8
x = 10 
while x >= 0:          
    print(x, end=' ')
    x -= 2 
print()                 #10 8 6 4 2
x = 10 
while x > 0:           #no = 0, because // last value is 0
    print(x, end=' ')
    x //= 2 
print()                  #10 5 2 1

#else 
x = 1 
while x < 5:
    if x % 2 == 1:
        x += 1
        continue 
    print(x, end=' ')
    x += 1                 #2 4 Loop completed successfully
else:                           
    print('Loop completed successfully')
print()                  
x = 1 
while x < 5:
    if x == 4:
        break 
    print(x, end=' ')
    x += 1                      #1 2 3
else:                              
    print('Loop completed successfully')
print()

#nested loops
for x in range(1,4):
    for y in range(4,7):
        print((x,y), end=' ')
print('\n')                #(1, 4) (1, 5) (1, 6) (2, 4) (2, 5) (2, 6) (3, 4) (3, 5) (3, 6) 
for x in range(1,3):
    for y in range(3,5):
        for z in range(5,7):
            print((x,y,z), end=' ')  
            print()       #(1, 3, 5) (1, 3, 6) (1, 4, 5) (1, 4, 6) (2, 3, 5) (2, 3, 6) (2, 4, 5) (2, 4, 6)

#matrix 
matrix = [ [4,5,6], [1,2,3], [7,8,9]]
#print matrix row-wise
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end='')
print()                               #4 5 6 1 2 3 7 8 9
#print matrix col-wise
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        print(matrix[j][i], end=' ')
print()                               #4 1 7 5 2 8 6 3 9