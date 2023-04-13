import random
num_x = random.randint(0,1000) 
num_y = random.randint(0,1000) 

num_iterat = 1000
sum = num_x + num_y
multy = num_x * num_y

if sum < num_iterat: num_iterat = sum 
flag = False
for i in range(num_iterat+1):
    for j in range(num_iterat+1):
        if i+j ==sum and i*j == multy:
            flag = True
            break
    if flag: break
print(f'Отгаданные числа {i} и {j}')

print(f'Загаданные числа {num_x} и {num_y}')