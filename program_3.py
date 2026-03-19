# Capital Quiz program
# Written By Wesley Greer on 3/19/2026

# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
import random
sc = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 'California':'Sacramento',
'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta',
'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka',
'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusetts':'Boston',
'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson City', 'Montana':'Helena',
'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe',
'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 'South Dakota':'Pierre',
'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier', 'Virginia':'Richmond',
'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

states = list(sc.keys())
correct_answers = 0
incorrect_answers = 0

# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.

print('This is a quiz on states and capitals. There are 10 questions total.')
for state in random.sample(list(sc.keys()), 10):
    state = random.choice(states)
    quiz = input(f"What is the capital of {state}? ").strip()
    if quiz.lower() == sc[state].lower():
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The capital of {state} is {sc[state]}.")
        incorrect_answers += 1

print('The quiz is over!')
print('The total number of questions you answered correctly is:', correct_answers)
print('The total number of questions you answered incorrectly is:', incorrect_answers)

