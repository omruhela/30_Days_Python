
# for and while loop ... which repeats the condition which has been passed inside the loop. 


#Q1 - Write a program to print multiplication table of a given number using for loop.
n=int(input("enter the number to get the multiplication table of : "))
for i in range(1,11):
    print(n," X " , i, " = ",n*i)


#Q2 - Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if(i.startswith("S")):
        print("HELLO ",i)


#Q3 - Attempt problem 1 using while loop. 
n=int(input("enter the number you want the multiplication table of : "))
i=1
while(i<11):
    print( n, " X ", i," = ",n*i)
    i+=1


#Q4 - Write a program to find whether a given number is prime or not.
n=int(input("enter the number : "))
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("number is prime")


#Q5 - Write a program to find the sum of first n natural numbers using while loop.
num=int(input("enter the number : "))
i=1
sum=0
while(i<=num):
    sum+=i
    i+=1
print(sum)


#Q6 - Write a program to calculate the factorial of a given number using for loop. 
num=int(input("enter the number : "))
fact=1
for i in range(1,num+1):
    fact = fact*i
print(fact)


#Q7 - #  print the pattern
#    *
#   ***
#  ***** n=3
n=int(input("enter the number : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")


#Q8 - Write a program to print the following star pattern: 
# * 
# ** 
# ***   for n = 3

n=int(input("enter the number : "))
for i in range(1,n+1):
    print("*"*i)



#Q9 - Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 
n=int(input("enter the numeber : "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")


#Q10 - Write a program to print multiplication table of n using for loops in reversed 
# order.
n=int(input("enter the number you want the multiplication table of : "))
for i in range(1,11):
    print(n," X ", 11-i, " = ", n*(11-i))