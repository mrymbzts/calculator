#we use '#' for comments
#this sign dosen't affect the code

#%%

#now let's try to print a string
print("hello world!")

#assume that we want to separate the text to lines
#for that we can use '\n'. let's look at the example
print("hi i'm elif\nit's my first year in industrial engineering\nistudy in Istanbul")
#(we should take care to use English characters while writing the code. Otherwise an error code may be received)

#we print a string 5 times
print(5 * "hello")
#use the previous feature for separating the lines
print(5 * "hello\n")

#now let's try to learn the type of values. we'll use the type() function
print(type(True))#it shows that 'True' is a boolean value
#we can use the console directly to learn the type of values

#%%

#now lets learn how to use the print function in a versatile way
#we can take more than one output in one step. 
#to print spaces: ',' or without spaces: '+'
a = 3 
b = "three"
c = "idiots"
print(a, c) #there is a space between the two variables
#print(a + c): there is no possibility to add a string and an integer.so we get a TypeError with this code
#instead of using the variable a, we can use the variable b for adding
print(b + c) #there is no space between the two variables
print(str(a) + c) #in this code, we turned the 'variable a' into a string with the str() function.
#now it doesn't give a TypeError ;)

#%% 

#assigment two variables
#and then change their values without any assignment
#at last, print the new values of the variables for checking the code
a = 19
b = 23
print("first value of a:",a)
print("first value  of b:",b)
a,b = b,a
print("new value of a", a)
print("new value of b", b)
#or: 
x = 2
y = 3
print(f"first value of x: {x} and first value of y: {y}")
z = x #in here, z value takes the value of x and becomes 2
x = y #x value takes the value of y and becomes 3
y = z #y value takes the value of z and becomes 2
print(f"new value of x: {x} and new value of y: {y}")

#in another option, we used the f-string method to get our output.

#%%

#slicing(indeksing)
#slicing in string is like: [initial index:end index:number of steps] 
s = "aeiou"
print(s[0:4:2])#starting from the first character (0. index) to the 4th character (4. index and it's not included) with skip 2 steps
print(s[0])#0. index means the first character 
print(s[::-1])# it prints the variable in reverse order
print(s[-3])#it prints the 3rd character from the end
print(s[:]) #it prints the whole string
#print(s[0:len(s):1]) is a complex version of the previous code
#lets make a little bit more complex: print(s[0:len(s)]) 

#%%

#input() function always returns str. 
#so if u wanna do an operation on int, you should change the type of value to integer with int() function
#now get a number from the user and multiply it by 9
a = int(input("please enter a number: "))
b = a * 9
print("the result is: ", b)

#%%

#comparison operators 
# ==, != (not equals), >, <, >=, <= 
#logical operators
# and, or, not
first = float(input("please enter a number: ")) #we get a number from the user and turn it into a float
second = float(input("please enter another number: "))
if first == second: #if first number is equal to second number
    print("first number and second number are equal") # print this
elif first > second: # if first number is greater than second number
    print("first number is greater than second number") 
else: # it's the last option: meaning that first number is less than second number
    print("first number is less than second number")

#%%

#len() function: helps us to find the length of variables
#it can be used for strings, lists, tuples, dictionaries
university = "Istanbul Technical University"
char = len(university)
print("the length of the string is: ", char) #it counts spaces as well

#%%

