import math

def divisor(n):
    for i in range(1,int(math.sqrt(n)) +1):
        if n%i==0:
            print(i)
            if n/i != i:
                print(int(n/i))
            



divisor(16)


# t math

# # Function to find and print all divisors of a number
# def print_divisors(number):
#     print(f"Divisors of {number} are:")
#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             print(i)  # Print the divisor
#             if i != number // i:  # Check for the corresponding divisor
#                 print(number // i)

# # Example usage
# num = int(input("Enter a number: "))
# print_divisors(num)
