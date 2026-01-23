#if-else statements are use to check if the condition is true or not ..
# First it will check the 'if' condition is true then is will do the operation which is inside the if and if it is false then it will do the operation which are in else.\

#Q1 - wap to find the greatest of four numbers entered by the user ...
num_1=int(input("enter the first number : "))
num_2=int(input("enter the second number : "))
num_3=int(input("enter the third number : "))
num_4=int(input("enter the fourth number : "))
if(num_1>num_2 and num_1>num_3 and num_1>num_4):
    print("the greatest number is ",num_1)
elif(num_2>num_1 and num_2>num_3 and num_2>num_4):
    print("the greatest number is ",num2)
elif(num_3>num_1 and num_3>num_2 and num_3>num_4):
    print("the greatest number is ",num_4)
elif(num_4>num_1 and num_4>num_2 and num_4>num_3):
    print("the greatest number is ",num_4)
else:
    print("you typed a invalid numbers ")


#Q2 - wap to find out whether a student is pass or fail,if it requires total 40%and at least in each subject to pass.assume 3 subjects to take the input from the user.
sub1=int(input("enter the marks of first subject : "))
sub2=int(input("enter the marks of second subject : "))
sub3=int(input("enter the marks of third subject : "))
if(sub1):
    if(sub1>33 or sub1>=40):
        print(" the student is passed in first subject.... ")
    else:
        print("the student is failed in first subject....")
if(sub2):
    if(sub2>33 or sub2>=40):
        print("the student is passed  in second subject....")
    else:
        print("the student is failed in second subject")
if(sub3):
    if(sub3>33 or sub3>=40):
        print("the student is passwd in third subject....")
    else:
        print("the student is failed in third subject....")


#Q3 - #A spam comment is defined as a text containing following keywords:  “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
#  to detect these spams. 
str=input("enter the sentence to detect that it is spam or not...")
if(str=="Make a lot of money"):
    print("spam comment detected")
elif(str=="buy now"):
    print("spam comment detected")
elif(str=="subscribe this"):
    print("spam comment detected")
elif(str=="click this"):
    print("spam comment detected")
else:
    print("this is not spam comment")



#Q4 - Write a program to find whether a given username contains less than 10 characters or not.
user_name=input("enter the username : ")
final_name=len(user_name)
if(final_name<10):
    print("yes, it is a valid username....")
else:
    print("it is against the conditions....")


#Q5 - Write a program to find whether a given username contains less than 10 characters or not.
l=["alex","andrew","alpha","aliana"]
name=input("enter the username...")
if(name in l):
    print("the name is present in list....")
else:
    print("name is not present in list....")


#Q6 - Write a program to calculate the grade of a student from his marks from the  following scheme:
mark=int(input("enter the marks of the student : "))
if(mark>90 and mark<=100):
    print("EX")
elif(mark>80 and mark<=90):
    print("A")
elif(mark>70 and mark<=80):
    print("B")
elif(mark>60 and mark<=70):
    print("C")
elif(mark>50 and mark<=60):
    print("D")
elif(mark>40 and mark<=50):
    print("F")
else:
    print("STUDENT FAILED....")


#Q7 - wap to find out whether a given post is talking about "Om" or not .
str=input("enter the post : ")
if("Om" in str):
    print("POST IS TALKING ABOUT THE OM....")
else:
    print("POST IS NOT TALKING ABOUT THE OM....")
