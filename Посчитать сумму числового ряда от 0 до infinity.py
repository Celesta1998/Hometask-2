a = input()
sum = 0
multiply = 1
for digit in a:
    if digit.isdigit():
        sum +=int(digit)
        multiply *= int(digit)
print('Сумма:',sum)
print('Произведение:',multiply)