print('Если ноль введётся как знак''\nПрограмма сойдёт с ума:D')
while True:
    a = input('Znak(+,-,*,/):')
    if a == '0':
        break
    if a in('+','-','*','/'):
        q = float(input('x='))
        w = float(input('y='))
        if a == '+':
            print('%.2f'%(q+w))
        elif a == '-':
            print('%.2f'%(q-w))
        elif a == '*':
            print('%.2f'%(q*w))
        elif a == '/':
            if w != 0:
             print('%.2f'%(q/w))
        else:
            print('Поделить на ноль!')
    else:
        print('Неверный знак')

