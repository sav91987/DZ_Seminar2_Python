number = int(input('Введите число N: '))
count = 0
pow = 1 
while pow <= number:
    print(f'2 в степени {count} равно {pow}')
    count+=1
    pow=2**count