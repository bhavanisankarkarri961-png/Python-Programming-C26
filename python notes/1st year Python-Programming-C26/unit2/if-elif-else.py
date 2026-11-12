# ==========================================
# PYTHON PROGRAMMING C26
# UNIT 2 - CONDITIONAL STATEMENTS
# ==========================================


# Program 1: Ticket Price with Discount

ticket_price = 200

age = int(input("Enter your age: "))
show_time = input("Enter show time: ").strip().lower()

discount1 = 50
discount2 = 20

if age >= 60 and show_time == "afternoon":
    ticket_price -= discount1 + discount2
    print("You will pay only:", ticket_price)

elif age >= 60:
    ticket_price -= discount1
    print("You will pay only:", ticket_price)

elif show_time == "afternoon":
    ticket_price -= discount2
    print("You will pay only:", ticket_price)

else:
    print("You will pay the full amount:", ticket_price)


# ==========================================

# Program 2: Student Grade Calculation

student_marks = int(input("\nEnter your marks: "))

if student_marks < 0 or student_marks > 100:
    print("Invalid marks")

elif student_marks >= 90:
    print("Congratulations! Your grade is A+")

elif student_marks >= 75:
    print("Congratulations! Your grade is A")

elif student_marks >= 50:
    print("Good! Your grade is B")

elif student_marks >= 35:
    print("You are pass")

else:
    print("You are fail")


# ==========================================
# END OF CONDITIONAL STATEMENTS
# ==========================================