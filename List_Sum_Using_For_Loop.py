list = {int(input("Enter a number: ")) for _ in range(int(input("How many numbers? ")))}
total = sum(list)

print("The list of numbers:", list)
print("The sum of all numbers:", total)
