# Course info program
# Written by Wesley Greer on 3/19/2026

# Write a program that has the user input a bunch of course ID and course name pairs.
course_list = {}
print("This program allows you to enter multiple course ID's and names, which you can then search through using the course ID.")
print('(e.g course ID = COS 2005, course name = Python Programming)')
more_courses = True
while more_courses == True:
    course_id = input("Enter the course ID: ")
    course_name = input("Enter the course name: ")
    course_list[course_id] = course_name
    q = input('Would you like to enter another course? (y/n): ').lower()
    if q == 'y':
        pass
    else:
        more_courses = False
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.

print('Enter a subject, (e.g. COS) to search through the courses you entered.')
subject = input('Enter Subject Here: ')
s = {}
for course_id, course_name in course_list.items():
    if subject.lower() in course_id.lower():
        s[course_id] = course_name
print(s)
