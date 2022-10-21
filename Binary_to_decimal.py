"""
num = int(input("Enter the number:"))

def convert(num):
    sum = 0
    i = 0
    while num != 0:
        a = num % 10
        sum = sum + a * pow(2, i)
        num = num // 10
        i += 1
    
    print("The conversion of Binary to decimal is", sum)

convert(num)
"""
























































