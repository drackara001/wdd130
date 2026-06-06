numbers = []

print("Enter a list of numbers, type 0 when finished.")

while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)

print(f"The sum is: {total}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")

positive_numbers = [n for n in numbers if n > 0]
if positive_numbers: 
    smallest_positive = min(positive_numbers)
    print(f"The smallest positive number is: {smallest_positive}")