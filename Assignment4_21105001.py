# Question 01

print("Question 1")
print()

def tower_of_honie(number_of_dics,a,b,c):
    if number_of_dics > 0:
        tower_of_honie(number_of_dics -1, a, c, b)
        print(f"Move disc {number_of_dics} from {a} to {c}")
        tower_of_honie(number_of_dics -1, b,a,c)

number_of_dics = 3  
tower_of_honie(3, "a", 'b', 'c')
print()


# Question 2

print("Question 2")
print()

print("Using recurrsion. \n")


def pascel_triangle(n,list1):
    if n == 0 :
        return
    
    pascel_triangle(n-1,list1)

    l = len(list1)
    list2 = list1.copy()             
    list1.append(1)

    for counter in range(0,l):
        if counter == 0:
            list1[0] = 1
        else:
            list1[counter] = list2[counter] + list2[counter-1]
    
    proper_pattern(list1)   

def proper_pattern(list1):
    print(" "*(number - len(list1)), end = "")

    for item in list1:
        print(item , end = " ")
    print()
    
number = int(input("Enter the number(natural number) of lines to print: "))
print()

initial_list = []
pascel_triangle(number,initial_list)


# Using iteration.

print()
print("Using iteration.\n")

output_list = []

for counter in range(number):
    if len(output_list) == 0:
        temp_list = []
    else:
        temp_list = output_list[counter - 1].copy()

    temp_list.append(1)
    
    if counter > 1:
        for j in range(1,len(output_list[counter - 1])):
            temp_list[j] = output_list[counter - 1][j] + output_list[counter - 1][j - 1]

    output_list.append(temp_list)

for lst in output_list:
    proper_pattern(lst)



# Question 3

print()
print("Question 3")
print()

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter second number(number must not be zero): "))
print()

quotient_reminder = divmod(num_1, num_2)
print(f"The quotient and reminder of the values are: {quotient_reminder}")

print()
print("Part A\n")

check = callable(quotient_reminder)
if check == True:
    print("It is callable.")
elif check == False:
    print("It is not callable.")

print()
print("Part B \n")

if quotient_reminder == (0,0):
    print("Both values are zero.")
elif quotient_reminder[0] == 0:
    print("Only quotient is zero")
elif quotient_reminder[1] == 0:
    print("Only reminder is zero.")
else:
    print("Both are non zero.")

print()
print("Part C \n")

new_set = quotient_reminder.__add__((4,5,6))
print(f"New set after adding the values is: {new_set}\n")

greater_than_4 = []
for counter in range(len(new_set)):
    if new_set[counter] > 4:
        greater_than_4.append(new_set[counter])
print(f"Numbers greater than 4 are: {greater_than_4}")
print()

print("Part D \n")

converting_to_set = set(greater_than_4)
print(f"Converting the list into set {converting_to_set} \n")


print("Part E \n")

converting_to_immutable = frozenset(converting_to_set)
print("Set is not immutable")

print()
print("Part F \n")

print(f"Max value in the set is {max(converting_to_immutable)}")
print(f"Hash value is: {hash(converting_to_immutable)}")

# Question 4.

print()
print("Question 4 \n")

class Student():

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print(f"Object created for {self.name}")

    def show_info(self):
        print(f'The name of the student is {self.name}')
        print(f'The roll number of {self.name} is {self.rollno}')

    def __del__(self):
        print(f"Destructor deleted {self.name}'s record.")

student_1 = Student("Ayush Kher", 21105001)
student_2 = Student("Armeen Singh", 21105002)
student_3 = Student("Harman Singh", 21105003)
print()

student_1.show_info()
print("\n")
student_2.show_info()
print("\n")
student_3.show_info()
print('\n')

del student_1
del student_2
del student_3

# Question 5

print()
print("Question 5 \n")

class factory():

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")

    def show_info(self):
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    def update_salary(self,new_salary):
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    def __del__(self):
        print(f"Record of the employee {self.name} is deleted.")
    
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()

Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()

print("Updating mehak's salary.")
Mehak.update_salary(70000)

print("Calling destructor to delete viren's record.")
del Viren

# Question 6

print()
print("Question 6 \n")

utter_word = input("First friend, Please enter any word: ")
print()
new_word = input("Second friend, Please enter a new word to test your friendship: ")
print()

count_list_uttered_word = [0]*26
count_list_new_word = [0]*26

for letter in utter_word:
    count_list_uttered_word[ord(letter.lower()) - ord('a')] += 1

for letter in new_word:
    count_list_new_word[ord(letter.lower()) - ord('a')] += 1

if count_list_uttered_word == count_list_new_word:

    while True:

        check = input("Please enter whether the new word have meaning or not(Y or N): ")
        print()
        if check == "Y":
            print("Congratulations! You and your friend has passed the friendship test.")
            break
        elif check == "N":
            print("Oops! You and your friend failed the friendship test")
            break
        else:
            print("Please enter a valid input.(Y or N)")

else:
    print("Oops! You and your friend failed the friendship test")
