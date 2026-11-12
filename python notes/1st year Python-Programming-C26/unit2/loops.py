
# ============================================================
# Python Programming - Unit 2
# File: loops.py
# Topic: Looping Statements and Number Programs
# ============================================================


# Programme 1: Multiplication Table of 5
def multiplication_table():
    number = 5

    print("Multiplication Table of", number)

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


# Programme 2: Print Even Numbers from 2 to 20
def even_numbers():
    print("Even numbers from 2 to 20:")

    for number in range(2, 21, 2):
        print(number, end=" ")

    print()


# Programme 3: Check Palindrome Number
def check_palindrome():
    number = int(input("Enter a number: "))

    original_number = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    if original_number >= 0 and original_number == reverse:
        print(original_number, "is a Palindrome Number.")
    else:
        print(original_number, "is not a Palindrome Number.")


# Programme 4: Check Armstrong Number
def check_armstrong():
    number = int(input("Enter a number: "))

    if number < 0:
        print("Armstrong number is not defined for negative numbers.")
        return

    original_number = number
    power = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** power
        number //= 10

    if original_number == total:
        print(original_number, "is an Armstrong Number.")
    else:
        print(original_number, "is not an Armstrong Number.")


# Programme 5: Check Prime Number
def check_prime():
    number = int(input("Enter a number: "))

    if number <= 1:
        print(number, "is neither Prime nor Composite.")

    else:
        for i in range(2, number):
            if number % i == 0:
                print(number, "is a Composite Number.")
                break
        else:
            print(number, "is a Prime Number.")


# Programme 6: Print Fibonacci Series
def fibonacci_series():
    terms = int(input("Enter the number of terms: "))

    first = 0
    second = 1

    if terms <= 0:
        print("Please enter a positive number.")

    else:
        print("Fibonacci Series:")

        for i in range(terms):
            print(first, end=" ")
            first, second = second, first + second

        print()


# Programme 7: Reverse a Number
def reverse_number():
    number = int(input("Enter a number: "))

    original_number = number
    number = abs(number)
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    if original_number < 0:
        reverse = -reverse

    print("Reverse of the number:", reverse)


# Programme 8: Number Pyramid
def number_pyramid():
    rows = int(input("Enter number of rows: "))

    if rows <= 0:
        print("Please enter a positive number.")
        return

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")

        print()


# Programme 9: Find Armstrong Numbers from 100 to 10000
def find_armstrong_numbers():
    armstrong_numbers = []

    for number in range(100, 10001):
        original_number = number
        power = len(str(number))
        total = 0

        while number > 0:
            digit = number % 10
            total += digit ** power
            number //= 10

        if total == original_number:
            armstrong_numbers.append(original_number)

    print("Armstrong numbers between 100 and 10000:")
    print(armstrong_numbers)


# Programme 10: Find Strong Numbers
def find_strong_numbers():
    strong_numbers = []

    for number in range(1, 1000):
        original_number = number
        total = 0

        while number > 0:
            digit = number % 10
            number //= 10

            factorial = 1

            for i in range(1, digit + 1):
                factorial *= i

            total += factorial

        if total == original_number:
            strong_numbers.append(original_number)

    print("Strong numbers between 1 and 999:")
    print(strong_numbers)


# Programme 11: Decimal to Binary Conversion
def decimal_to_binary():
    number = int(input("Enter a decimal number: "))

    if number < 0:
        print("Please enter a non-negative number.")
        return

    if number == 0:
        print("Binary representation: 0")
        return

    binary_digits = []

    while number > 0:
        remainder = number % 2
        binary_digits.append(str(remainder))
        number //= 2

    binary_number = "".join(binary_digits[::-1])

    print("Binary representation:", binary_number)


# Programme 12: Sum of First 10 Prime Numbers
def sum_first_ten_primes():
    prime_numbers = []

    for number in range(2, 100):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)

        if len(prime_numbers) == 10:
            break

    print("First 10 Prime Numbers:", prime_numbers)
    print("Sum:", sum(prime_numbers))


# Programme 13: Find Twin Prime Numbers from 1 to 50
def twin_prime_numbers():
    prime_numbers = []

    for number in range(2, 51):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)

    print("Twin Prime Numbers between 1 and 50:")

    for i in range(len(prime_numbers) - 1):
        if prime_numbers[i + 1] - prime_numbers[i] == 2:
            print(prime_numbers[i], ",", prime_numbers[i + 1])


# ============================================================
# Main Function
# ============================================================
def main():
    print("\n========== UNIT 2 - LOOPS ==========")
    print("1. Multiplication Table of 5")
    print("2. Even Numbers")
    print("3. Palindrome Number")
    print("4. Armstrong Number")
    print("5. Prime Number")
    print("6. Fibonacci Series")
    print("7. Reverse a Number")
    print("8. Number Pyramid")
    print("9. Armstrong Numbers in a Range")
    print("10. Strong Numbers")
    print("11. Decimal to Binary")
    print("12. Sum of First 10 Prime Numbers")
    print("13. Twin Prime Numbers")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        multiplication_table()
    elif choice == 2:
        even_numbers()
    elif choice == 3:
        check_palindrome()
    elif choice == 4:
        check_armstrong()
    elif choice == 5:
        check_prime()
    elif choice == 6:
        fibonacci_series()
    elif choice == 7:
        reverse_number()
    elif choice == 8:
        number_pyramid()
    elif choice == 9:
        find_armstrong_numbers()
    elif choice == 10:
        find_strong_numbers()
    elif choice == 11:
        decimal_to_binary()
    elif choice == 12:
        sum_first_ten_primes()
    elif choice == 13:
        twin_prime_numbers()
    else:
        print("Invalid choice. Please select 1 to 13.")



if __name__ == "__main__":
    main()
