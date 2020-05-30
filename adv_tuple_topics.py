# adv_tuple_topics
#   more tuple topics needed for programming labs
#   shows use of multiple data types in a tuple(str,int)
#   also shows comparison of values


#1 adding multiple variable types to a tuple
#   (can use for or while loop, shown with for here) 

# initialize variables
s_name = ""
s_grade = 0
s_tuple = ()
fail_tuple = ()
s_len_max = 0
s_grade_max = 0
long_name = ""
num_fail = 0
# CONSTANT: a variable that contains an unchanging value (capitalized)
VOWELS = "aeiou"
vowel_count = 0

for i in range(4):
    s_name = input("\nWhat is the student's name? ")
    s_grade = int(input("What is their grade? 0-100: "))
    
    s_tuple +=((s_name, s_grade),)

    print(s_tuple)
    
#2 finding number of vowels in name
    vowel_count = 0
    for i in s_name:
        if i in VOWELS:
            vowel_count += 1
    print("\nThere are", vowel_count, "vowel(s) in" , s_name)

#3 comparing len of student names to find the longest name
    if len(s_name) > s_len_max:
        s_len_max = len(s_name)
        long_name = s_name
    print ("\nThe longest name is: ", long_name,
           "and it is" , s_len_max , "letters long.")

#4 comparing student scores to find highest score
    if s_grade > s_grade_max:
        s_grade_max = s_grade
    print ("The highest grade is: ", s_grade_max)

print("\nThis is the s_tuple in tuple format: ", s_tuple)

#5 looping through tuple to find students who are failing
input("\nPress enter to find failing students: ")
for i in s_tuple:
    if i[1] < 60:
        num_fail += 1
        fail_tuple += (i[0],)

print("\nThe number of students who are failing is: ", num_fail)
print("The failing students are:")
for i in fail_tuple:
    print(i)

input("\nPress enter to exit.")
        
