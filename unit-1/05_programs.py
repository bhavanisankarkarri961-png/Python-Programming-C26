#                              Program 1: Student Details

name = input("Enter your name: ")
code = input("Enter your code: ")

print("\n--- Student Details ---")
print("Name:", name)
print("Code:", code)
print("Congratulations!")

#                             Program 2: Hall Ticket Details

hall_ticket_number = input("Enter your hall ticket number: ")
date_of_birth = input("Enter your date of birth: ")
name = input("Enter your full name: ")

print("\n--- Hall Ticket Details ---")
print("Hall Ticket Number:", hall_ticket_number)
print("Date of Birth:", date_of_birth)
print("Name:", name)

#                           Program 3: Student Marks and Rank

polycet_marks = int(input("Enter your POLYCET marks: "))
ssc_marks = input("Enter your SSC marks: ")

ssc_rank = input("Enter your SSC rank: ")
polycet_rank = int(input("Enter your POLYCET rank: "))

print("\n--- Student Results ---")

print("POLYCET Marks:", polycet_marks)
print("SSC Marks:", ssc_marks)
print("SSC Rank:", ssc_rank)
print("POLYCET Rank:", polycet_rank)

print("Congratulations! Keep learning.")

#                          Program 4: Print List Without Brackets and Commas

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(*numbers)