numbers = []
user_number = -1

while user_number != 0:
    # ask user for a number
    user_number = int(input("please enter a number: "))

    if user_number != 0:
    # put it into te loop
        numbers.append(user_number)

print(numbers)

sum = 0
for number in numbers:
    sum = sum + number

count = len(numbers)
average = sum/count

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

# check for the smallest positive number
smallest_positive = 999999999999999

for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number

print(f"The sum is {sum}")
print(f"The average is {average}")
print(f"The largest number was {largest}")
print(f"The smallest_positive number is {smallest_positive}")
