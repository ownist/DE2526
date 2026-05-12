# ========================
# দ্বিঘাত সমীকরণের সমাধান নির্ণয়
# ========================
import cmath

a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
c = float(input("Enter c value: "))

d = (b**2) - (4 * a * c)

root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b - cmath.sqrt(d)) / (2 * a)

print(f"somikoroner somadhan gulo holo: {root1} and {root2}")
