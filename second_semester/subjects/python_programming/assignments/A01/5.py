# ===================
# ৫. গ্রেড নির্ণয়
# ===================
grade = float(input("Enter your grade: "))

if grade >= 80 and grade <= 100:
    print("A+")
elif grade >= 70 and grade <= 79:
    print("A")
elif grade >= 60 and grade <= 69:
    print("A-")
elif grade >= 50 and grade <= 59:
    print("B")
elif grade >= 40 and grade <= 49:
    print("C")
elif grade >= 33 and grade <= 39:
    print("D")
elif grade >= 0 and grade <= 32:
    print("Fail")
else:
    print(f"{grade} is Invalid marks. Please provide a valid marks")
