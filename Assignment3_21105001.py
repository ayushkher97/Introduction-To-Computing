#Question1

print("Question1")
print()

user_inp=input("Enter your string:")
user_inp=user_inp.lower()
user_words=user_inp.split()

count_dic={}

if len(user_words)==1:
    user_words=user_inp
    
for word in user_words:
    if word in count_dic:
        count_dic[word]+=1
    else:
        count_dic.update({word:1})

if len(user_inp)==0:
    print("NO word or sentence found.")
else:
    print("Number of each word/character is:",count_dic)

#Question2

print("Question 2")
print()

date=int(input("Enter the date\n[1,31]\t\t:"))
month=int(input("Enter the month\n[1,12]\t\t:"))
year=int(input("Enter the year\n[1800,2025]\t:"))
print()

verify_1 = (month in (1,3,5,7,8,10,12) and (1 <= date <= 31))
verify_2 = (month in (4,6,9,11) and (1 <= date <= 30))
verify_3 = ((year % 4) == 0 and month == 2 and (1 <= date <= 29)) or ((year % 4) != 0 and month == 2 and (1 <= date <= 29))

if (verify_1 or verify_2 or verify_3) and (1800<=year<=2025):

  # calculating next date for months having 31 days.
    if month in(1,3,5,7,8,10):
        if date<31:
            date+=1
        else:
            date=1
            month+=1

  # calculating next date for months having 30 days.
    elif month in(4,6,9,11):
        if date<30:
             date+=1
        else:
             date=1
             month+=1

  # calculating next date for feburary month because it has only 28 days.
    elif month==2:

        # calculating next date in case of leap year.
          if year%4==0:
              if date<29:
                  date+=1
              else:
                  date=1
                  month+=1
          else:
              if date<28:
                  date+=1
              else:
                  date=1
                  month+=1

  # calculating next date for december.
    else:
        if date<31:
            date+=1
        else:
            date=1
            month=1
            year+=1
            
    print(f"Next Date Is: {date}/{month}/{year}")    
else:
    print("Invalid Date.\nPlease enter a valid date.")

#Question 3

print("Question 3")
print()

given_list= []
output_list= []

max_num=int(input(" Enter the total number of numbers that you are going to enter: "))
print()
for i in range(max_num):
    number=int(input(f" Enter the {i+1} number:"))
    given_list.append(number)
print()

for num in given_list:
    tuple=(num,num**2)
    output_list.append(tuple)

print("The Final Output List Is:",output_list)


# Question 4

print("Question 4")
print()

grade_points=int(input("Enter the grade points \n [4,10] \t\t :"))
print()

if 4<=grade_points<=10 :
    if grade_points==10:
        print("Your Grade is 'A+' and Outstanding Performance.")
    elif grade_points==9:
        print("Your Grade is 'A' and Excellent Performance.")
    elif grade_points==8:
        print("Your Grade is 'B+' and Very Good Performance.")
    elif grade_points==7:
        print("Your Grade is 'B' and Good Performance.")
    elif grade_points==6:
        print("Your Grade is 'C+' and Average Performance.")
    elif grade_points==5:
        print("Your Grade is 'C' and Below Average Performance.")
    else:
        print("Your Grade is 'D' and Poor Performance.")
else:
    print("Invalid Grade.")

# Question 5

print("Question 5")
print()

initial_string= "ABCDEFGHIJK"

length=len(initial_string)

for counters in range(int(length/2) + 1):
    print(" "*counters + initial_string)

    if length >= 2:
        initial_string=initial_string.rstrip(initial_string[-1])
        initial_string=initial_string.rstrip(initial_string[-1])
        length -= 2

# Question 6

print("Question 6")
print()

student_information= {}

while True:

    ask= input("Do you want to enter detials of student? \n\t\t(Y or N) \t\t: ")
    print()

    if ask=="Y":
        student_sid=int(input("Enter the student's SID:"))
        student_name=input("Enter the student's name: ")
        student_information.update({student_sid : student_name})
        print()

    elif ask=="N":

     break

    else:
        print("Invalid input.\nPlease enter valid input.(Y/N)")
        print()

# part a

print("Part a")
print()
print("Student detials are: ",student_information)
print()

# part b

print("Part b")
print()

student_sids=list(student_information.keys())
student_names=list(student_information.values())

sorted_names=sorted(student_names)

sorted_dict= {}

for name in sorted_names:
    for index in range(len(student_names)):
        if student_names[index]==name:
            sorted_dict.update({student_sids[index] : name})
        
print("Sorted dictionary using student's name is:", sorted_dict)
print()

# part c

print("Part c")
print()
print("Sorted dictionary using student's SID is: " , dict(sorted(student_information.items())))
print()

# part d

print("Part d")
print()

while True:

    search_sid = int(input("Enter the SID whose name you want to search: "))
    print()
    
    if search_sid in student_information.keys():
        print(f"Student's name is: {student_information[search_sid]}")
        
        break

    else:
        print("NO such SID present.")
        print()

# Question 7

print("Question 7")
print()

def fibonacci_sequence(n):
    if n <= 1:
       return n
    return(fibonacci_sequence(n-1) + fibonacci_sequence(n-2))

sum= 0
avg_counter= 0

while True:
    
    
    num_terms = int(input("Enter the the number of terms you want in the sequence: "))
    print()

    if num_terms <= 0:
        print("Plese enter a positive integer")
    else:
        print(f"Fibonacci sequence with {num_terms} terms:")

        for count in range(num_terms):
            num= fibonacci_sequence(count)
            sum += num
            avg_counter += 1
            print(num)
        
        print()
    break

avg_fibonacci_seq = sum/avg_counter
print("Average of fibonacci sequence is:",avg_fibonacci_seq)

# question 8

print("Question 8")

set_1 = {1,2,3,4,5}
set_2 = {2,4,6,8}
set_3 = {1,5,9,13,17}

# part a
print()
print("Part a")
print()
set_a = (set_1 | set_2) - (set_1 & set_2)
print("Set of all the elemets that are in Set 1 and Set 2 but not in both:",set_a)

# part b
print()
print("Part b")
print()
set_b = (set_1 | set_2 | set_3)- (set_1 & set_2 & set_3) - (set_1 & set_2) - (set_2 & set_3) - (set_3 & set_1)
print("Set of all the elements that are only in one of the three sets (Set1,Set2,Set3):",set_b)

# part c
print()
print("Part c")
print()
set_c = ((set_1 & set_2) | (set_2 & set_3) | (set_1 & set_3)) - (set_1 & set_2 & set_3)
print("Set of all the elements that are exactly in two of the sets (Set1, Set2 and Set3):",set_c)

# part d
print()
print("Part d")
print()
set_d = {1,2,3,4,5,6,7,8,9,10} - set_1
print("Set of all the integers in the range 1 to 10 that are not in set_1: ",set_d)

# part e
print()
print("Part e")
print()
set_e = {1,2,3,4,5,6,7,8,9,10} - set_1 - set_2 - set_3
print("The set having all integers less than equal to 10 except that are not in all the sets: ",set_e)
        
