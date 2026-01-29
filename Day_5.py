#functions are the user defined operations 


#Q1 - Write a program using functions to find greatest of three numbers.
a=int(input("enter the first number "))
b=int(input("enter the second number : "))
c=int(input("enter the third number : "))
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
print(greatest(a,b,c))


#Q2 - Write a python program using function to convert  fahrenhit to celcius.
f=int(input("enter the tempercature in f: "))
def convert(f):
     return 5*(f-32)/9

print(round(convert(f),2))


#Q3 - ow do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c", end="")
print("d", end="")


#Q4 - Write a recursive function to calculate the sum of first n natural numbers. 
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(5))


#Q5 - 
# *** 
# **               
# * - for n = 3
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
print(pattern(5))


#Q6 - Write a python function which converts inches to cms.
def inch_to_cm(inch):
    return inch*2.54
n=int(input("enter the value in inches: "))
print("the corresponding value in cm is ",inch_to_cm(n))


#Q7 - Write a python function to remove a given word from a list ad strip it at the same time.
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["harry","rohan","shubham","an"]
print(rem(l,"an"))


#Q8 - Write a python function to print multiplication table of a given number. 
def multiply(n):
    for i in range(1,n+1):
        print(n," X ", i, " = ",n*i)

multiply(5)