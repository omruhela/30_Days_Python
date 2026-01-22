#We can check the type of the data 

#Number
num=34
print(type(num))

#String
name="Omruhela"
print(type(name))

#float
decimal=23.34
print(type(decimal))

#Boolean
value=True
print(type(value))

#Q1 = wap to display a user entered name followed by good afternoon using input() function 
name=input("enter your name ")
print(f"good afternoon {name}")

#Q2 = Fill the information 
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Om").replace("<|Date|>","22 December 2025"))

#Q3 = Write a program to find that there is double space in a string or not 
name="Om is a good  boy"
print(name.find("  "))

# '\n' is used to give the statement a new line...
# '\t' is used to give tyhe indentation or "your spaces" to the word....