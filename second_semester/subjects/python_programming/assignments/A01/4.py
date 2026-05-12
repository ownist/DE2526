# =========================
# ৪. ত্রিভুজের ক্ষেত্রফল নির্ণয়
# =========================
import math


def tringle_area():
    a = float(input("Enter first arm: "))
    b = float(input("Enter second arm: "))
    c = float(input("Enter third arm: "))

    if (a + b) > c and (b + c) > a and (a + c) > b:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Triangle area: {area}")
    else:
        print("Triangle is not possible")


tringle_area()
