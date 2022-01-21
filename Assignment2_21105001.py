#Question1

print("SOLUTION-1")
print()
input_str="Python is a case sensitive language"
print("(a)The Length of the given string is:",len(input_str))
rev_str=input_str[::-1]
print("(b)The string in the reverse order is:",rev_str)
new_str=input_str[10:26]
print("(c)The new string becomes:",new_str)
sec_input_str=input_str.replace("a case sensitive","object oriented")
print("(d)The input string after replacing:",sec_input_str)
ind=input_str.index("a")
print("(e)The index of the substring 'a' is:",ind)
rem=input_str.replace(" ","")
print("(f)The input string after removing the white spaces is:",rem)

#Question2

print("SOLUTION-2")
print()
name=input("Enter your name:")
sid=int(input("Enter your SID:"))
dep_name=input("Enter the name of your department:")
cgpa=float(input("Enter your CGPA:"))
print("Hey,%s Here! \n My SID is %d \n I am from %s department and my cgpa is %f."%(name,sid,dep_name,cgpa))

#Question 3

print("SOLUTION-3")
print()
a=56
b=10
print("(a) a&b=%d"%(a&b))
print("(b) a|b=%d"%(a|b))
print("(c) a^b=%d"%(a^b))
print("(d) Left shift both a and b with 2 bits: a=%d,b=%d"%(a<<2,b<<2))
print("(e) Right shifth awith 2 bits and b with 4 bits: a=%d,b=%d"%(a>>2,b>>4))

#Question 4

print("SOLUTION-4")
print()
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if (a>=b) and (a>=c):
    print("The greatest number is: %s"%a)
elif (b>=a) and (b>=c):
    print("The greatest number is: %s"%b)
else:
    print("The greatest number is: %s"%c)

#Question 5

print("SOLUTION-5")
print()
string=str(input("Enter the string:"))
if "name" in string:
    print("Yes")
else:
    print("No")

#Question 6

print("SOLUTION-6")
print()
a=int(input("Enter the length of first side of the triangle:"))
b=int(input("Enter the length of second side of the triangle:"))
c=int(input("Enter the length of third side of the triangle:"))
if a<b+c and b<a+c and c<a+b:
    print("Yes")
else:
    print("No")
