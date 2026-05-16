# ===================
# ১. সবচেয়ে বড় সংখ্যা নির্ণয়
# ===================
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

largest_number = 0

if first > second and first > third:
    largest_number = first
elif second > first and second > third:
    largest_number = second
else:
    largest_number = third

print(f"{largest_number} is the largest number than {first}, {second} and {third}.")
