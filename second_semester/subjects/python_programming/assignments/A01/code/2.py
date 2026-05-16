# =======================
# ২. সবচেয়ে ছোট সংখ্যা নির্ণয়
# =======================
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
third_number = int(input("Enter your third number: "))

smallest_number = 0

# checking
if first_number < second_number and first_number < third_number:
    smallest_number = first_number
elif second_number < first_number and second_number < third_number:
    smallest_number = second_number
else:
    smallest_number = third_number


print(
    f"{smallest_number} is the smalles number than {first_number}, {second_number} and {third_number}"
)
