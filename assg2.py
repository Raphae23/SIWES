#fizzbuzz interview
Q1 = int(input("Enter num: "))

for Q1 in range(1,10):
    if(Q1 % 2 == 0):
        print('Fizz')
    elif(Q1 % 5 == 0):
        print('Buzz')
    elif(Q1 % 10 == 0):
        print('FizzBuzz')
    else:
        print(Q1)
    
