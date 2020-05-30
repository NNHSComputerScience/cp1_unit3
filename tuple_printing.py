# tuple_printing.py
# Printing multiple tuples in columns

#initialize variables
names = ()
ages = ()
grades = ()
again = "y"

#while loop to gather student info
while again == "y":
    name = input("What is the student's name?")
    age = input("What is the student's age?")
    grade = int(input("What is the student's grade?"))
    names += (name,)
    ages += (age,)
    grades += (grade,)

    again = input("Enter another student? (y or n)").lower()

# printing student info in columns
print("Names\t\tAges\t\tGrades")
for i in range(len(names)):
    print(names[i],"\t\t", ages[i] , "\t\t" , grades[i])
    

input("Press enter to exit.")





