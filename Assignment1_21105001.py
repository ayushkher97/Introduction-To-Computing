#Question 1

print("First Question")
num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
num3=float(input("Enter your third number:"))
avg=(num1+num2+num3)/3
print("The average of the three numbers is:",avg)
print()

#Question 2

print("Second Question")
grossincome=float(input("What is your gross income?"))
numberofdependants=int(input("What is the number of dependants?"))
standarddeduction=10000
additionaldeduction=3000
taxableincome=grossincome-(standarddeduction)-(numberofdependants*additionaldeduction)
if taxableincome<0:
    print("The Taxable Income Is:0")
else:
 print("The Taxable Income Is:",taxableincome)
tax=(20/100)*taxableincome
if tax<0:
 print("No tax to be paid")
else:        
 print("The Total Amount Of Tax Is:",tax)
print()

#Question 3

print("Third Question")
print("List of the students") 
sid=int(input("Enter the SID:"))
name=input("Enter the name:")
gender=input("Enter the gender.\n(M,F,U)         :")
coursename=input("Enter the course name.\n(CSE,ECE,EE,ME,,CE,AERO,META):")
cgpa=float(input("Enter the CGPA:"))
print("[SID,NAME,GENDER,COURSENAME,CGPA]")
student=[sid,name,gender,coursename,cgpa] 
print("List Of The Student Is:")
print(student)
print()

#Question 4

print("Fourth Question")
m1=float(input("Enter the marks of the first student:"))
m2=float(input("Enter the marks of the second student:"))
m3=float(input("Enter the marks of the third student:"))
m4=float(input("Enter the marks of the fourth student:"))
m5=float(input("Enter the marks of the fifth student:"))
marks=[m1,m2,m3,m4,m5]
print("List of the student's marks:",marks)
marks.sort()
print("List of the student's marks (sorted):",marks)
print()

#Question5

print("Fifth Question")
color=['Red','Green','White','Black','Pink','Yellow']
color1=['Red','Green','White','Black','Pink','Yellow']
print("Original list of the color is:",color1)
color1.pop(3)
print("List of the colors after removing black color is:",color1)
color[3:5]=["Purple"]
print("List of the colors after replacing black and pink by purple",color)


